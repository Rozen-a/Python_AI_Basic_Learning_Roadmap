import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt


class Trainer:
    """模型训练器类，包含训练、评估和画图功能"""
    
    def __init__(self, model, criterion=None, optimizer=None, device=None):
        """
        初始化训练器
        
        Args:
            model: 要训练的模型
            criterion: 损失函数，默认为CrossEntropyLoss
            optimizer: 优化器，默认为SGD
            device: 设备（cuda/cpu），默认自动选择
        """
        self.model = model
        self.criterion = criterion if criterion is not None else nn.CrossEntropyLoss()
        self.device = device if device is not None else torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        
        # 如果未提供优化器，使用默认的SGD优化器
        if optimizer is None:
            self.optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
        else:
            self.optimizer = optimizer
        
        # 用于存储训练历史
        self.train_losses = []
        self.val_losses = []
        self.val_accuracies = []
    
    def evaluating(self, dataloader):
        """
        评估函数，计算模型在数据集上的平均损失和准确率
        
        Args:
            dataloader: 数据加载器
            
        Returns:
            avg_loss: 平均损失
            avg_acc: 准确率
        """
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
        return avg_loss, avg_acc    # 返回平均损失和准确率
    
    def train(self, train_loader, val_loader, num_epochs, verbose=True):
        """
        训练模型
        
        Args:
            train_loader: 训练数据加载器
            val_loader: 验证数据加载器
            num_epochs: 训练轮数
            verbose: 是否打印训练信息，默认为True
        """
        # 清空历史记录
        self.train_losses = []
        self.val_losses = []
        self.val_accuracies = []
        
        # 模型训练
        for epoch in range(num_epochs):
            self.model.train()  # 设置为训练模式
            running_loss = 0.0
            
            for images, labels in train_loader:
                images, labels = images.to(self.device), labels.to(self.device)

                self.optimizer.zero_grad()           # 梯度清零
                outputs = self.model(images)         # 前向传播
                loss = self.criterion(outputs, labels)  # 计算损失
                loss.backward()                 # 反向传播
                self.optimizer.step()                # 更新参数

                running_loss += loss.item() * labels.size(0)  # 将每个batch的损失乘以batch大小后累加到total running_loss

            train_loss = running_loss / len(train_loader.dataset)  # 计算整个训练集的平均损失
            val_loss, val_acc = self.evaluating(val_loader)  # 用验证集评估模型，获得平均损失与准确率

            self.train_losses.append(train_loss)
            self.val_losses.append(val_loss)
            self.val_accuracies.append(val_acc)

            if verbose:
                print(f"Epoch [{epoch+1}/{num_epochs}], "
                      f"Train Loss: {train_loss:.4f}, "
                      f"Val Loss: {val_loss:.4f}, "
                      f"Val Acc: {val_acc:.4f}")
    
    def plot_history(self, figsize=(10, 5)):
        """
        绘制训练历史曲线（损失和准确率）
        
        Args:
            figsize: 图像大小，默认为(10, 5)
        """
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
        plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
        
        if not self.train_losses:
            print("警告：没有训练历史数据，请先调用train方法进行训练")
            return
        
        epochs = range(1, len(self.train_losses) + 1)

        # 损失曲线
        plt.figure(figsize=figsize)
        plt.plot(epochs, self.train_losses, 'o-', label='训练损失')
        plt.plot(epochs, self.val_losses, 's-', label='验证损失')
        plt.xlabel('轮数')
        plt.ylabel('损失')
        plt.title('训练与验证损失')
        plt.legend()
        plt.show()

        # 准确率曲线
        plt.figure(figsize=figsize)
        plt.plot(epochs, self.val_accuracies, 'd-', label='验证准确率')
        plt.xlabel('轮数')
        plt.ylabel('准确率')
        plt.title('验证集准确率')
        plt.legend()
        plt.show()

