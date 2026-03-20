## Python AI Basic Learning Roadmap

个人 Python / 数据分析 / 机器学习 学习代码与笔记仓库

### 项目简介

- **学习目标**：从 Python 语法基础，一路过渡到数据分析与机器学习的完整知识体系。
- **配套内容**：每日配套 `DayX` 代码练习 + 三份系统化 Markdown 笔记，便于回顾与查阅。
- **适合人群**：有一定编程基础，想系统入门 Python 数据分析 / 机器学习的同学。

### 目录

- **项目结构**（各目录与笔记文件说明）
- **学习路径概览**（按 Day 梳理知识点）
- **其他笔记与补充内容**

### 目录结构总览

```text
WangDao_PythonAI/
├── Day2/                    # Python 基础语法
├── Day3/                    # 数据结构基础
├── Day4/                    # 函数与进阶语法
├── Day5/                    # 面向对象编程
├── Day6/                    # 类方法、异常、模块与文件
├── Day7/                    # 正则表达式、排序、二叉树
├── Day8/                    # Matplotlib 数据可视化
├── Day9/                    # Numpy & Pandas 入门
├── Day10/                   # Pandas 进阶与特征工程
├── Day11/                   # sklearn 数值预处理 / 特征选择 / 降维
├── Day12/                   # KNN、超参数搜索、分类评估
├── Day13/                   # 正则化回归、逻辑回归与优化
├── Day14/                   # 神经网络与分类实战
├── Day15/                   # 深度学习进阶与训练技巧
├── Day16/                   # 深度学习拓展：回归/超参搜索、Embedding/Pooling、RNN
├── Day17/                   # RNN 进阶与文本生成
├── Day18/                   # LSTM、双向与多层 RNN、子词级建模 (BPE)
├── Project1_Seq2Seq-Translation-en-ja/ # 英日翻译 Seq2Seq 项目实战
├── Project2_Transformer/              # 德英翻译 Transformer 项目实战
├── 系统学习笔记/              # 系统学习的 Markdown 笔记
│   ├── 1-Python基础笔记.md   # Day2–Day7 Python 基础与进阶总结
│   ├── 2-数据分析笔记.md      # Day8–Day10 Numpy / Pandas / Matplotlib
│   ├── 3-机器学习笔记.md      # Day10–Day13 上：特征工程 / KNN / 回归与正则化 / 逻辑回归
│   ├── 4-深度学习.md         # Day13 下–Day18：PyTorch / 神经网络 / 初始化 / BN & Dropout / EarlyStopping / RNN / Embedding / 超参搜索 / LSTM / BPE / 实战
│   ├── 5-自然语言处理.md      # Seq2Seq / Attention / Masking / BLEU / Transformer / ResNet / LN / 调参工程化 / Linux 命令
│   └── imgs/                 # 笔记图片存储
├── 零散笔记/                 # 若干补充知识点
│   ├── fit() 和 transform().md
│   ├── wc 命令.md
│   ├── 为什么标准化后均值为 0、标准差为 1.md
│   └── 逻辑回归为什么使用 Sigmoid 函数.md
└── README.md
```

### 学习路径概览（按阶段）

---

#### 阶段一：Python 基础（Day2–Day7）

> 目标：打牢 Python 语法与数据结构基础，熟悉函数与面向对象编程。

**Day2 - Python 基础入门**

- **基础语法**：变量、输入输出、表达式与运算符（算术 / 比较 / 逻辑）
- **控制流**：if-elif-else、while / for 循环、range、三目运算符
- **字符串插值**：f-string、`str.format()`、`%` 格式化

**Day3 - 数据结构基础**
- **字符串**：切片、判断方法、查找与替换、大小写与对齐、split/join 等
- **列表 / 元组 / 字典 / 集合**：常用增删改查、遍历、内置方法与特性
- **公共工具**：`len` / `max` / `min` / `sorted` / `enumerate`
- **推导式**：列表 / 字典 / 集合推导式

**Day4 - 函数与进阶语法**
- **函数**：定义与调用、返回值与拆包、高阶函数、匿名函数 `lambda`
- **参数系统**：位置 / 关键字 / 缺省 / `*args` / `**kwargs`
- **作用域与引用**：全局变量、`global`、引用传递、浅拷贝 / 深拷贝
- **面向对象入门**：`__init__` / `__str__` / `__del__` 等内置方法

**Day5 - 面向对象编程**
- **注解与类型提示**：方法参数类型标注
- **封装与访问控制**：公开属性、受保护 `_attr`、私有 `__attr`
- **继承与多重继承**：MRO、菱形继承、`super()` 调用父类方法
- **多态与抽象类**：`ABC`、`@abstractmethod`、抽象属性 `@property`

**Day6 - 高级特性与异常 / 文件 / 模块**
- **类属性 / 类方法 / 静态方法**：`cls` vs `self`
- **单例模式**：重写 `__new__` 实现全局唯一对象
- **异常处理**：`try/except/else/finally`、异常传递、`raise`、断言 `assert`
- **文件与目录操作**：`open`/`with`、文本与二进制读写、`os` 常用 API
- **模块与包**：导入方式、`__name__ == "__main__"`、包结构与 `__init__.py`
- **深浅拷贝**：`copy` / `deepcopy`、可变与不可变对象行为差异

**Day7 - 正则表达式、迭代器与二叉树**
- **正则基础**：字符匹配、数量词、边界与分组、贪婪 / 非贪婪
- **`re` 模块**：`match` / `search` / `findall` / `sub` / `split` / `compile`
- **生成器与迭代器**：`yield`、`iter`、`Iterator` vs `Iterable`
- **排序与内置函数**：`sorted` 与 `sort`、`key` / 多条件排序、`__repr__`
- **二叉树实现**：面向对象实现二叉树及前中后序、层序遍历

---

#### 阶段二：数据分析与可视化（Day8–Day10）

> 目标：掌握 Matplotlib / Numpy / Pandas 的核心用法，能完成基础数据分析与可视化。

**Day8 - Matplotlib 数据可视化**

- **Jupyter 快捷键** 与 Notebook 使用
- **基础绘图**：折线图、设置颜色 / 线型 / 标记、画布大小与保存 (`figure` / `savefig`)
- **坐标轴控制**：刻度与标签、中文字体与负号显示、网格、图例
- **多图布局**：一图多线、`subplots` / `subplot` 多子图
- **常用图形**：散点图、柱状图、直方图、饼图

**Day9 - Numpy 与 Pandas 入门**
- **Numpy 核心**：`ndarray` 创建（数组 / 随机数）、`shape`/`ndim`/`dtype`/`size`
- **数组操作**：`reshape`、`astype`、切片与索引、布尔索引、广播机制
- **统计函数**：`sum` / `mean` / `max` / `min` / `cumsum` / `argmin` / `std` / `ptp`
- **数组增删改查**：`append` / `insert` / `delete` / `unique` / `concatenate` / `stack` / `split`
- **缺失值与特殊值**：`nan` / `inf` 处理、`isnan`、`count_nonzero`
- **Pandas 核心结构**：`Series` 与 `DataFrame` 的创建、索引、基础增删查改

**Day10（上）- Pandas 进阶（数据分析视角）**
- **Pandas 函数应用**：`apply` / `map` / `agg` / `transform`
- **描述性统计**：`describe`、`mean` / `median` / `std` 等及 `include` 用法
- **分组聚合**：`groupby`、分组统计、`rank` 排名
- **数据清洗**：重复值检测与删除、缺失值检测 / 删除 / 填充 (`dropna` / `fillna`)

---

#### 阶段三：机器学习与模型优化（Day10 下–Day13 上）

> 目标：掌握 sklearn 中的预处理、特征工程、典型分类 / 回归算法与评估方法。

**Day10（下）- 特征工程与编码**
- **独热编码与特征表示**：One-Hot 编码思想、字典特征提取 `DictVectorizer`
- **文本特征工程**：`CountVectorizer` / `TfidfVectorizer`，英文与中文（结合 `jieba` 分词）文本特征抽取

**Day11 - sklearn 数值预处理 / 特征工程**
- **数值预处理**：归一化 `MinMaxScaler`、标准化 `StandardScaler`
- **缺失值填充**：`SimpleImputer`（均值 / 中位数 / 众数 / 常量）
- **特征选择**：`VarianceThreshold` 方差筛选、过滤 / 嵌入 / 包裹法概念
- **降维**：PCA 理论（方差 / 主成分）、`PCA` API 与方差解释率
- **分类 vs 回归**：任务定义与常见算法、评估指标差异

**Day12 - KNN、交叉验证与模型评估**
- **KNN 算法**：分类与回归流程、距离度量（欧式 / 曼哈顿）、优缺点与适用场景
- **FB Location 实战**：特征工程（时间特征、位置过滤）、标准化、KNN 建模与评估
- **超参数搜索**：交叉验证 `cv`、`GridSearchCV` 网格搜索调参
- **分类评估指标**：混淆矩阵、准确率、精确率 / 召回率、F1、ROC & AUC

**Day13（上）- 回归、正则化与逻辑回归**
- **线性回归**：损失函数（MSE）、正规方程与梯度下降（FGD / SGD / Mini-batch）
- **回归评估**：MSE / RMSE / MAE、过拟合与欠拟合及常见解决方案
- **正则化回归**：L1（Lasso）与 L2（Ridge）正则化思想与 sklearn API
- **逻辑回归**：Sigmoid 函数、二分类概率解释、交叉熵损失、`LogisticRegression`
- **优化与梯度**：学习率、数值求导 / 梯度检查、SGD 相关变体概念

---

#### 阶段四：深度学习入门（Day13 下–Day18）

> 目标：完成从传统机器学习到深度学习的过渡，掌握 PyTorch 基础与训练流程。

**Day13（下）- 深度学习与 PyTorch 入门**
- **PyTorch 张量基础**：张量创建 / 类型转换 / 数值运算与索引 / 形状变换与拼接
- **自动微分与计算图**：`autograd` 机制、`backward()`、参数梯度 `grad`
- **训练通用套路**：定义网络 / 损失函数 / 优化器，前向传播、反向传播与参数更新
- **数据集与数据加载**：自定义 `Dataset`、使用 `DataLoader` 批量加载和打乱数据

**Day14 - 神经网络与分类实战**
- **人工神经网络（ANN）**：网络结构（输入层 / 隐藏层 / 输出层）、前向传播与反向传播
- **激活函数**：Sigmoid / Tanh / ReLU / SoftMax 的特性、导数与选择策略
- **损失函数对比**：交叉熵损失 vs 均方误差损失，分类任务中的优势
- **数据集划分**：训练集 / 验证集 / 测试集的作用与划分原则
- **全连接层**：`nn.Linear()` 原理、`nn.Flatten()` 处理高维数据
- **Fashion-MNIST 实战**：完整分类流程（数据加载 / 模型搭建 / 训练评估 / 可视化）

**Day15 - 深度学习进阶与训练技巧**
- **权重初始化**：均匀 / 正态分布，对比 Xavier 与 Kaiming 初始化及与激活函数的匹配
- **图像预处理**：`ToTensor` 与 `Normalize` 实现图像归一化与标准化
- **训练过程控制**：早停（Early Stopping）参数含义、典型使用流程
- **模型保存与可视化**：`torch.save` / `torch.load`、TensorBoard 日志记录与曲线查看
- **网络结构与正则化**：使用 `nn.Sequential` 构建 DNN，结合 BatchNorm、Dropout / AlphaDropout 缓解过拟合与梯度问题
- **Fashion-MNIST DNN 系列实战**：多种训练脚本，对比标准化、早停、BN、SELU、AlphaDropout 等配置效果

**Day16 - 深度学习拓展与 NLP 入门**
- **超参数搜索**：Grid / Random / 遗传算法 / AutoML 思路；学习率与 Batch Size 影响
- **RNN 基础**：循环结构、隐藏状态、时间展开与计算公式
- **Embedding 与文本处理**：Word2Vec vs Embedding；序列的 embedding / padding / pooling
- **二分类方案**：BCE vs Softmax 二分类
- **DataLoader 高级**：`collate_fn`、`zip(*batch)`、`functools.partial` 的用法
- **数据集缓存**：sklearn `data_home` 参数与本地缓存目录

**Day17 - RNN 进阶与文本生成**
- **RNN 接口**：`nn.RNN` 参数（`input_size`, `hidden_size`, `num_layers`, `batch_first`）、输入输出形状
- **双向 RNN**：`bidirectional=True`、前向/后向状态拼接、输出维度变化
- **文本表示粒度**：Char-level vs Word-level vs Subword-level
- **文本生成**：基于 RNN 的 Char-level 文本生成流程

**Day18 - LSTM、多层/双向 RNN 与子词级建模**
- **文本生成优化**：`Temperature` 与 `Multinomial` 机制
- **LSTM (长短期记忆网络)**：遗忘门、输入门、输出门、细胞状态，解决长距离依赖问题
- **RNN 变体总结**：对比单层/多层、单向/双向 RNN 的结构与数据形状
- **子词级建模 (BPE)**：OOV 问题、BPE 算法原理、`subword-nmt` 工具实战、`@@` 粘合剂

---

#### 阶段五：自然语言处理项目实战

> 目标：通过 Seq2Seq 与 Transformer 项目实战，深入理解编码器-解码器架构、注意力机制、序列建模以及并行计算优势。

**Project1 - Seq2Seq 英日翻译项目**

- **核心架构**：Seq2Seq (Encoder-Decoder)、GRU 模型应用、日语分词工具 `Janome`
- **注意力机制**：Bahdanau 注意力原理、计算步骤 (Score / Softmax / Weighted Sum)
- **训练优化**：填充掩码 (Padding Mask)、因果掩码 (Causal Mask)、带掩码的交叉熵损失函数
- **模型评估与指标**：BLEU 算法原理 (n-gram Precision / BP / Clipping)、测试集平均 **BLEU-1: 56.91%**, **BLEU-4: 21.27%**
- **推理与可视化**：自回归生成、注意力热力图 (Heatmap) 可解释性分析
- **实战对比与分析**：对比 Sutskever (2014) 原始论文架构，分析注意力机制对参数量与长程依赖的影响，探讨集束搜索与贪心搜索的性能差异
- **Python 进阶**：`@property` 装饰器、`random.choice` 与 `np.random.choice` 差异

**Project2 - Transformer 德英翻译项目**

- **核心架构**：Transformer (Encoder-Decoder)、多头注意力 (Multi-Head Attention)、位置编码 (Positional Encoding)
- **核心组件**：残差连接 (ResNet) 解决深层训练难题、层归一化 (LayerNorm) 稳定数据分布
- **数据工程**：Moses Tokenization 数据清洗、BPE (Byte Pair Encoding) 子词建模、动态批处理 (Token Batching)
- **模型优化**：标签平滑 (Label Smoothing)、Noam 学习率调度器、验证集最佳检查点自动保存
- **评估与监控**：BLEU-4 定量评估（截断匹配与短句惩罚）、TensorBoard 实时曲线记录、Multi-Head Attention 权重热力图可视化
- **工程实践**：Python `argparse` 参数解析、Shell 脚本自动化流水线、Linux `touch/cat` 核心命令应用
- **实战意义**：深入理解并行计算优势，掌握现代大模型 (LLM) 的基石架构。

---

### 其他笔记与零散内容
- **fit() 和 transform().md**：解释 `fit()` 和 `transform()` 的区别与使用场景
- **wc 命令.md**：Linux `wc` 命令详解，用于统计文件行数、单词数、字节数等
- **为什么标准化后均值为 0、标准差为 1.md**：说明标准化后的统计性质及原因
- **逻辑回归为什么使用 Sigmoid 函数.md**：从线性函数 / 阶跃函数对比到对数几率模型，系统解释 Sigmoid 在逻辑回归中的作用

