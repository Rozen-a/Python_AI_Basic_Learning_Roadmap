import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator  # 刻度定位器


class Trainer:
    """模型训练器类，包含训练、评估和画图功能"""
    
    def __init__(self, model, criterion=None, optimizer=None, device=None, 
                 train_loader=None, val_loader=None,
                 early_stopping=True, patience=5, monitor='val_loss', min_delta=0.001, restore_best_weights=True):
        """
        初始化训练器
        
        Args:
            model: 要训练的模型
            criterion: 损失函数，默认为CrossEntropyLoss
            optimizer: 优化器，默认为SGD
            device: 设备（cuda/cpu），默认自动选择
            train_loader: 训练数据加载器（可选，可在初始化时传入或train方法中传入）
            val_loader: 验证数据加载器（可选，可在初始化时传入或train方法中传入）
            early_stopping: 是否启用早停，默认为False
            patience: 早停耐心值，验证指标连续patience个epoch没有改善则停止训练，默认为5
            monitor: 监控指标，'val_loss'（验证损失）或'val_acc'（验证准确率），默认为'val_loss'
            min_delta: 最小改善幅度，只有改善超过min_delta才算有效改善，默认为0.001
            restore_best_weights: 是否在早停后恢复最佳模型权重，默认为True
        """
        self.model = model
        self.criterion = criterion if criterion is not None else nn.CrossEntropyLoss()
        self.device = device if device is not None else torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        
        # 如果未提供优化器，使用默认的SGD优化器
        if optimizer is None:
            # 创建SGD（随机梯度下降）优化器
            # optim.SGD: PyTorch提供的随机梯度下降优化器，用于更新模型参数以最小化损失函数
            # model.parameters(): 获取模型所有需要训练的参数（权重和偏置），优化器将对这些参数进行更新
            # lr=0.01: 学习率（learning rate），控制每次参数更新的步长大小
            #          - 值越大，参数更新幅度越大，训练速度越快，但可能跳过最优解
            #          - 值越小，参数更新幅度越小，训练更稳定，但速度较慢
            #          - 0.01是一个常用的中等学习率，适合大多数深度学习任务
            # momentum=0.9: 动量系数，用于加速SGD优化过程并减少震荡
            #               - 动量机制会保留之前梯度更新的方向，使优化器能够"记住"之前的更新趋势
            #               - 取值范围通常在0到1之间，0.9是常用的值
            #               - 值越大，对历史梯度的依赖越强，有助于在梯度方向一致时加速收敛
            #               - 同时有助于在梯度方向变化时减少震荡，使训练过程更平滑
            # 这行代码的作用：初始化一个SGD优化器，用于在训练过程中根据损失函数的梯度更新模型参数
            self.optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)   
        else:
            self.optimizer = optimizer
        
        # 存储数据加载器（可选）
        self.train_loader = train_loader
        self.val_loader = val_loader
        
        # 用于存储训练历史
        self.train_losses = []
        self.val_losses = []
        self.train_accuracies = []  # 训练准确率
        self.val_accuracies = []
        
        # 早停相关配置（可在初始化时设置，也可在train方法中覆盖）
        self.early_stopping = early_stopping
        self.patience = patience
        self.monitor = monitor
        self.min_delta = min_delta
        self.restore_best_weights = restore_best_weights
        
        # 早停相关状态变量
        self.best_val_loss = float('inf')
        self.best_val_acc = 0.0
        self.best_epoch = 0
        self.best_model_state = None
        
        # 打印初始化信息
        print("=" * 60)
        print("Trainer 初始化完成")
        print("=" * 60)
        print(f"设备: {self.device}")
        print(f"损失函数: {self.criterion}")
        print(f"优化器: {self.optimizer}")
        if train_loader is not None:
            print(f"训练集: {len(train_loader.dataset)} 个样本, {len(train_loader)} 个批次")
        if val_loader is not None:
            print(f"验证集: {len(val_loader.dataset)} 个样本, {len(val_loader)} 个批次")
        if early_stopping:
            print(f"早停: 启用 (patience={patience}, monitor={monitor}, min_delta={min_delta})")
        print("=" * 60)
    
    def evaluating(self, dataloader=None, verbose=True):
        """
        评估函数，计算模型在数据集上的平均损失和准确率
        
        Args:
            dataloader: 数据加载器（可选，如果为None则使用初始化时传入的val_loader）
            verbose: 是否打印评估信息，默认为True
            
        Returns:
            avg_loss: 平均损失
            avg_acc: 准确率
        """
        # 如果没有传入dataloader，使用初始化时设置的val_loader
        if dataloader is None:
            if self.val_loader is None:
                raise ValueError("请提供dataloader参数，或在初始化时设置val_loader")
            dataloader = self.val_loader
        
        if verbose:
            print(f"\n开始评估模型...")
            print(f"评估数据集: {len(dataloader.dataset)} 个样本, {len(dataloader)} 个批次")
        
        self.model.eval()  # 设置为评估模式
        correct = 0  # 正确预测的样本数量
        total = 0    # 样本总数
        loss_sum = 0.0  # 累加损失之和
        
        with torch.no_grad():  # 关闭自动求导，节省内存与计算
            for images, labels in dataloader:  # 遍历dataloader中的所有批次
                images, labels = images.to(self.device), labels.to(self.device)  # 将数据移动到指定的设备
                outputs = self.model(images)  # 前向传播，计算输出
                loss = self.criterion(outputs, labels)  # 计算当前批次的损失
                loss_sum += loss.item() * labels.size(0)  # 将损失乘以该批样本数累加到总损失
                predicted = torch.argmax(outputs, dim=1)  # 取概率最大的类别作为预测结果
                total += labels.size(0)  # 累加样本总数
                correct += (predicted == labels).sum().item()  # 累加预测正确的数量
        
        avg_loss = loss_sum / total  # 计算平均损失
        avg_acc = correct / total   # 计算准确率
        
        if verbose:
            print(f"评估完成 - 损失: {avg_loss:.4f}, 准确率: {avg_acc:.4f} ({correct}/{total})")
        
        return avg_loss, avg_acc    # 返回平均损失和准确率
    
    def train(self, train_loader=None, val_loader=None, num_epochs=10, verbose=True,
              early_stopping=None, patience=None, monitor=None, min_delta=None, restore_best_weights=None):
        """
        训练模型
        
        Args:
            train_loader: 训练数据加载器（可选，如果为None则使用初始化时传入的train_loader）
            val_loader: 验证数据加载器（可选，如果为None则使用初始化时传入的val_loader）
            num_epochs: 训练轮数，默认为10
            verbose: 是否打印训练信息，默认为True
            early_stopping: 是否启用早停（可选，如果为None则使用初始化时的设置）
            patience: 早停耐心值（可选，如果为None则使用初始化时的设置）
            monitor: 监控指标，'val_loss'或'val_acc'（可选，如果为None则使用初始化时的设置）
            min_delta: 最小改善幅度（可选，如果为None则使用初始化时的设置）
            restore_best_weights: 是否恢复最佳模型权重（可选，如果为None则使用初始化时的设置）
        """
        # 早停相关参数：使用传入的参数，如果为None则使用初始化时的设置
        early_stopping = self.early_stopping if early_stopping is None else early_stopping
        patience = self.patience if patience is None else patience
        monitor = self.monitor if monitor is None else monitor
        min_delta = self.min_delta if min_delta is None else min_delta
        restore_best_weights = self.restore_best_weights if restore_best_weights is None else restore_best_weights

        # 如果没有传入数据加载器，使用初始化时设置的
        if train_loader is None:
            if self.train_loader is None:
                raise ValueError("请提供train_loader参数，或在初始化时设置train_loader")
            train_loader = self.train_loader
        
        if val_loader is None:
            if self.val_loader is None:
                raise ValueError("请提供val_loader参数，或在初始化时设置val_loader")
            val_loader = self.val_loader
        
        # 打印训练配置信息
        if verbose:
            print("\n" + "=" * 60)
            print("开始训练模型")
            print("=" * 60)
            print(f"训练轮数: {num_epochs}")
            print(f"训练集: {len(train_loader.dataset)} 个样本, {len(train_loader)} 个批次")
            print(f"验证集: {len(val_loader.dataset)} 个样本, {len(val_loader)} 个批次")
            print(f"设备: {self.device}")
            print(f"优化器: {self.optimizer}")
            if early_stopping:
                print(f"早停: 启用 (patience={patience}, monitor={monitor}, min_delta={min_delta})")
            print("=" * 60)
            print()
        
        # 清空历史记录
        self.train_losses = []
        self.val_losses = []
        self.train_accuracies = []
        self.val_accuracies = []
        
        # 早停相关变量初始化
        self.best_val_loss = float('inf')
        self.best_val_acc = 0.0
        self.best_epoch = 0
        self.best_model_state = None
        patience_counter = 0  # 早停计数器
        
        # 模型训练
        for epoch in range(num_epochs):
            self.model.train()  # 设置为训练模式
            running_loss = 0.0
            train_correct = 0
            train_total = 0
            
            for images, labels in train_loader:
                images, labels = images.to(self.device), labels.to(self.device)

                self.optimizer.zero_grad()           # 梯度清零，避免梯度累积
                outputs = self.model(images)         # 前向传播
                loss = self.criterion(outputs, labels)  # 计算损失
                loss.backward()                 # 反向传播，计算梯度
                self.optimizer.step()                # 根据梯度更新模型参数

                running_loss += loss.item() * labels.size(0)  # 将每个batch的损失乘以batch大小后累加到total running_loss
                
                # 计算训练准确率
                predicted = torch.argmax(outputs, dim=1)
                train_total += labels.size(0)
                train_correct += (predicted == labels).sum().item()

            train_loss = running_loss / len(train_loader.dataset)  # 计算整个训练集的平均损失
            train_acc = train_correct / train_total  # 计算训练准确率
            val_loss, val_acc = self.evaluating(val_loader, verbose=False)  # 用验证集评估模型，获得平均损失与准确率

            self.train_losses.append(train_loss)
            self.val_losses.append(val_loss)
            self.train_accuracies.append(train_acc)
            self.val_accuracies.append(val_acc)
            
            # 早停逻辑
            improved = False  # 是否改善标志
            if early_stopping:
                if monitor == 'val_loss':
                    # 监控验证损失，越小越好
                    if val_loss < self.best_val_loss - min_delta:
                        improved = True  # 设置为True，表示有改善
                        self.best_val_loss = val_loss  # 更新最佳验证损失
                        self.best_epoch = epoch + 1  # 更新最佳轮数
                        patience_counter = 0  # 重置早停计数器
                        # 保存最佳模型状态
                        if restore_best_weights:
                            self.best_model_state = self.model.state_dict().copy()
                    else:  # 没有改善，增加早停计数器
                        patience_counter += 1
                elif monitor == 'val_acc':
                    # 监控验证准确率，越大越好
                    if val_acc > self.best_val_acc + min_delta:
                        improved = True  # 设置为True，表示有改善
                        self.best_val_acc = val_acc  # 更新最佳验证准确率
                        self.best_epoch = epoch + 1  # 更新最佳轮数
                        patience_counter = 0  # 重置早停计数器
                        # 保存最佳模型状态
                        if restore_best_weights:
                            self.best_model_state = self.model.state_dict().copy()
                    else:  # 没有改善，增加早停计数器
                        patience_counter += 1
                
                # 检查是否应该早停
                if patience_counter >= patience:  # 如果早停计数器达到耐心值，则早停
                    if verbose:
                        print(f"\n早停触发！验证指标连续 {patience} 个epoch没有改善")
                        best_value = self.best_val_loss if monitor == 'val_loss' else self.best_val_acc
                        print(f"最佳轮数: {self.best_epoch}, 最佳{monitor}: {best_value:.4f}")
                    
                    # 恢复最佳模型权重
                    # 将模型参数回退到验证集上表现最好的轮次，而不是停留在早停时的状态，从而确保使用性能最好的模型
                    if restore_best_weights and self.best_model_state is not None:
                        self.model.load_state_dict(self.best_model_state)
                        if verbose:
                            print("已恢复最佳模型权重")
                    
                    break  # 提前结束训练

            # 打印训练信息
            if verbose:  
                print(f"Epoch [{epoch+1}/{num_epochs}], "
                      f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}, "
                      f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
        
        # 训练完成提示
        if verbose:
            print("\n" + "=" * 60)
            if early_stopping and patience_counter >= patience:
                print("训练提前结束（早停）！")
            else:
                print("训练完成！")
            print("=" * 60)
            print(f"总训练轮数(实际轮数/计划轮数): {len(self.train_losses)}/{num_epochs}")
            print(f"最佳轮数: {self.best_epoch}")
            if monitor == 'val_loss':
                print(f"最佳验证损失: {self.best_val_loss:.4f}")
            else:
                print(f"最佳验证准确率: {self.best_val_acc:.4f}")
            print(f"最终训练损失: {self.train_losses[-1]:.4f}")
            print(f"最终训练准确率: {self.train_accuracies[-1]:.4f}")
            print(f"最终验证损失: {self.val_losses[-1]:.4f}")
            print(f"最终验证准确率: {self.val_accuracies[-1]:.4f}")
            print("=" * 60)
    
    def plot_history(self, figsize=(16, 5), verbose=True):
        """
        绘制训练历史曲线（损失和准确率）
        
        Args:
            figsize: 图像大小，默认为(10, 5)
            verbose: 是否打印绘图信息，默认为True
        """
        if not self.train_losses:
            print("警告：没有训练历史数据，请先调用train方法进行训练")
            return
        
        if verbose:
            print("\n" + "=" * 60)
            print("开始绘制训练历史曲线")
            print("=" * 60)
            print(f"训练轮数: {len(self.train_losses)}")
            print(f"图像大小: {figsize}")
            print("=" * 60)
        
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
        plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
        
        epochs = range(1, len(self.train_losses) + 1)

        # 创建左右分布的两个子图
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))
        
        # 左图：损失曲线
        ax1.plot(epochs, self.train_losses, '-', label='训练损失')
        ax1.plot(epochs, self.val_losses, '-', label='验证损失')
        ax1.set_xlabel('轮数')
        ax1.set_ylabel('损失')
        ax1.set_title('训练与验证损失')
        ax1.legend()
        ax1.grid(True, alpha=0.3)  # 显示网格线，alpha=0.3表示透明度为0.3
        # 设置X轴只显示整数轮数，Y轴显示更多刻度
        ax1.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=min(15, len(self.train_losses))))  # X轴只显示整数
        ax1.yaxis.set_major_locator(MaxNLocator(nbins=10))  # Y轴显示更多刻度
        
        # 右图：准确率曲线
        ax2.plot(epochs, self.train_accuracies, '-', label='训练准确率')
        ax2.plot(epochs, self.val_accuracies, '-', label='验证准确率')
        ax2.set_xlabel('轮数')
        ax2.set_ylabel('准确率')
        ax2.set_title('训练与验证准确率')
        ax2.legend()
        ax2.grid(True, alpha=0.3)  # 显示网格线，alpha=0.3表示透明度为0.3
        # 设置X轴只显示整数轮数，Y轴显示更多刻度
        ax2.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=min(15, len(self.train_losses))))  # X轴只显示整数
        ax2.yaxis.set_major_locator(MaxNLocator(nbins=10))  # Y轴显示更多刻度
        
        plt.tight_layout()  # 自动调整布局，避免重叠
        plt.show()
        
        if verbose:
            print("训练历史曲线绘制完成！")
            print("=" * 60)


if __name__ == '__main__':
    """
    使用随机生成的简单数据测试 Trainer 类
    """
    print("=" * 60)
    print("Trainer 类测试示例")
    print("=" * 60)
    
    # 1. 创建一个简单的神经网络模型
    class SimpleModel(nn.Module):
        def __init__(self, input_size=784, hidden_size=128, num_classes=10):
            super().__init__()
            self.flatten = nn.Flatten()
            self.fc1 = nn.Linear(input_size, hidden_size)
            self.relu = nn.ReLU()
            self.fc2 = nn.Linear(hidden_size, num_classes)
        
        def forward(self, x):
            x = self.flatten(x)
            x = self.fc1(x)
            x = self.relu(x)
            x = self.fc2(x)
            return x
    
    # 2. 生成随机训练数据
    print("\n生成随机数据...")
    num_train_samples = 100
    num_val_samples = 50
    input_size = 784  # 28x28 图像展平后的尺寸
    num_classes = 10
    
    # 生成随机图像数据 (batch, channels, height, width)
    train_images = torch.randn(num_train_samples, 1, 28, 28)
    train_labels = torch.randint(0, num_classes, (num_train_samples,))
    
    val_images = torch.randn(num_val_samples, 1, 28, 28)
    val_labels = torch.randint(0, num_classes, (num_val_samples,))
    
    print(f"训练集: {num_train_samples} 个样本")
    print(f"验证集: {num_val_samples} 个样本")
    
    # 3. 创建数据加载器
    from torch.utils.data import TensorDataset, DataLoader
    
    train_dataset = TensorDataset(train_images, train_labels)
    val_dataset = TensorDataset(val_images, val_labels)
    
    batch_size = 16  # 减小批次大小，加快每个epoch的速度
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    
    print(f"批次大小: {batch_size}")
    print(f"训练批次数: {len(train_loader)}")
    print(f"验证批次数: {len(val_loader)}")
    
    # 4. 创建模型实例（简化模型）
    print("\n创建模型...")
    model = SimpleModel(input_size=input_size, hidden_size=64, num_classes=num_classes)  # 减少隐藏层大小
    
    # 计算模型参数数量
    total_params = sum(p.numel() for p in model.parameters())
    print(f"模型参数总数: {total_params:,}")
    
    # 5. 创建 Trainer 实例（在初始化时设置早停参数）
    print("\n创建 Trainer...")
    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        early_stopping=True,  # 在初始化时启用早停
        patience=5,  # 连续5个epoch没有改善则停止
        monitor='val_loss',  # 监控验证损失
        min_delta=0.001,  # 最小改善幅度
        restore_best_weights=True  # 恢复最佳模型权重
    )
    
    # 6. 训练模型（使用初始化时设置的早停参数）
    print("\n开始训练...")
    num_epochs = 111  # 设置最大训练轮数
    trainer.train(num_epochs=num_epochs)  # 早停参数已在初始化时设置，这里可以省略
    
    # 7. 评估模型
    print("\n评估模型...")
    val_loss, val_acc = trainer.evaluating()
    print(f"最终验证结果 - 损失: {val_loss:.4f}, 准确率: {val_acc:.4f}")
    
    # 8. 绘制训练历史曲线
    print("\n绘制训练历史曲线...")
    trainer.plot_history()
    
    print("\n" + "=" * 60)
    print("测试完成！")
    print("=" * 60)

