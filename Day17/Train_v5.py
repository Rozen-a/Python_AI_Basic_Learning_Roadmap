"""
基于Train_v4.py的改进版
1. 添加二分类的训练和评估方法
"""
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator  # 刻度定位器
import os
import __main__


class Trainer:
    """模型训练器类，包含训练、评估和画图功能"""
    
    def __init__(self, model, criterion=None, optimizer=None, device=None, 
                 train_loader=None, val_loader=None,
                 early_stopping=True, patience=5, monitor='val_loss', min_delta=0.001, restore_best_weights=True,
                 save_best_model=True, save_every_epoch=False, save_dir='./checkpoints', model_name=None):
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
            save_best_model: 是否保存最佳模型，默认为True
            save_every_epoch: 是否每个epoch都保存模型，默认为False
            save_dir: 模型保存目录，默认为'./checkpoints'
            model_name: 模型名称（用于生成文件名），
                        默认为：训练脚本文件名（不含扩展名） + '_model'
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
        self.best_val_acc = -float('inf')
        self.best_epoch = 0
        self.best_model_state = None
        self.patience_counter = 0  # 早停计数器
        
        # 模型保存相关配置
        self.save_best_model = save_best_model
        self.save_every_epoch = save_every_epoch
        self.save_dir = save_dir
        # 模型名称：默认使用“训练脚本文件名_model”
        if model_name is None:
            # 优先使用主运行脚本的文件名；如果没有（例如在Notebook中），则退回当前文件名
            script_file = getattr(__main__, '__file__', None)
            if script_file is not None:
                base_name = os.path.splitext(os.path.basename(script_file))[0]
            else:
                base_name = os.path.splitext(os.path.basename(__file__))[0]
            self.model_name = f"{base_name}_model"
        else:
            self.model_name = model_name
        
        # 创建保存目录（如果不存在）
        if save_best_model or save_every_epoch:
            os.makedirs(save_dir, exist_ok=True)
        
        # 打印初始化信息
        print("=" * 60)
        print("Trainer 初始化完成")
        print("=" * 60)
        print(f"设备: {self.device}")
        print(f"损失函数: {self.criterion}")
        print(f"优化器: {self.optimizer}")
        print(f"模型名称: {self.model_name}")
        if train_loader is not None:
            print(f"训练集: {len(train_loader.dataset)} 个样本, {len(train_loader)} 个批次")
        if val_loader is not None:
            print(f"验证集: {len(val_loader.dataset)} 个样本, {len(val_loader)} 个批次")
        if early_stopping:
            print(f"早停: 启用 (patience={patience}, monitor={monitor}, min_delta={min_delta})")
        if save_best_model:
            print(f"模型保存: 保存最佳模型 (保存目录: {save_dir})")
        if save_every_epoch:
            print(f"模型保存: 每个epoch都保存 (保存目录: {save_dir})")
        print("=" * 60)
    
    def evaluating_classification(self, dataloader=None, verbose=True):
        """
        分类任务评估函数，计算模型在数据集上的平均损失和准确率
        
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

    def evaluating_binary_classification(self, dataloader=None, verbose=True):
        """
        二分类任务评估函数（适用于输出为单个logit并使用BCEWithLogitsLoss等情况）
        
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
            print(f"\n开始评估二分类模型...")
            print(f"评估数据集: {len(dataloader.dataset)} 个样本, {len(dataloader)} 个批次")
        
        self.model.eval()
        correct = 0
        total = 0
        loss_sum = 0.0
        
        with torch.no_grad():
            for inputs, labels in dataloader:
                inputs = inputs.to(self.device)
                labels = labels.to(self.device)
                
                # 假设模型输出为形状 (N, 1) 或 (N,)
                logits = self.model(inputs)
                logits = logits.view(-1)
                targets = labels.view(-1).float()
                
                # 计算损失
                loss = self.criterion(logits, targets)
                loss_sum += loss.item() * targets.size(0)
                
                # 直接使用 logit 的符号做分类：logit >= 0 视为正类1，否则为0
                preds = (logits >= 0).long()
                total += targets.size(0)
                correct += (preds == targets.long()).sum().item()
        
        avg_loss = loss_sum / total
        avg_acc = correct / total
        
        if verbose:
            print(f"评估完成 - 损失: {avg_loss:.4f}, 准确率: {avg_acc:.4f} ({correct}/{total})")
        
        return avg_loss, avg_acc

    def evaluating_regression(self, dataloader=None, verbose=True):
        """
        回归任务评估函数，计算模型在数据集上的平均损失
        
        Args:
            dataloader: 数据加载器（可选，如果为None则使用初始化时传入的val_loader）
            verbose: 是否打印评估信息，默认为True
            
        Returns:
            avg_loss: 平均损失
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
        total = 0    # 样本总数
        loss_sum = 0.0  # 累加损失之和
        
        with torch.no_grad():  # 关闭自动求导，节省内存与计算
            for inputs, targets in dataloader:  # 遍历dataloader中的所有批次
                inputs, targets = inputs.to(self.device), targets.to(self.device)  # 将数据移动到指定的设备
                outputs = self.model(inputs)  # 前向传播，计算输出
                loss = self.criterion(outputs, targets)  # 计算当前批次的损失
                loss_sum += loss.item() * targets.size(0)  # 将损失乘以该批样本数累加到总损失
                total += targets.size(0)  # 累加样本总数
        
        avg_loss = loss_sum / total  # 计算平均损失
        
        if verbose:
            print(f"评估完成 - 损失: {avg_loss:.4f}")
        
        return avg_loss    # 返回平均损失
        
    def _save_model(self, epoch=None, is_best=False, train_loss=None, train_acc=None, 
                   val_loss=None, val_acc=None, model_state_dict=None, verbose=True):
        """
        保存模型
        
        Args:
            epoch: 当前轮数（如果为None，则保存为最佳模型）
            is_best: 是否为最佳模型，默认为False
            train_loss: 训练损失（可选，用于保存到文件名或信息中）
            train_acc: 训练准确率（可选）
            val_loss: 验证损失（可选）
            val_acc: 验证准确率（可选）
            model_state_dict: 模型状态字典（可选，如果为None则使用当前模型状态）
            verbose: 是否打印保存信息，默认为True
        """
        # 使用传入的模型状态或当前模型状态
        if model_state_dict is None:
            model_state_dict = self.model.state_dict()
        
        # 构建保存信息字典
        save_info = {
            'model_state_dict': model_state_dict,
            'optimizer_state_dict': self.optimizer.state_dict(),
        }
        
        # 添加训练信息（如果提供）
        if epoch is not None:
            save_info['epoch'] = epoch
        if train_loss is not None:
            save_info['train_loss'] = train_loss
        if train_acc is not None:
            save_info['train_acc'] = train_acc
        if val_loss is not None:
            save_info['val_loss'] = val_loss
        if val_acc is not None:
            save_info['val_acc'] = val_acc
        
        # 构建文件名
        if is_best:
            # 最佳模型文件名
            filename = f"{self.model_name}_best.pth"
        elif epoch is not None:
            # 每个epoch的模型文件名（包含轮次）
            filename = f"{self.model_name}_epoch_{epoch+1:04d}.pth"  # epoch是从0开始的，所以需要加1；将轮次格式化为4位数字
        else:
            # 默认文件名
            filename = f"{self.model_name}.pth"
        
        # 完整路径
        filepath = os.path.join(self.save_dir, filename)  # 将保存目录和文件名拼接成完整路径
        
        # 保存模型
        torch.save(save_info, filepath)
        
        if verbose:
            print(f"模型已保存: {filepath}")
    
    def _check_early_stopping(self, epoch, val_loss, val_acc, early_stopping, patience, 
                              monitor, min_delta, restore_best_weights, verbose):
        """
        检查是否应该早停
        
        Args:
            epoch: 当前轮数（从0开始）
            val_loss: 当前验证损失
            val_acc: 当前验证准确率
            early_stopping: 是否启用早停
            patience: 早停耐心值
            monitor: 监控指标，'val_loss'或'val_acc'
            min_delta: 最小改善幅度
            restore_best_weights: 是否恢复最佳模型权重
            verbose: 是否打印信息
            
        Returns:
            should_stop: 是否应该早停（bool）
        """
        if not early_stopping:
            return False
        
        improved = False  # 是否改善标志
        
        if monitor == 'val_loss':
            # 监控验证损失，越小越好
            if val_loss < self.best_val_loss - min_delta:
                improved = True  # 设置为True，表示有改善
                self.best_val_loss = val_loss  # 更新最佳验证损失
                self.best_epoch = epoch + 1  # 更新最佳轮数
                self.patience_counter = 0  # 重置早停计数器
                # 保存最佳模型状态
                if restore_best_weights:
                    self.best_model_state = self.model.state_dict().copy()
            else:  # 没有改善，增加早停计数器
                self.patience_counter += 1
        elif monitor == 'val_acc':
            # 监控验证准确率，越大越好
            if val_acc > self.best_val_acc + min_delta:
                improved = True  # 设置为True，表示有改善
                self.best_val_acc = val_acc  # 更新最佳验证准确率
                self.best_epoch = epoch + 1  # 更新最佳轮数
                self.patience_counter = 0  # 重置早停计数器
                # 保存最佳模型状态
                if restore_best_weights:
                    self.best_model_state = self.model.state_dict().copy()
            else:  # 没有改善，增加早停计数器
                self.patience_counter += 1
        
        # 检查是否应该早停
        if self.patience_counter >= patience:  # 如果早停计数器达到耐心值，则早停
            if verbose:
                print(f"\n早停触发！！！验证指标连续 {patience} 个epoch没有改善")
                best_value = self.best_val_loss if monitor == 'val_loss' else self.best_val_acc
                print(f"最佳轮数: {self.best_epoch}, 最佳{monitor}: {best_value:.4f}")
            
            # 恢复最佳模型权重
            # 将模型参数回退到验证集上表现最好的轮次，而不是停留在早停时的状态，从而确保使用性能最好的模型
            if restore_best_weights and self.best_model_state is not None:
                self.model.load_state_dict(self.best_model_state)
                if verbose:
                    print("已恢复最佳模型权重")
            
            return True  # 返回True表示应该早停
        
        return False  # 返回False表示不应该早停
        
    def train_classification(self, train_loader=None, val_loader=None, num_epochs=10, verbose=True,
              early_stopping=None, patience=None, monitor=None, min_delta=None, restore_best_weights=None,
              save_best_model=None, save_every_epoch=None):
        """
        分类任务训练函数
        
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
            save_best_model: 是否保存最佳模型（可选，如果为None则使用初始化时的设置）
            save_every_epoch: 是否每个epoch都保存（可选，如果为None则使用初始化时的设置）
        """
        # 早停相关参数：使用传入的参数，如果为None则使用初始化时的设置
        early_stopping = self.early_stopping if early_stopping is None else early_stopping
        patience = self.patience if patience is None else patience
        monitor = self.monitor if monitor is None else monitor
        min_delta = self.min_delta if min_delta is None else min_delta
        restore_best_weights = self.restore_best_weights if restore_best_weights is None else restore_best_weights
        
        # 模型保存相关参数：使用传入的参数，如果为None则使用初始化时的设置
        save_best_model = self.save_best_model if save_best_model is None else save_best_model
        save_every_epoch = self.save_every_epoch if save_every_epoch is None else save_every_epoch

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
            if save_best_model:
                print(f"模型保存: 保存最佳模型 (保存目录: {self.save_dir})")
            if save_every_epoch:
                print(f"模型保存: 每个epoch都保存 (保存目录: {self.save_dir})")
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
        self.patience_counter = 0  # 早停计数器
        
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
            val_loss, val_acc = self.evaluating_classification(val_loader, verbose=False)  # 用验证集评估模型，获得平均损失与准确率

            self.train_losses.append(train_loss)
            self.val_losses.append(val_loss)
            self.train_accuracies.append(train_acc)
            self.val_accuracies.append(val_acc)
            
            # 打印训练信息（先打印，再检查早停，这样触发早停的epoch也会在日志中出现）
            if verbose:  
                print(f"Epoch [{epoch+1}/{num_epochs}], "
                      f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}, "
                      f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
            
            # 每个epoch保存模型（如果开启）
            if save_every_epoch:
                self._save_model(
                    epoch=epoch,
                    is_best=False,
                    train_loss=train_loss,
                    train_acc=train_acc,
                    val_loss=val_loss,
                    val_acc=val_acc,
                    verbose=verbose
                )

            # 早停逻辑
            # 早停逻辑放在最后，这样触发早停的epoch也会完成打印、保存操作
            should_stop = self._check_early_stopping(
                epoch=epoch,
                val_loss=val_loss,
                val_acc=val_acc,
                early_stopping=early_stopping,
                patience=patience,
                monitor=monitor,
                min_delta=min_delta,
                restore_best_weights=restore_best_weights,
                verbose=verbose
            )
            
            if should_stop:
                break  # 提前结束训练
        
        # 训练完成提示
        if verbose:
            print("\n" + "=" * 60)
            if early_stopping and self.patience_counter >= patience:
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
        
        # 训练完成后保存最佳模型
        if save_best_model:
            # 确定最佳模型的指标值
            if monitor == 'val_loss':
                best_val_loss = self.best_val_loss
                best_val_acc = self.val_accuracies[self.best_epoch - 1] if self.best_epoch > 0 else self.val_accuracies[-1]
                best_train_loss = self.train_losses[self.best_epoch - 1] if self.best_epoch > 0 else self.train_losses[-1]
                best_train_acc = self.train_accuracies[self.best_epoch - 1] if self.best_epoch > 0 else self.train_accuracies[-1]
            else:  # monitor == 'val_acc'
                best_val_acc = self.best_val_acc
                best_val_loss = self.val_losses[self.best_epoch - 1] if self.best_epoch > 0 else self.val_losses[-1]
                best_train_loss = self.train_losses[self.best_epoch - 1] if self.best_epoch > 0 else self.train_losses[-1]
                best_train_acc = self.train_accuracies[self.best_epoch - 1] if self.best_epoch > 0 else self.train_accuracies[-1]
            
            # 使用最佳模型状态（如果存在），否则使用当前模型状态
            best_model_state = self.best_model_state if self.best_model_state is not None else self.model.state_dict()
            
            self._save_model(
                epoch=self.best_epoch - 1 if self.best_epoch > 0 else len(self.train_losses) - 1,
                is_best=True,
                train_loss=best_train_loss,
                train_acc=best_train_acc,
                val_loss=best_val_loss,
                val_acc=best_val_acc,
                model_state_dict=best_model_state,
                verbose=verbose
            )

    def train_binary_classification(self, train_loader=None, val_loader=None, num_epochs=10, verbose=True,
              early_stopping=None, patience=None, monitor=None, min_delta=None, restore_best_weights=None,
              save_best_model=None, save_every_epoch=None):
        """
        二分类任务训练函数（适用于输出为单个logit并使用BCEWithLogitsLoss等情况）
        
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
            save_best_model: 是否保存最佳模型（可选，如果为None则使用初始化时的设置）
            save_every_epoch: 是否每个epoch都保存（可选，如果为None则使用初始化时的设置）
        """
        # 早停相关参数：使用传入的参数，如果为None则使用初始化时的设置
        early_stopping = self.early_stopping if early_stopping is None else early_stopping
        patience = self.patience if patience is None else patience
        monitor = self.monitor if monitor is None else monitor
        min_delta = self.min_delta if min_delta is None else min_delta
        restore_best_weights = self.restore_best_weights if restore_best_weights is None else restore_best_weights
        
        # 模型保存相关参数：使用传入的参数，如果为None则使用初始化时的设置
        save_best_model = self.save_best_model if save_best_model is None else save_best_model
        save_every_epoch = self.save_every_epoch if save_every_epoch is None else save_every_epoch

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
            print("开始训练二分类模型")
            print("=" * 60)
            print(f"训练轮数: {num_epochs}")
            print(f"训练集: {len(train_loader.dataset)} 个样本, {len(train_loader)} 个批次")
            print(f"验证集: {len(val_loader.dataset)} 个样本, {len(val_loader)} 个批次")
            print(f"设备: {self.device}")
            print(f"优化器: {self.optimizer}")
            if early_stopping:
                print(f"早停: 启用 (patience={patience}, monitor={monitor}, min_delta={min_delta})")
            if save_best_model:
                print(f"模型保存: 保存最佳模型 (保存目录: {self.save_dir})")
            if save_every_epoch:
                print(f"模型保存: 每个epoch都保存 (保存目录: {self.save_dir})")
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
        self.patience_counter = 0  # 早停计数器
        
        # 模型训练
        for epoch in range(num_epochs):
            self.model.train()
            running_loss = 0.0
            train_correct = 0
            train_total = 0
            
            for inputs, labels in train_loader:
                inputs = inputs.to(self.device)
                labels = labels.to(self.device)

                # 假设模型输出为形状 (N, 1) 或 (N,)
                logits = self.model(inputs)
                logits = logits.view(-1)  # [N, 1] -> [N,]
                targets = labels.view(-1).float()

                # 计算损失
                self.optimizer.zero_grad()
                loss = self.criterion(logits, targets)
                loss.backward()
                self.optimizer.step()

                running_loss += loss.item() * targets.size(0)
                # 计算准确率：logit >= 0 判为1，否则为0
                preds = (logits >= 0).long()
                train_total += targets.size(0)
                train_correct += (preds == targets.long()).sum().item()
                
            # 计算平均损失和准确率
            train_loss = running_loss / len(train_loader.dataset)
            train_acc = train_correct / train_total
            # 用验证集评估模型，获得平均损失和准确率
            val_loss, val_acc = self.evaluating_binary_classification(val_loader, verbose=False)
            # 保存损失和准确率
            self.train_losses.append(train_loss)
            self.val_losses.append(val_loss)
            self.train_accuracies.append(train_acc)
            self.val_accuracies.append(val_acc)
            # 打印训练信息
            if verbose:
                print(f"Epoch [{epoch+1}/{num_epochs}], "
                      f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}, "
                      f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
            
            # 每个epoch保存模型（如果开启）
            if save_every_epoch:
                self._save_model(
                    epoch=epoch,
                    is_best=False,
                    train_loss=train_loss,
                    train_acc=train_acc,
                    val_loss=val_loss,
                    val_acc=val_acc,
                    verbose=verbose
                )

            # 早停逻辑
            should_stop = self._check_early_stopping(
                epoch=epoch,
                val_loss=val_loss,
                val_acc=val_acc,
                early_stopping=early_stopping,
                patience=patience,
                monitor=monitor,
                min_delta=min_delta,
                restore_best_weights=restore_best_weights,
                verbose=verbose
            )
            
            if should_stop:
                break
        
        # 训练完成提示
        if verbose:
            print("\n" + "=" * 60)
            if early_stopping and self.patience_counter >= patience:
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
        
        # 训练完成后保存最佳模型
        if save_best_model:
            # 确定最佳模型的指标值
            if monitor == 'val_loss':
                best_val_loss = self.best_val_loss
                best_val_acc = self.val_accuracies[self.best_epoch - 1] if self.best_epoch > 0 else self.val_accuracies[-1]
                best_train_loss = self.train_losses[self.best_epoch - 1] if self.best_epoch > 0 else self.train_losses[-1]
                best_train_acc = self.train_accuracies[self.best_epoch - 1] if self.best_epoch > 0 else self.train_accuracies[-1]
            else:  # monitor == 'val_acc'
                best_val_acc = self.best_val_acc
                best_val_loss = self.val_losses[self.best_epoch - 1] if self.best_epoch > 0 else self.val_losses[-1]
                best_train_loss = self.train_losses[self.best_epoch - 1] if self.best_epoch > 0 else self.train_losses[-1]
                best_train_acc = self.train_accuracies[self.best_epoch - 1] if self.best_epoch > 0 else self.train_accuracies[-1]
            
            # 使用最佳模型状态（如果存在），否则使用当前模型状态
            best_model_state = self.best_model_state if self.best_model_state is not None else self.model.state_dict()
            
            self._save_model(
                epoch=self.best_epoch - 1 if self.best_epoch > 0 else len(self.train_losses) - 1,
                is_best=True,
                train_loss=best_train_loss,
                train_acc=best_train_acc,
                val_loss=best_val_loss,
                val_acc=best_val_acc,
                model_state_dict=best_model_state,
                verbose=verbose
            )
    
    def train_regression(self, train_loader=None, val_loader=None, num_epochs=10, verbose=True,
              early_stopping=None, patience=None, monitor='val_loss', min_delta=None, restore_best_weights=None,
              save_best_model=None, save_every_epoch=None):
        """
        回归任务训练函数
        
        Args:
            train_loader: 训练数据加载器（可选，如果为None则使用初始化时传入的train_loader）
            val_loader: 验证数据加载器（可选，如果为None则使用初始化时传入的val_loader）
            num_epochs: 训练轮数，默认为10
            verbose: 是否打印训练信息，默认为True
            early_stopping: 是否启用早停（可选，如果为None则使用初始化时的设置）
            patience: 早停耐心值（可选，如果为None则使用初始化时的设置）
            monitor: 监控指标，默认为'val_loss'（回归任务只监控损失）
            min_delta: 最小改善幅度（可选，如果为None则使用初始化时的设置）
            restore_best_weights: 是否恢复最佳模型权重（可选，如果为None则使用初始化时的设置）
            save_best_model: 是否保存最佳模型（可选，如果为None则使用初始化时的设置）
            save_every_epoch: 是否每个epoch都保存（可选，如果为None则使用初始化时的设置）
        """
        # 早停相关参数：使用传入的参数，如果为None则使用初始化时的设置
        early_stopping = self.early_stopping if early_stopping is None else early_stopping
        patience = self.patience if patience is None else patience
        monitor = 'val_loss'  # 回归任务只监控损失
        min_delta = self.min_delta if min_delta is None else min_delta
        restore_best_weights = self.restore_best_weights if restore_best_weights is None else restore_best_weights
        
        # 模型保存相关参数：使用传入的参数，如果为None则使用初始化时的设置
        save_best_model = self.save_best_model if save_best_model is None else save_best_model
        save_every_epoch = self.save_every_epoch if save_every_epoch is None else save_every_epoch

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
            print("开始训练模型（回归任务）")
            print("=" * 60)
            print(f"训练轮数: {num_epochs}")
            print(f"训练集: {len(train_loader.dataset)} 个样本, {len(train_loader)} 个批次")
            print(f"验证集: {len(val_loader.dataset)} 个样本, {len(val_loader)} 个批次")
            print(f"设备: {self.device}")
            print(f"优化器: {self.optimizer}")
            if early_stopping:
                print(f"早停: 启用 (patience={patience}, monitor={monitor}, min_delta={min_delta})")
            if save_best_model:
                print(f"模型保存: 保存最佳模型 (保存目录: {self.save_dir})")
            if save_every_epoch:
                print(f"模型保存: 每个epoch都保存 (保存目录: {self.save_dir})")
            print("=" * 60)
            print()
        
        # 清空历史记录
        self.train_losses = []
        self.val_losses = []
        
        # 早停相关变量初始化
        self.best_val_loss = float('inf')
        self.best_epoch = 0
        self.best_model_state = None
        self.patience_counter = 0  # 早停计数器
        
        # 模型训练
        for epoch in range(num_epochs):
            self.model.train()  # 设置为训练模式
            running_loss = 0.0
            
            for inputs, targets in train_loader:
                inputs, targets = inputs.to(self.device), targets.to(self.device)

                self.optimizer.zero_grad()           # 梯度清零，避免梯度累积
                outputs = self.model(inputs)         # 前向传播
                loss = self.criterion(outputs, targets)  # 计算损失
                loss.backward()                 # 反向传播，计算梯度
                self.optimizer.step()                # 根据梯度更新模型参数

                running_loss += loss.item() * targets.size(0)  # 将每个batch的损失乘以batch大小后累加到total running_loss

            train_loss = running_loss / len(train_loader.dataset)  # 计算整个训练集的平均损失
            val_loss = self.evaluating_regression(val_loader, verbose=False)  # 用验证集评估模型，获得平均损失

            self.train_losses.append(train_loss)
            self.val_losses.append(val_loss)
            
            # 打印训练信息（先打印，再检查早停，这样触发早停的epoch也会在日志中出现）
            if verbose:  
                print(f"Epoch [{epoch+1}/{num_epochs}], "
                      f"Train Loss: {train_loss:.4f}, "
                      f"Val Loss: {val_loss:.4f}")
            
            # 每个epoch保存模型（如果开启）
            if save_every_epoch:
                self._save_model(
                    epoch=epoch,
                    is_best=False,
                    train_loss=train_loss,
                    train_acc=None,  # 回归任务不需要准确率
                    val_loss=val_loss,
                    val_acc=None,  # 回归任务不需要准确率
                    verbose=verbose
                )

            # 早停逻辑（回归任务只监控损失，不监控准确率）
            # 早停逻辑放在最后，这样触发早停的epoch也会完成打印、保存操作
            should_stop = self._check_early_stopping(
                epoch=epoch,
                val_loss=val_loss,
                val_acc=0.0,  # 回归任务不需要准确率，传入0.0
                early_stopping=early_stopping,
                patience=patience,
                monitor=monitor,
                min_delta=min_delta,
                restore_best_weights=restore_best_weights,
                verbose=verbose
            )
            
            if should_stop:
                break  # 提前结束训练
        
        # 训练完成提示
        if verbose:
            print("\n" + "=" * 60)
            if early_stopping and self.patience_counter >= patience:
                print("训练提前结束（早停）！")
            else:
                print("训练完成！")
            print("=" * 60)
            print(f"总训练轮数(实际轮数/计划轮数): {len(self.train_losses)}/{num_epochs}")
            print(f"最佳轮数: {self.best_epoch}")
            print(f"最佳验证损失: {self.best_val_loss:.4f}")
            print(f"最终训练损失: {self.train_losses[-1]:.4f}")
            print(f"最终验证损失: {self.val_losses[-1]:.4f}")
            print("=" * 60)
        
        # 训练完成后保存最佳模型
        if save_best_model:
            # 确定最佳模型的指标值
            best_val_loss = self.best_val_loss
            best_train_loss = self.train_losses[self.best_epoch - 1] if self.best_epoch > 0 else self.train_losses[-1]
            
            # 使用最佳模型状态（如果存在），否则使用当前模型状态
            best_model_state = self.best_model_state if self.best_model_state is not None else self.model.state_dict()
            
            self._save_model(
                epoch=self.best_epoch - 1 if self.best_epoch > 0 else len(self.train_losses) - 1,
                is_best=True,
                train_loss=best_train_loss,
                train_acc=None,  # 回归任务不需要准确率
                val_loss=best_val_loss,
                val_acc=None,  # 回归任务不需要准确率
                model_state_dict=best_model_state,
                verbose=verbose
            )
    
    def plot_history(self, figsize=(16, 5), plot_loss=True, plot_acc=True, verbose=True):
        """
        绘制训练历史曲线（损失和准确率）
        
        Args:
            figsize: 图像大小，默认为(16, 5)
            plot_loss: 是否绘制损失曲线，默认为True
            plot_acc: 是否绘制准确率曲线，默认为True（如果训练历史中没有准确率数据，会自动跳过）
            verbose: 是否打印绘图信息，默认为True
        """
        if not self.train_losses:
            print("警告：没有训练历史数据，请先调用train方法进行训练")
            return
        
        # 检查是否有准确率数据
        has_acc_data = (len(self.train_accuracies) > 0 and len(self.val_accuracies) > 0)
        
        # 如果要求绘制准确率但没有数据，给出警告并跳过
        if plot_acc and not has_acc_data:
            if verbose:
                print("警告：训练历史中没有准确率数据，将跳过准确率曲线的绘制")
            plot_acc = False
        
        # 如果两个都不绘制，给出警告并返回
        if not plot_loss and not plot_acc:
            print("警告：plot_loss 和 plot_acc 都为 False，没有可绘制的内容")
            return
        
        if verbose:
            print("\n" + "=" * 60)
            print("开始绘制训练历史曲线")
            print("=" * 60)
            print(f"训练轮数: {len(self.train_losses)}")
            print(f"图像大小: {figsize}")
            print(f"绘制损失曲线: {plot_loss}")
            print(f"绘制准确率曲线: {plot_acc}")
            print("=" * 60)
        
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
        plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
        
        epochs = range(1, len(self.train_losses) + 1)

        # 根据要绘制的曲线数量决定子图布局
        if plot_loss and plot_acc:
            # 两个都绘制：创建左右分布的两个子图
            fig, axes = plt.subplots(1, 2, figsize=figsize)
            ax1, ax2 = axes[0], axes[1]
        elif plot_loss:
            # 只绘制损失：单个子图
            fig, ax1 = plt.subplots(1, 1, figsize=(figsize[0] // 2, figsize[1]))
            ax2 = None
        else:
            # 只绘制准确率：单个子图
            fig, ax2 = plt.subplots(1, 1, figsize=(figsize[0] // 2, figsize[1]))
            ax1 = None
        
        # 绘制损失曲线
        if plot_loss and ax1 is not None:
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
        
        # 绘制准确率曲线
        if plot_acc and ax2 is not None:
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


def test_classification():
    """
    使用随机生成的简单数据测试 Trainer 类分类任务
    """
    print("=" * 60)
    print("Trainer 类分类任务测试示例")
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
    
    # 5. 创建 Trainer 实例（在初始化时设置早停参数和模型保存参数）
    print("\n创建 Trainer...")
    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        early_stopping=True,  # 在初始化时启用早停
        patience=5,  # 连续5个epoch没有改善则停止
        monitor='val_loss',  # 监控验证损失
        min_delta=0.001,  # 最小改善幅度
        restore_best_weights=True,  # 恢复最佳模型权重
        save_best_model=True,  # 保存最佳模型
        save_every_epoch=True,  # 每个epoch都保存模型
    )
    
    # 6. 训练模型（使用初始化时设置的早停参数）
    print("\n开始训练...")
    num_epochs = 111  # 设置最大训练轮数
    trainer.train_classification(num_epochs=num_epochs)  # 早停参数已在初始化时设置，这里可以省略
    
    # 7. 评估模型
    print("\n评估模型...")
    val_loss, val_acc = trainer.evaluating_classification()
    print(f"最终验证结果 - 损失: {val_loss:.4f}, 准确率: {val_acc:.4f}")
    
    # 8. 绘制训练历史曲线
    print("\n绘制训练历史曲线...")
    trainer.plot_history()
    
    print("\n" + "=" * 60)
    print("测试完成！")
    print("=" * 60)


def test_regression():
    """
    使用随机生成的简单数据测试 Trainer 类回归任务
    """
    print("=" * 60)
    print("Trainer 类回归任务测试示例")
    print("=" * 60)
    
    # 1. 创建一个简单的回归神经网络模型
    class SimpleRegressor(nn.Module):
        def __init__(self, input_size=10, hidden_size=64, output_size=1):
            super().__init__()
            self.fc1 = nn.Linear(input_size, hidden_size)
            self.relu = nn.ReLU()
            self.fc2 = nn.Linear(hidden_size, hidden_size // 2)
            self.relu2 = nn.ReLU()
            self.fc3 = nn.Linear(hidden_size // 2, output_size)
        
        def forward(self, x):
            x = self.fc1(x)
            x = self.relu(x)
            x = self.fc2(x)
            x = self.relu2(x)
            x = self.fc3(x)
            return x
    
    # 2. 生成随机训练数据
    print("\n生成随机数据...")
    num_train_samples = 200
    num_val_samples = 50
    input_size = 10  # 输入特征维度
    output_size = 1  # 输出维度（回归任务通常是1）
    
    # 生成随机特征数据
    torch.manual_seed(42)  # 设置随机种子以便复现
    train_features = torch.randn(num_train_samples, input_size)
    # 生成目标值：使用简单的线性关系加上一些噪声
    train_targets = (train_features.sum(dim=1, keepdim=True) * 0.5 + 
                     torch.randn(num_train_samples, output_size) * 0.1)
    
    val_features = torch.randn(num_val_samples, input_size)
    val_targets = (val_features.sum(dim=1, keepdim=True) * 0.5 + 
                   torch.randn(num_val_samples, output_size) * 0.1)
    
    print(f"训练集: {num_train_samples} 个样本")
    print(f"验证集: {num_val_samples} 个样本")
    print(f"输入特征维度: {input_size}")
    print(f"输出维度: {output_size}")
    
    # 3. 创建数据加载器
    from torch.utils.data import TensorDataset, DataLoader
    
    train_dataset = TensorDataset(train_features, train_targets)
    val_dataset = TensorDataset(val_features, val_targets)
    
    batch_size = 32
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    
    print(f"批次大小: {batch_size}")
    print(f"训练批次数: {len(train_loader)}")
    print(f"验证批次数: {len(val_loader)}")
    
    # 4. 创建模型实例
    print("\n创建模型...")
    model = SimpleRegressor(input_size=input_size, hidden_size=64, output_size=output_size)
    
    # 计算模型参数数量
    total_params = sum(p.numel() for p in model.parameters())
    print(f"模型参数总数: {total_params:,}")
    
    # 5. 创建损失函数（回归任务使用MSE）
    criterion = nn.MSELoss()
    
    # 6. 创建 Trainer 实例（在初始化时设置早停参数和模型保存参数）
    print("\n创建 Trainer...")
    trainer = Trainer(
        model=model,
        criterion=criterion,  # 使用MSE损失
        train_loader=train_loader,
        val_loader=val_loader,
        early_stopping=True,  # 在初始化时启用早停
        patience=5,  # 连续5个epoch没有改善则停止
        monitor='val_loss',  # 监控验证损失
        min_delta=0.001,  # 最小改善幅度
        restore_best_weights=True,  # 恢复最佳模型权重
        save_best_model=True,  # 保存最佳模型
        save_every_epoch=True,  # 每个epoch都保存模型
    )
    
    # 7. 训练模型（使用初始化时设置的早停参数）
    print("\n开始训练...")
    num_epochs = 50  # 设置最大训练轮数
    trainer.train_regression(num_epochs=num_epochs)  # 使用回归训练方法
    
    # 8. 评估模型
    print("\n评估模型...")
    val_loss = trainer.evaluating_regression()
    print(f"最终验证结果 - 损失: {val_loss:.4f}")
    
    # 9. 绘制训练历史曲线（只绘制损失，不绘制准确率）
    print("\n绘制训练历史曲线...")
    trainer.plot_history(plot_loss=True, plot_acc=False)
    
    print("\n" + "=" * 60)
    print("测试完成！")
    print("=" * 60)


def test_binary_classification():
    """
    使用随机生成的简单数据测试 Trainer 类二分类任务
    """
    print("=" * 60)
    print("Trainer 类二分类任务测试示例")
    print("=" * 60)
    
    # 1. 创建一个简单的二分类神经网络模型（输出单个logit）
    class SimpleBinaryModel(nn.Module):
        def __init__(self, input_size=20, hidden_size=32):
            super().__init__()
            self.fc1 = nn.Linear(input_size, hidden_size)
            self.relu = nn.ReLU()
            self.fc2 = nn.Linear(hidden_size, 1)  # 输出1维logit
        
        def forward(self, x):
            x = self.fc1(x)
            x = self.relu(x)
            x = self.fc2(x)  # 不做sigmoid，由损失函数和评估函数内部处理
            return x
    
    # 2. 生成随机训练数据
    print("\n生成随机数据（二分类）...")
    torch.manual_seed(123)
    num_train_samples = 200
    num_val_samples = 80
    input_size = 20
    
    # 构造一个简单的线性可分任务：根据特征和的正负决定标签，再加一点噪声
    train_features = torch.randn(num_train_samples, input_size)
    train_scores = train_features.sum(dim=1) + 0.5 * torch.randn(num_train_samples)
    train_labels = (train_scores > 0).long()  # 0 / 1
    
    val_features = torch.randn(num_val_samples, input_size)
    val_scores = val_features.sum(dim=1) + 0.5 * torch.randn(num_val_samples)
    val_labels = (val_scores > 0).long()
    
    print(f"训练集: {num_train_samples} 个样本")
    print(f"验证集: {num_val_samples} 个样本")
    
    # 3. 创建数据加载器
    from torch.utils.data import TensorDataset, DataLoader
    
    train_dataset = TensorDataset(train_features, train_labels)
    val_dataset = TensorDataset(val_features, val_labels)
    
    batch_size = 32
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    
    print(f"批次大小: {batch_size}")
    print(f"训练批次数: {len(train_loader)}")
    print(f"验证批次数: {len(val_loader)}")
    
    # 4. 创建模型实例
    print("\n创建模型...")
    model = SimpleBinaryModel(input_size=input_size, hidden_size=32)
    
    # 计算模型参数数量
    total_params = sum(p.numel() for p in model.parameters())
    print(f"模型参数总数: {total_params:,}")
    
    # 5. 创建损失函数（二分类使用BCEWithLogitsLoss）
    criterion = nn.BCEWithLogitsLoss()
    
    # 6. 创建 Trainer 实例
    print("\n创建 Trainer...")
    trainer = Trainer(
        model=model,
        criterion=criterion,  # 使用BCEWithLogitsLoss
        train_loader=train_loader,
        val_loader=val_loader,
        early_stopping=True,
        patience=5,
        monitor='val_loss',   # 可以改为 'val_acc' 监控准确率
        min_delta=0.001,
        restore_best_weights=True,
        save_best_model=True,
        save_every_epoch=False,
    )
    
    # 7. 训练模型
    print("\n开始训练（二分类）...")
    num_epochs = 50
    trainer.train_binary_classification(num_epochs=num_epochs)
    
    # 8. 评估模型
    print("\n评估模型（二分类）...")
    val_loss, val_acc = trainer.evaluating_binary_classification()
    print(f"最终验证结果（二分类） - 损失: {val_loss:.4f}, 准确率: {val_acc:.4f}")
    
    # 9. 绘制训练历史曲线
    print("\n绘制训练历史曲线（二分类）...")
    trainer.plot_history()
    
    print("\n" + "=" * 60)
    print("二分类测试完成！")
    print("=" * 60)


if __name__ == '__main__':
    # test_classification()  # 测试分类任务
    # test_regression()  # 测试回归任务（取消注释以运行）
    test_binary_classification()  # 测试二分类任务（取消注释以运行）
    