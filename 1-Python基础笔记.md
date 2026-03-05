

# Python基础笔记

[TOC]



## <span style='color:red'>Day2</span>

### 1. 现字符串插值的方式

| **方法**                              | **基本语法**                                                 | **主要优点**                                     |
| :------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------ |
| **f**-**string** (格式化字符串字面值) | `f"Hello, {name}"`                                           | 语法简洁直观，**执行效率高**，支持内嵌复杂表达式 |
| **str.format()** 方法                 | `"Hello, {}".format(name)`<br>` "Hello,{name}".format(name=name)` | 功能灵活强大，兼容性较好，支持位置和关键字参数   |
| **%** **格式化** (旧式格式化)         | `"Hello, %s" % name`                                         | 语法简单，兼容所有 Python 版本                   |



### 2. 除法

除法：左操作数除以右操作数，得到商  a/b=0.5

取整除：返回商的整数部分   a//b=0

### 3. 在Python中，没有 ++ 和 -- 

### 4. 三目运算符

``` python
表达式1 if 条件表达式 else 表达式
```

当条件表达式为True时，结果表达式1，否则结果是表达式2。

### 5. if

``` python
if 判断条件1:
判断条件1成立时执行的代码
判断条件1成立时执行的代码
...
elif 判断条件2:
判断条件1不成立,判断条件2成立时会执行的代码
判断条件1不成立,判断条件2成立时会执行的代码
...
else:
判断条件1和判断条件2都不成立,执行的代码
判断条件1和判断条件2都不成立,执行的代码
...
```

> 注意事项:
> 1. elif不要分开写，不要写成了 else if
> 2. 当判断条件1成立，判断条件2也成立时，会执行判断条件1控制的代码，不会执行判断条
> 件2执行的代码
> 3. 多分支的结构，执行也永远只会执行其中的一个分支
> 4. else后面不能再加分支了，else必须放在最后面

### 6. range函数

`range(起始值，结束值，步长) `

 起始值默认为0，步长默认为1，不包含结束值（**左闭右开**）

### 7. while / for + else

``` python
while循环或者是for循环:
循环体
else:
语句...
```

> 语法解释:
>
> 1. 只要循环不是正常退出的，就一定会执行else中的内容
> 2. 循环正常退出，是指以非break的方式跳出
> 3. 大白话：只要循环不是以break形式跳出，那么就一定会执行else中的内容

## <span style='color:red'>Day3</span>

### 1. 切片：左闭右开

### 2. 字符串常用操作方法

#### 判断类型

``` python
# 如果 string 中只包含空格，则返回True
def isspace()

# 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True
def isalnum()

# 如果 string 至少有一个字符并且所有字符都是字母则返回 True
def isalpha()

# 如果 string 只包含数字则返回 True，包含Unicode数字，，全角数字（双字节）
def isdecimal()

# 如果 string 只包含数字则返回 True，包含Unicode数字，byte数字（单字节），全角数字（双字节）
def isdigit()

# 如果 string 只包含数字则返回 True，包含Unicode 数字，全角数字（双字节），汉字数字
def isnumeric()

# 如果 string 是标题化的(每个单词的首字母大写)则返回 True
def istitle()

# 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True
def islower()

# 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True
def isupper()
```

#### 查找与替换

```python
# 检查字符串是否是以 str 开头，是则返回 True
def startswith(str)

# 检查字符串是否是以 str 结束，是则返回 True
def endswith(str)

# 检测 str 是否包含在 string 中，如果start 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
# 与index区别,只能用位置参数，不能用keyword
def find(str,start=0,end=len(str))

# 类似于 find()，不过是从右边开始查找
def rfind(str,start=0,end=len(str))

# 跟 find() 方法类似，不过如果 str 不在 string 会报错
def index(str,start=0,end=len(str))

# 类似于 index()，不过是从右边开始
def rindex(str,start=0,end=len(str))

# 把 string 中的 old_str 替换成new_str，如果 num 指定，则替换不超过 num次
def replace(old_str, new_str, num=string.count(old))
```

#### 大小写转换

``` python
# 把字符串的第一个字符大写
def capitalize()

# 把字符串的每个单词首字母大写
def title()

# 转换 string 中所有大写字符为小写
def lower()

# 转换 string 中的小写字母为大写
def upper()

# 翻转 string 中的大小写
def swapcase()
```

#### 其他功能

``` python
# 返回一个原字符串左对齐，并使用空格填充至长度 width 的新字符串
def ljust(width)

# 返回一个原字符串右对齐，并使用空格填充至长度 width 的新字符串
def rjust(width)

# 返回一个原字符串居中，并使用空格填充至长度 width 的新字符串
def center(width)

# 截掉 string 左边（开始）的空白字符,可以去除字符 char
def lstrip(char)

# 截掉 string 右边（末尾）的空白字符，可以去除字符 char
def rstrip(char)

# 截掉 string 左右两边的空白字符，可以去除字符 char
def strip(char)

# 把字符串 string 分成一个 3 元素的元组 (str 前面, str, str 后面)
def partition(str)

# 类似于 partition() 方法，不过是从右边开始查找
def rpartition(str)

# 以 str 为分隔符拆分 string，如果num 有指定值，则仅分隔 num + 1个子字符串，str 默认包含空格
def split(str="", num)

# splitlines 只是换行，每行字符串的内容不做修改
def splitlines()

# 用字符串将可迭代对象中的元素连接起来, seq为可迭代的对象，比如','.join(['a','b','c']) -> 'a,b,c'
def join(seq)
```

### 3. 列表常用操作方法

增加: `append()`、 `extend()`、 `insert()`

删除: `del`、 `remove()`、`pop()`、 `clear()`

查询: `index()`、 `count()`、`in`、 `not in`

修改: `列表[索引] = 修改后的值`、 `reverse()`、 `sort()`

> ==index(元素值, 起始位置, 结束位置 )==: 从列表中找出某个值第一个匹配项的索引位置
>
> 注意事项：
>
> 1. 元素必须在列表中，否则会报错
> 2. 起始位置和结束位置这两个参数可以省略，默认查询整个列表

![image-20260209140542878](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260209140543101.png)

### 4. 元组

**元组不可修改**

![image-20260209142907483](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260209142907555.png)

### 5. 字典

**基本语法：`字典名 = {键1:值1, 键2: 值2, 键3: 值3, ...}`**

**键**key是索引，必须是**不可变类型**，往往是字符串

**值**可以取任何数据类型，但**键**只能使用**字符串**、数字或元组

| 序号 | 函数                            | 描述                                                         |
| :--- | :------------------------------ | :----------------------------------------------------------- |
| 1    | `dict.clear()`                  | 删除字典内所有元素                                           |
| 2    | `dict.copy()`                   | 返回一个字典的浅复制                                         |
| 3    | `dict.fromkeys(seq, val)`       | 创建一个新字典，以序列 `seq` 中元素做字典的键，`val` 为所有键对应的初始值 |
| 4    | `dict.get(key, default)`        | 返回指定键的值，如果键不在字典中则返回 `default` 设置的默认值 |
| 5    | `key in dict`                   | 如果键在字典里返回 `True`，否则返回 `False`                  |
| 6    | `dict.items()`                  | 返回一个包含所有键值对的视图对象（可迭代）                   |
| 7    | `dict.keys()`                   | 返回一个包含所有键的视图对象（可迭代）                       |
| 8    | `dict.setdefault(key, default)` | 如果键存在则返回值，否则插入键并设置值为 `default`           |
| 9    | `dict.update(dict2)`            | 将字典 `dict2` 的键值对更新到当前字典中                      |
| 10   | `dict.values()`                 | 返回一个包含所有值的视图对象（可迭代）                       |
| 11   | `dict.pop(key)`                 | 删除并返回指定键对应的值                                     |
| 12   | `dict.popitem()`                | 删除并返回字典中的一个键值对（在 Python 3.7+ 中为后进先出）  |

> default 默认为 None

![image-20260215001548495](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215001548727.png)

**字典的特征：**

**可变容器**：字典中的数据是可变的，和列表一样，是可变容器，而元组是不可变容

器

**键的唯一性**：字典中的键必须是唯一的，如果同一个键被赋值多次，那么后面的值

会把前面的值覆盖

**键的类型限制**：字典使用哈希表存储，字典的键必须是可哈希的，也就是必须是不

可变类型，一般建议设置为字符串类型



### 6. 除了变量名，函数名也可以被del()删除

### 7. 集合

> 集合主要是用来去重。
>
> 集合的定义
>
> - 创建空集合 `my_set = set()`
>
> - 创建有元素的集合 `my_set = {元素1, 元素2, 元素3 ...}`
>
> - 通过序列创建集合(这一步会去重) `my_set = set(序列名)`

| 编号 | 方法                            | 描述                                           |
| :--- | :------------------------------ | :--------------------------------------------- |
| 1    | `add()`                         | 为集合添加元素                                 |
| 2    | `clear()`                       | 移除集合中的所有元素                           |
| 3    | `copy()`                        | 拷贝一个集合                                   |
| 4    | `difference()`                  | 返回多个集合的差集                             |
| 5    | `difference_update()`           | 移除集合中那些同时存在于指定集合中的元素       |
| 6    | `discard()`                     | 删除集合中指定的元素（如果元素不存在，不报错） |
| 7    | `intersection()`                | 返回集合的交集                                 |
| 8    | `intersection_update()`         | 用交集更新原集合                               |
| 9    | `isdisjoint()`                  | 判断两个集合是否没有交集，无则返回 `True`      |
| 10   | `issuperset()`                  | 判断当前集合是否为另一个集合的超集             |
| 11   | `pop()`                         | 随机移除并返回一个元素                         |
| 12   | `remove()`                      | 移除指定元素（若不存在则报错）                 |
| 13   | `symmetric_difference()`        | 返回两个集合的对称差集                         |
| 14   | `symmetric_difference_update()` | 用对称差集更新原集合                           |
| 15   | `union()`                       | 返回两个集合的并集                             |
| 16   | `update()`                      | 用并集更新原集合                               |
| 17   | `len()`                         | 计算集合元素个数（内置函数，非集合方法）       |

> 集合还支持特定的运算符来求交集、并集和差集
>
> - &：交集
>
> - -：差集
>
> - |：并集

```python
# 求交集、并集和差集
set1 = {1,2,3,4}
set2 = {3,4,5,6}

# 并集
union_set = set1 | set2
print(union_set) # 输出: {1, 2, 3, 4, 5, 6}

# 差集
diff_set = set1 - set2
print(diff_set) # 输出: {1, 2}

# 交集
inter_set = set1 & set2
print(inter_set) # 输出: {3, 4}
```

### 8. 公共运算符

| 运算符             | 描述                       | 支持的容器类型                 |
| :----------------- | :------------------------- | :----------------------------- |
| `+`                | 合并                       | 字符串、列表、元组             |
| `*`                | 复制                       | 字符串、列表、元组             |
| `in`               | 元素是否存在（字典是键）   | 字符串、列表、元组、字典、集合 |
| `not in`           | 元素是否不存在（字典是键） | 字符串、列表、元组、字典、集合 |
| `[start:end:step]` | 切片（对序列进行截取）     | 字符串、列表、元组             |

| 容器类型    | `==` / `!=`（相等 / 不等）       | `>` / `<` / `>=` / `<=`（大小比较）  |
| :---------- | :------------------------------- | :----------------------------------- |
| 列表 / 元组 | 比较元素、顺序、数量是否完全相同 | 按元素顺序逐个比较，短的前缀容器更小 |
| 集合        | 比较元素是否相同（顺序无关）     | 判断子集/超集关系（一般少用）        |
| 字典        | 比较键值对是否相同（顺序无关）   | **不支持**，会抛出 `TypeError`       |

### 9. 公共方法

| 编号 | 函数          | 字符串 (str) | 列表 (list) | 元组 (tuple) | 字典 (dict) | 集合 (set) | 描述与说明                                                   |
| ---- | ------------- | ------------ | ----------- | ------------ | ----------- | ---------- | ------------------------------------------------------------ |
| 0    | `del`         | ×            | ✓           | ×            | ✓           | ×          | **删除容器中的元素**：从列表、字典等可变容器中移除指定的元素或键值对。 |
| 1    | `len()`       | ✓            | ✓           | ✓            | ✓           | ✓          | **获取长度**。返回容器中元素的数量。                         |
| 2    | `max()`       | ✓            | ✓           | ✓            | ✓           | ✓          | **获取最大值**。返回容器中“最大”的元素。                     |
| 3    | `min()`       | ✓            | ✓           | ✓            | ✓           | ✓          | **获取最小值**。返回容器中“最小”的元素。                     |
| 4    | `sum()`       | ×            | ✓           | ✓            | ×           | ✓          | **求和**。返回容器中所有元素的总和（元素必须是数字类型）。   |
| 5    | `sorted()`    | ✓            | ✓           | ✓            | ✓           | ✓          | **排序**。返回一个新的已排序的列表，不改变原容器。           |
| 6    | `reversed()`  | ✓            | ✓           | ✓            | ✓           | ×          | **反转**。返回一个反转==迭代器==。（想打印迭代器只能通过遍历或使用该迭代器创建一个list用于打印） |
| 7    | `enumerate()` | ✓            | ✓           | ✓            | ✓           | ✓          | **枚举**。返回一个枚举对象，包含索引和值。                   |

``` python
word_list = ['hello', 'today', 'good', 'day']
for index, word in enumerate(word_list):
    print(index, word)
```

运行结果：

![image-20260209164702501](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260209164702561.png)

```python
word_list =['hello','today','good','day']
word_dict = {}
for index，word in enumerate(word_list): # 遍历可选代对象时，每个位置依次给与编号
    word_dict[word]= index
print(word_dict)
```

运行结果：

![image-20260209164836876](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260209164836925.png)

### 10. 推导式

基本语法：

- if 的情况：==[表达式 for 项目 in 可迭代对象 if 条件]==

- if-else的情况==[表达式 if 条件 else 表达式 for 项目 in 可迭代对象 ]==

**常见的推导式类型**

| 推导式类型 | 语法结构                                                   | 描述                           |
| ---------- | ---------------------------------------------------------- | ------------------------------ |
| 列表推导式 | `[expr for item in iterable if condition]`                 | 创建一个新的列表。             |
| 字典推导式 | `{key_expr: value_expr for item in iterable if condition}` | 创建一个新的字典。             |
| 集合推导式 | `{expr for item in iterable if condition}`                 | 创建一个新的集合（自动去重）。 |

## <span style='color:red'>Day4</span>

### 1. 全局变量

如果在函数内要修改全局变量的值，需要使用global关键字声明

不声明直接赋值则会重新创建一个同名局部变量

```python
a = 100

def testA():
	print(a)
    
def testB():
    # global 关键字声明a是全局变量
    # 如果这里没有写global a, 那么 a = 200就相当于是在testB中重新定义了一个局部变量
    global a
    a = 200
    print(a)
    
testA() # 100
testB() # 200
print(f'全局变量a = {a}') # 全局变量a = 200
```

### 2. 函数可以作为 (另一个函数的)参数进行传递

```python
# 定义加法函数
def get_sum(a, b):
	return a + b

# 定义减法函数
def get_substract(a, b):
	return a - b

# 定义计算函数
def calculate(a, b, fn):
    """
    自定义函数, 模拟计算器, 传入什么 函数(对象), 就做什么操作.
    :param a: 要操作的第1个整数
    :param b: 要操作的第2个整数
    :param fn: 具体的操作规则
    :return: 计算结果.
    """
    return fn(a, b)

# 把函数作为calculate的参数进行传递（传递行为）
print(calculate(10, 20, get_sum))
print(calculate(10, 20, get_substract))
```

> 此时被传递函数不加括号，加括号则传递的是函数返回值

### 3. 函数返回值，拆包

可以返回多个结果，默认是元组类型

return返回多个值的时候，单个值的类型没有限制，可以是列表、元组、字典等等

```python
def return_num():
	return 1,2

result = return_num()
print(result) # (1,2)
print(type(result)) # <class 'tuple'>
```

也可以用多个变量接收多个返回值(变量个数必须和返回值个数相同)

```python
def return_num():
	return 1,2

a,b=return_num() # 对元组拆包
print(a) # 1
print(b) # 2
```

**对元组、列表或者字典都可以进行拆包操作**

```python
# 对列表拆包
my_list = [1,3.14,'Cskaoyan',True]
num,pi,name,my_bool=my_list
print(f"num:{my_list}, pi:{pi}, name:{name}, my_bool:{my_bool}")

# 对字典拆包
dict1 = {'name':'李云龙','age':20,'gender':'男'}

# 对字典拆包的时候，获取到的是key值
key1,key2,key3 = dict1
print(f"key1:{key1},key2:{key2},key3:{key3}")
```

### 4. 函数的多种参数

(1)**位置参数**

调用函数时根据函数定义的参数的位置来传递参数

![image-20260210200400563](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260210200400652.png)

（2）**关键字参数**

函数调用时通过“键=值”形式传递参数

作用: 可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求

```python
def print_info(name,age,gender):
    print(f"您的名字是:{name}")
    print(f"您的年龄是:{age}")
    print(f"您的性别是:{gender}")
    
print_info(age=30,gender='女',name='Alice')
print_info('bob',gender='男',age=18)
```

（3）**缺省参数**

缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值

作用: 当调用函数时没有传递参数, 就会使用默认是用缺省参数对应的值

```python
# 缺省参数
def print_info(name,age,gender='男'):
    print(f"您的名字是:{name}")
    print(f"您的年龄是:{age}")
    print(f"您的性别是:{gender}")
    
print_info('Tom',20) # 可以不传缺省参数的值, 使用缺省值
print_info("秀芹",25,'女') # 也可以传缺省参数的值, 使用传入的值
```

> 注意事项：
>
> - 定义缺省参数的时候，所有的位置参数必须在缺省参数之前
>
> - 函数调用时，如果没有为缺省参数传值，那么使用默认值，否则使用传入的值

（4）**不定长参数（多值参数）**

不定长参数：**不定长参数也叫可变参数，即参数的个数是可以变化的。**

Python 中，不定长参数用于处理 “参数数量不确定” 的场景，分为两类：

==*args== ：接收**多个位置参数**，将参数打包为**元组（tuple）**；

==*kwargs== ：接收**多个关键字关键字参数**，将参数打包为**字典（dict）**。

两者的核心区别在于传递方式：

==*args== 处理 “按位置顺序传递的参数”

==*kwargs== 处理 “按 ==键=值== 格式传递的参数”。

```python
def sum_total(*args):
    total = 0
    for i in args:
        total += i
	print(total)
    
sum_total(1, 2, 3, 4, 5) # 15
```

```python
def print_demo(*arg, **kwargs):
    print(args)
    print(kwargs)
    
print_demo(1, 2, 3, 4, 5, name='Alice', age=20, gender='女')
# (1, 2, 3, 4, 5) 
# {'name': 'Alice', 'age': 20, 'gender': '女'}
```

> `*arg`和 `**kwargs`中的`arg`和`kwargs`都可替换为其他名称，但需保留*和**
>
> 一起使用时必须保证==`*arg`在前`**kwargs`在后==

``` python
def print_demo2(*args, **kwargs):
    print(args)
    print(kwargs)
    
def print_demo(*args, **kwargs):
    # 变量名作为实参传的是对应的元组和字典
    print_demo2(args, kwargs)
    '''
    输出结果：
    ((2，3，4，5),{'name':'Alice','age':20,'gender':'女'})
    {}
    '''
    
    # 加上*号对元组、字典进行拆包，**将字典的键值对作为关键字参数传入（只有传参时会用这种）
    print_demo2(*args, **kwargs)
    '''
    输出结果：
    (2，3，4，5)
    {'name':'Alice','age':20,'gender':'女'}
    '''
    
print_demo(1, 2, 3, 4, 5, name='Alice', age=20, gender='女')
```

### 5. 引用

**python中的引用？**

**变量** **≠** **对象**：变量只是 “引用的名字”，对象才是真正的数据；

比如 a = 10：

10 是**整数对象**（存在内存里）

a 是**引用**（指向 10 这个对象的 “地址”）

再比如 b = a：

不是把 10 复制一份给 b，而是让 b 也指向 10 这个对象（两个引用指向同一个对象）。

![image-20260210143806038](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260210143806155.png)

**补充说明**：局部变量的引用在栈帧中，全局变量的引用在模块的命名空间（堆）中。

每次函数调用，CPython（解释器） 会创建一个 PyFrameObject ：

```python
栈帧（frame）：
- 局部变量表（fast locals）
- 操作数栈
- 指令指针
```

> 这个“栈帧”是 **虚拟机层面的栈**，不是 C 语言意义上的 CPU 栈。

**验证引用传递**

打印a和b的地址值，可以看到地址值是一样的，实际是同一个数据，并不是内存中的两份数据

```python
def fuc1():
    a = 10
    b = a
    
    print(id(a)) # 140730885489864
    print(id(b)) # 140730885489864
    
if __name__ == '__main__':
	fuc1()
```

> **结论：**Python中只有引用传递。一句话：**一切皆引用**
>
> 函数传参时，**传递的是 “指向堆中对象的引用”**，不是对象本身；
>
> 引用的存储位置会变（比如参数引用存到新栈帧），但堆中对象的位置不变；
>
> 最终效果由 “对象是否可变” 决定，核心是 “改引用” 还是 “改堆中对象”。

**可变类型：列表、字典、集合**——修改对中的内容，所有对其的引用都变

**不可变类型：整数、字符串、元组**——无法在函数内修改函数外某个变量的值（不考虑全局变量）

> 1 引用是 **“地址”**：变量存的是引用（指向堆中对象），不是对象本身；
>
> 2 **存储分工**：
>
> - 堆：存所有对象（真正的数据）
>
> - 栈帧：存函数内局部变量 / 参数的引用（函数结束销毁）
>
> - 全局引用：存模块命名空间（长期存在）
>
> 3 **传参本质**：只传引用（引用从外部到函数栈帧），不改堆中对象地址
>
> 4 **效果判断**：
>
> - **不可变对象：改栈帧里的引用** **→** **外部不变**
>
> - **可变对象：改堆中的对象内容** **→** **外部也变（因为两个引用指向同一块堆空间）**

==引用计数为0时，对应的对象空间就会被释放==

### 6. copy()

使用copy对可变对象进行赋值，会将原对象的值复制给另一个堆空间，新的可变对象引用指向此空间，从而两个引用指向不同的空间，不会同步改变

```python
list = [10, 20]
list1 = list # list1的引用指向list引用的堆空间，list和list1的id相同

list = [10, 20]
list1 = list.copy() # 将list的值赋给list1，list和list1的id不同
```

### 7. 匿名函数

格式：==lambda 参数1, 参数2, ... : 表达式 	# 冒号前是参数，冒号后是返回结果的表达式==

```python
"""
普通函数
"""
def get_sum(a, b):
	return a + b # 求和

def get_sub(a, b):
	return a - b # 差

def get_mul(a, b):
	return a * b # 积
# ...

"""
匿名函数
"""
def cal_num(a,b,fn):
	return fn(a,b)

a = 10
b = 20
# 求和
sum_result = cal_num(a,b,lambda a,b:a+b)
sub_result = cal_num(a,b,lambda a,b:a-b)
mul_result = cal_num(a,b,lambda a,b:a*b)
```

### 8. 面向对象内置方法

初始化: `__init__`

对象描述: `__str__`

对象销毁:` __del__`

```python
# 小明同学当前体重是100kg。每当他跑步一次时，则会减少0.5kg；每当他大吃大喝一次时，则会增加2kg
# 1. 定义学生类
class Student:
    # 2. 定义初始化方法
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    # 3. 定义打印方法
    def __str__(self):
    	return f"{self.name}同学的体重是:{self.weight}"
    
    # 4. 定义跑步方法
    def run(self):
        self.weight -= 0.5
        print(f"跑步一次，减重0.5kg, {self.name}当前的体重是:{self.weight}")
        
    # 5. 定义大吃大喝方法
    def eat(self):
        self.weight += 2
        print(f"大吃大喝一次，增加2kg, {self.name}当前的体重是:{self.weight}")
        
# 6. 创建小明同学这个对象
stu = Student('小明',100)

# 7. 调用方法
stu.run()
stu.run()
stu.eat()
```

## <span style='color:red'>Day5</span>

### 1. 使用注解说明参数类型

格式：==def function(形参名:注解)==

注解为形参的数据类型

```python
class HouseItem:
    # 家具类
    '''
    省略具体内容
    '''
    
class House:
    # 房子类
    '''
    省略具体内容
    '''
    # 添加家具方法
    def add_item(self, item:HouseItem): # 使用':[数据类型]'注解，此处表示item是HouseItem类型
		print("要添加 %s" % item)
```

### 2. 访问控制

| 命名方式             | 访问权限   | 说明                                                         |
| -------------------- | ---------- | ------------------------------------------------------------ |
| `attr`（普通）       | **公开**   | 可被外部直接访问和修改                                       |
| `_attr`（单下划线）  | **受保护** | 约定为内部使用，外部应避免访问（非强制）                     |
| `__attr`（双下划线） | **私有**   | 被 Python 解释器改名，外部无法直接访问（强制隐藏）（子类也无法访问） |

### 3. 继承

**继承格式：**

```python
class 父类名(object):
	...(省略)
class 子类名(父类名): # 继承语法
	...(省略)
```

**多继承:**

```python
# 父类1
class Flyable:
    def fly(self):
        print("会飞")

# 父类2
class Swimmable:
    def swim(self):
        print("会游泳")

# 子类继承多个父类
class Duck(Flyable, Swimmable):
    pass

# 使用子类
duck = Duck()
duck.fly()   # 继承Flyable → 会飞
duck.swim()  # 继承Swimmable → 会游泳
```

#### 3.1 菱形问题

![image-20260211202820512](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260211202820652.png)

- 子类D同时继承B和C；
- B和C又同时继承A；
- 若A、B、C中有同名方法，那么D用该方法时，到底执行哪个父类的版本？

``` python
class A:  # 祖父类
    def say(self):
        print("A的say方法")

class B(A):  # 父类1，继承A
    def say(self):
        print("B的say方法")

class C(A):  # 父类2，继承A
    def say(self):
        print("C的say方法")

class D(B, C):  # 子类，继承B和C
    pass  # 未重写say方法

# 问题：D的对象调用say()，会执行B还是C的方法？
d = D()
d.say()  # 输出：B的say方法（为什么？）
```

**菱形问题的核心：方法的调用顺序（MRO）**

```python
# 打印D类的方法解析顺序
print(D.__mro__)
# 输出：
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

> - 顺序规则：从左到右，深度优先，不重复访问（先查 D，再 B，再 C，再 A，最后 object）；
>
> - 因此 `d.say()` 会优先找到 **B** 中的 `say` 方法。
>
> - MRO的计算原则（C3算法）
>
>     1. 子类优先于父类；
>     2. 同一层级的父类，按继承时的顺序（如 `class D(B, C)` 中 **B** 优先于 **C**）；
>     3. 确保祖父类只被访问一次。
>
>     
>
> - 记住：查看 ==`类名.__mro__`== 即可明确方法搜索顺序，无需死记规则。

#### 3.1 子类调用父类方法

子类重写父类方法后，可通过 ==`super()`== 函数调用父类的原始实现

`super()`是匿名父类

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # 调用父类的构造函数
        self.school = school

    def get_info(self):
        return f"{self.name}，{self.age}岁，在{self.school}上学"

# 实例化Student类并调用方法
student = Student("张三", 15, "阳光中学")
print(student.get_info())
```

> **补充说明**：在 Python 2.x 时，如果在子类中需要调用父类中的方法，还可以使用：`父类名.方法(self)`
>
> - 这种方式，目前在 Python 3.x 还支持这种方式
> - 这种方法 **不推荐使用**，因为一旦 **父类发生变化**，方法调用位置的 **类名** 同样需要修改

### 4. 空函数/类

使用`pass`表示空函数/类

```python
# 定义父类
class Father:
    def __init__(self):
        self.gender = 'man'

    def walk(self):
        print("爱好散步行走")

# 定义子类
class Son(Father):
    pass	# 使用pass表示内容为空

# 实例化验证继承
son = Son()
print(son.gender)
son.walk()
```

### 5. 多态

**多态依赖继承和方法重写，需同时满足：**

1. 存在继承关系：子类继承父类；
2. 子类重写父类方法：子类对父类的方法进行重新实现；
3. 父类引用指向子类对象：用父类类型的变量接收子类对象。

```python
# 1. 父类
class Animal:
    def make_sound(self):
        # 父类方法：定义接口
        pass

# 2. 子类（继承+重写）
class Dog(Animal):
    def make_sound(self):  # 重写父类方法
        print("汪汪叫")

class Cat(Animal):
    def make_sound(self):  # 重写父类方法
        print("喵喵叫")

class Duck(Animal):
    def make_sound(self):  # 重写父类方法
        print("嘎嘎叫")

# 3. 统一调用（父类引用指向子类对象）
def animal_sound(animal: Animal):  # 参数声明为父类类型
    animal.make_sound()  # 调用同一方法，表现不同

# 测试多态
dog = Dog()
cat = Cat()
duck = Duck()

animal_sound(dog)   # 输出：汪汪叫
animal_sound(cat)   # 输出：喵喵叫
animal_sound(duck)  # 输出：嘎嘎叫
```

> **关键**：`animal_sound` 函数无需区分传入的是 `Dog`、`Cat` 还是 `Duck`，只需调用 `make_sound` 方法，即可得到对应行为。

### 6. 抽象类与抽象方法

 **抽象类==继承 `ABC`==**

> **说明：**
>
> - 不能被实例化
> - 用来作为父类，规定子类的行为
> - 抽象类中至少有一个抽象方法
>
> **作用：**
>
> - 约束子类必须实现某些方法
> - 提前发现设计错误
> - 统一接口

 **抽象方法==使用 `@abstractmethod`修饰==**

> **说明：**
>
> - 只有方法声明（或部分实现）
> - 子类必须实现父类的全部抽象方法，否则会报错
> - 否则子类不能实例化

**定义方式：**

```python
from abc import ABC, abstractmethod

class Animal(ABC): # 抽象类

    @abstractmethod # 修饰抽象方法
    def speak(self):
        pass
```

**特点**

- 抽象类中至少有一个 `@abstractmethod`
- 抽象类不能创建对象

```python
Animal()  # 报错
```

**抽象类 vs 普通类:**

| 项目                 | 抽象类 | 普通类 |
| --------------- | ------ | ------ |
| 能否实例化           | ❌      | ✅      |
| 是否强制子类实现方法 | ✅      | ❌      |
| 是否用于规范设计     | ✅      | ❌      |

### 7. 抽象属性（`@property`）

**规定子类必须有某个属性**

```python
class Person(ABC):

    @property
    @abstractmethod
    def name(self):
        pass
    
class Student(Person):
    @property
    def name(self):
        return "Tom"
```

## <span style='color:red'>Day6</span>

### 1. 对象属性和类属性

**对象属性：**定义在`__init__`方法中，与具体对象绑定

**类属性：**定义在`__init__`方法外，与类绑定，通过==类名.属性名==访问，对所有对象共享

> 若使用==对象名.属性名==访问类属性，将会给此对象增加一个同名对象属性，而不会访问原类属性

```python
class Student:
    # 类属性：定义在 __init__ 外，所有学生共享
    school = "北京大学"  # 所有学生的学校相同

    def __init__(self, name):
        self.name = name  # 对象属性

# 所有对象共享类属性
stu1 = Student("张三")
stu2 = Student("李四")

print(Student.school)  # 输出：北京大学（推荐：类名访问）
print(stu1.school)     # 输出：北京大学（对象也能访问，但不推荐修改）
print(stu2.school)     # 输出：北京大学（和 stu1 共享同一值）

# 修改类属性（所有对象同步变化）
Student.school = "清华大学"
print(stu1.school)     # 输出：清华大学（所有对象共享新值）
```

### 2. 类方法

绑定到**类本身**的方法，用于操作类属性（通过 `@classmethod` 装饰）

- 通过==`类名.方法名()`== 调用

- 第一个参数固定为 `cls`（代表类本身）
- 可访问/修改类属性，**不能直接访问对象属性**

> `cls`表示类本身
>
> `self`表示对象本身

```python
class Tool:
    # 类属性：记录工具总数
    count = 0

    def __init__(self, name):
        self.name = name  # 对象属性
        Tool.count += 1   # 每次创建对象，类属性 +1

    # 类方法：操作类属性（统计工具总数）
    @classmethod
    def show_total(cls):
        print(f"当前工具总数：{cls.count} 个")  # 通过 cls 访问类属性

# 调用类方法（推荐用类名）
Tool.show_total()  # 输出：当前工具总数：0 个

# 创建对象后，类属性变化
tool1 = Tool("锤子")
tool2 = Tool("螺丝刀")
Tool.show_total()  # 输出：当前工具总数：2 个
```

### 3. 静态方法

定义在类中的**普通函数**，与类属性、对象属性均无直接关联（通过 `@staticmethod` 装饰）

- 无强制参数（可传普通参数，无需 `self` 或 `cls`）
- **不能直接访问类属性或对象属性**（如需访问，需通过参数传入）
- 可通过 `类名.方法名()` 调用，也可通过 `对象.方法名()` 调用；

```python
class MathHelper:
    # 静态方法：纯功能逻辑（判断是否为偶数）
    @staticmethod
    def is_even(num):
        return num % 2 == 0

    # 静态方法：纯功能逻辑（计算平均值）
    @staticmethod
    def average(a, b):
        return (a + b) / 2

# 调用静态方法（推荐用类名）
print(MathHelper.is_even(4))   # 输出：True
print(MathHelper.average(3, 5)) # 输出：4.0
```

### 4. `__new__`方法

- 使用类名()创建对象时，Python解释器会先调用`__new__`方法为对象分配空间
- `__new__`是由`object`基类提供的内置静态方法，主要作用有两个：
    - 在内存中为对象分配空间
    - 返回对象的引用
- Python解释器获得对象引用后，将引用作为第一个参数传递给`__init__`方法
- 通过重写`__new__`可以控制对象的创建过程，确保只生成一个实例

### 5. 单例模式

单例是一种创建型设计模式，让你保证一个类只有一个实例对象，每一次执行`类名()`创建的对象，内存地址是相同的。

```python
class MusicPlayer(object):
    instance = None  # 始终指向唯一的音乐播放器对象

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, music_name):
        self.music_name = music_name

    def play(self):
        print(f"正在播放: {self.music_name}")


player1 = MusicPlayer('青花瓷')
player2 = MusicPlayer('如愿')
player1.play()
player2.play()
```

 ### 6. 异常

通过`try-except`结构，可以 “捕获” 异常并处理，避免程序崩溃

``` python
try:
    # 可能会引发异常的代码
    pass
except (错误类型1, 错误类型2):
    # 针对上述两种错误类型，执行对应的代码
    pass
except 错误类型3 as e:
    # 针对错误类型3，执行对应的代码，e是异常对象
    # 可以记录日志...
    pass
except Exception as e:
    # 兜底处理，捕获所有其他异常
    # 可以记录日志...
    pass
else:
    # 如果没有异常发生，则会执行此处的代码
    pass
finally:
    # 无论有没有异常发生，都一定会执行此处的代码
    pass
```

> 即使在`except`或`else`中包含`return`语句，依然会执行`finally`中的代码

**异常传递**

- 当函数/方法执行出现异常时，会**将异常传递给函数/方法的调用一方**。
- 如果传递到主程序，仍然没有异常处理，程序才会被终止。
- 在开发中，可以**在主函数中增加异常捕获**。
- 而在主函数中调用的其他函数，只要出现异常，都会**传递到主函数的异常捕获**中。
- 这样就不需要在代码中，增加大量的异常捕获，能够保证代码的整洁。

![image-20260212170517729](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260212170517886.png)

> **异常传递的终止条件：**
>
> - **被某个层级的 try - except 捕获**：如上述例子中，主程序的 except 捕获异常后，传递终止。
> - **到达程序顶层仍未被捕获**：此时程序会打印异常信息并崩溃。

### 7. 抛出异常

在开发中，除了 **代码执行出错** Python 解释器会 **抛出** 异常之外， 还可以根据 **应用程序特有的业务需求主动抛出异常**

基本语法：==raise 异常对象==

![image-20260212170754715](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260212170754835.png)

```python
def get_password():
    # 假设这个函数从数据库或配置文件中获取密码
    password = "abc"  # 模拟一个长度不足的密码
    
    if len(password) < 8:
        # 主动抛出异常
        raise Exception("密码长度不正确")
    
    return password

try:
    pwd = get_password()
    print(f"获取到的密码是: {pwd}")
except Exception as e:
    print(f"发生错误: {e}")
```

> **注意事项：**
>
> 1. 使用 `raise` 关键字可以主动抛出异常。
> 2. `raise` 关键字后面可以跟一个异常对象，例如 `Exception("错误信息")`。
> 3. 抛出的异常需要被外部的 `try - except` 语句捕获并处理，否则程序会崩溃。

### 8. 断言（Assertion）异常

**语法：**==`assert 条件表达式, 错误信息`==

**执行逻辑：**

- 如果 `条件表达式` 的结果为 `True`，程序继续执行。
- 如果 `条件表达式` 的结果为 `False`，程序抛出 `AssertionError` 异常，并显示 `错误信息`。

```python
def calculate_average(numbers):
    # 断言：传入的列表不能为空
    assert len(numbers) > 0, "列表不能为空"
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

# 正常调用
scores = [90, 85, 78]
avg = calculate_average(scores)
print(f"平均分是: {avg}")  # 输出: 平均分是: 84.333...

# 异常调用
empty_scores = []
avg_empty = calculate_average(empty_scores)  # 此处会抛出 AssertionError
```

### 9. 常见异常类型

| 编号 | 异常类型            | 触发场景                    | 示例                                         |
| ---- | ------------------- | --------------------------- | -------------------------------------------- |
| 1    | `TypeError`         | 数据类型错误                | `"2" + 2`（字符串 + 整数）                   |
| 2    | `ValueError`        | 数据值合法但不符合要求      | `int("abc")`（字符串无法转整数）             |
| 3    | `IndexError`        | 序列索引越界                | `[1,2][3]`（列表索引 3 不存在）              |
| 4    | `KeyError`          | 字典键不存在                | `{"name": "张三"}["age"]`                    |
| 5    | `ZeroDivisionError` | 除以零                      | `1 / 0`                                      |
| 6    | `AttributeError`    | 访问对象不存在的属性 / 方法 | `Student().score`（Student 类无 score 属性） |
| 7    | `NameError`         | 变量未定义                  | `print(x)`                                   |
| 8    | `AssertionError`    | 断言失败                    | `x = 5; assert x > 10`                       |
| 9    | `FileNotFoundError` | 打开的文件不存在            | `open("data.txt", "r")`                      |

### 10. 模块

通过`import`导入模块，导入方式：

| 导入方式             | 语法示例                            | 说明                                  |
| -------------------- | ----------------------------------- | ------------------------------------- |
| 导入整个模块         | `import 模块名`                     | 使用时需加模块名前缀（`模块名.功能`） |
| 导入模块并取别名     | `import 模块名 as 别名`             | 简化模块名（`别名.功能`）             |
| 导入模块中的特定功能 | `from 模块名 import 功能1, 功能2`   | 直接使用功能名（无需前缀）            |
| 导入特定功能并取别名 | `from 模块名 import 功能名 as 别名` | 直接使用别名                          |
| 导入模块中的所有功能 | `from 模块名 import *`              | 不推荐（可能导致命名冲突）            |

> 将模块`mod1.py`导入模块`mod2.py`中，执行`mod2.py`时会自动先执行`mod1.py`
>
> `if __name__ == "__main__":`下的内容不会被执行

**模块搜索路径**

当导入模块时，Python解释器会按照以下顺序查找模块文件：

1. 当前执行脚本所在的目录。
2. 系统环境变量PYTHONPATH指定的目录。
3. Python安装目录的标准库路径（如site-packages）。

可以通过`sys.path`查看模块的搜索路径

```python
import sys
print(sys.path) # 输出模块搜索路径列表
```

### 11. 模块的name属性

每个模块都有一个内置属性`__name__`，用于标识模块的名字

- 当模块被导入时，`__name__`属性的值为模块的名字
- 当模块被直接执行时，`__name__`属性的值为`__main__`

于是模块被导入后，运行导入的模块无法执行`if __name__ == "__main__":`下的代码

> `if __name__ == "__main__":`下的变量在本模块中是全局变量
>
> `if __name__ == "__main__":`中的内容无法被其他模块使用

### 12. 包

包是一个包含了`__init__.py`文件的文件夹

包下可包含：

- `__init__.py` 文件
- 模块文件
- 子包

**导入模块的三种方式：**

1. `import 包名.模块名`
2. `from 包名 import 指定模块`
3. `from 包名 import *`

**快速入门案例：**
1. 新建包 `my_package`
2. 在包内新建模块 `my_module1` 和 `my_module2`
3. 在两个模块内各定义一个函数 `say_hello()`
4. 导入并调用

**文件准备：**

*   **my_module1.py**
    ```python
    def say_hello():
        print('我是my_module1的hello')
    ```

*   **my_module2.py**
    ```python
    def say_hello():
        print('我是my_module2的hello')
    ```

****

**导包并使用的方式：**

**方式一：`import 包名.模块名`**

```python
# 导入 wangdao 包下的 my_module1 模块
import wangdao.my_module1

# 使用模块内的方法
wangdao.my_module1.say_hello()
```

**方式二：`from 包名 import 模块名`**

```python
# 导入 wangdao 包下的 my_module1 模块
from wangdao import my_module1

# 使用模块内的方法
my_module1.say_hello()
```

**方式三：`from 包名 import *`**

导入包内 `__init__.py` 文件中 `__all__` 列表里的所有模块。

> 注意：需要在 `__init__.py` 文件中定义 `__all__` 属性。

`__init__.py`文件：

```python
# 指定以下模块可以导入
from . import my_module1 
from . import my_module2
```

> '`.`'代表**当前目录**（即当前模块所在的目录）
>
> '`..`'代表上一级目录

```python
# 导入 wangdao 包下 __all__ 列表里的所有模块
from wangdao import *

# 使用模块内的方法
my_module1.say_hello()
my_module2.say_hello()
```

### 13. pip

安装最新版本的包

```cmd
pip3 install 包名
```

安装指定版本的包

```cmd
pip3 install 包名==版本号
```

卸载已安装的包

```cmd
pip3 uninstall 包名
```

将已安装的包升级到最新版本

```cmd
pip3 install --upgrade 包名 # 或 -U 简写
```

查看已安装的包列表

```cmd
pip3 list
```

查看某个包的详细信息

```cmd
pip3 show 包名
```

临时更换安装源安装

```cmd
pip3 install 包名 -i 镜像源地址
```

> 常用国内镜像源：
>
> 豆瓣：https://pypi.doubanio.com/simple/
>
> 阿里云：https://mirrors.aliyun.com/pypi/simple/
>
> 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/

永久设置安装源

```cmd
pip config set global.index-url 镜像源地址
```

### 14. 文件

#### 14.1 打开文件 `open()`

打开文件并返回文件句柄，使用==`文件句柄.文件方法`==格式对文件进行操作

基本语法：==`文件句柄 = open(文件路径, 打开模式, encoding=编码格式)`==

> 使用==`文件句柄.close()`==关闭文件

**打开模式**

| 模式 | 类型     | 核心功能                                     | 注意事项                             |
| :--- | :------- | :------------------------------------------- | :----------------------------------- |
| `r`  | 文本读   | **只读**（默认模式），文件不存在则报错       | 不能写操作                           |
| `w`  | 文本写   | **覆盖写**，文件不存在则创建，存在则清空内容 | 会覆盖原有内容，谨慎使用             |
| `a`  | 文本追   | **追加写**，文件不存在则创建，内容加在末尾   | 不会覆盖原有内容，适合写日志         |
| `r+` | 文本读写 | 可读可写，文件**不存在则报错**               | 写操作从文件开头**覆盖**             |
| `w+` | 文本读写 | 可读可写，文件**不存在则创建**，存在则清空   | 先**清空**再读写，慎用               |
| `a+` | 文本读写 | 可读可写，文件**不存在则创建，写在末尾**     | 读操作需先移动指针（后续讲`seek()`） |
| `rb` | 二进制读 | 以二进制格式读（如图片、视频）               | 不指定`encoding`，避免乱码           |
| `wb` | 二进制写 | 以二进制格式写（如保存图片）                 | 常用于文件传输、保存非文本数据       |
| `ab` | 二进制追 | 以二进制格式追加写                           | 如给视频文件追加内容                 |

#### 14.2 文件读方法

- **`read(size)`：读指定长度 / 全部内容**
    - `size`（可选）：指定读取字符数，默认读取全部
- **`readline()`：逐行读取（适合大文件）**
    - 每次调用读“一行内容”，包括换行符`\n`
    - 读到文件末尾返回空字符串""，可用于**循环读数**
- **`readlines()`：读取所有行，返回列表**
    - 把文件每一行作为列表的一个元素，适合处理 “需要按行操作” 的场景

#### 14.3 文件写方法

- **`write(content)`：写入字符串/二进制数据**
    - 文本模式：`content`必须是字符串
    - 二进制模式：`content`必须是字节串（如：`b"hello`）
- **`writelines(line)`：写入列表（元素为字符串）**
    - 用于批量写入多行内容，列表中每个元素是一行字符串（需手动加`\n`）

### 15. 安全操作`with`

with语句能自动关闭文件（退出with块时触发），无需手动调用`close()`

**语法格式：**

```python
with open(文件路径, 模式, encoding=编码) as 文件句柄：
    # 缩进内执行读写操作
    读/写代码
    # 退出缩进后，文件自动关闭，无需手动调用 `close()`
```

案例：

```python
# 读文件：with自动关闭
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)  # 缩进内操作文件

# 写文件：with自动关闭
with open("with_write.txt", "w", encoding="utf-8") as f:
    f.write("用with写的内容，无需手动close() \n")
    f.write("自动关闭更安全！")

# 验证：文件已关闭
print(f.read())  # 报错: ValueError: I/O operation on closed file.
```

### 16. 文件/目录操作

需要导入`os`模块，使用==`import os`==

**文件操作**

| 序号 | 方法名   | 说明                     | 示例                              |
| ---- | -------- | ------------------------ | --------------------------------- |
| 01   | `rename` | 重命名文件               | `os.rename(源文件名, 目标文件名)` |
| 02   | `remove` | 删除文件, 不能删除文件夹 | `os.remove(文件名)`               |

**提示**: 文件或者目录操作都支持 **相对路径** 和 **绝对路径**



**目录操作**

| 序号 | 方法名       | 说明                           | 示例                      |
| ---- | ------------ | ------------------------------ | ------------------------- |
| 01   | `listdir`    | 列出指定目录下的所有文件       | `os.listdir(目录名)`      |
| 02   | `mkdir`      | 创建目录文件                   | `os.mkdir(目录名)`        |
| 03   | `rmdir`      | 删除目录文件, 注意只能删除空的 | `os.rmdir(目录名)`        |
| 04   | `getcwd`     | 获取当前目录                   | `os.getcwd()`             |
| 05   | `chdir`      | 修改工作目录                   | `os.chdir(目标目录)`      |
| 06   | `path.isdir` | 判断是否是文件夹               | `os.path.isdir(文件路径)` |

### 17. 给Python传参

- **方式一：PyCharm设置**

    ![image-20260213003315110](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260213003315221.png)

    ![image-20260213003251304](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260213003251429.png)

    > 参数之间用空格隔开

    ****

- **方式二：命令行**

    在命令行中输入命令传参并执行：

    ``` 
    python .\17-给python传参.py ip port
    ```

    - **`.\17-给python传参.py`**：要执行的 Python 脚本文件（`.\` 表示当前目录）
    - **`ip` 和 `port`**：传递给脚本的两个命令行参数

    使用 `sys.argv` 打印传递的所有参数，`sys.argv`是一个列表

    ``` python
    import sys
    
    print(sys.argv)  # 打印所有命令行参数
    ```

    打印结果：

    ```python
    ['.\17-给python传参.py', 'ip', 'port']
    ```

    > - `sys.argv[0]` = `'.\17-给python传参.py'`（脚本名称）
    > - `sys.argv[1]` = `'ip'`（第一个参数）
    > - `sys.argv[2]` = `'port'`（第二个参数）

### 18. `eavl()`

作用：**将字符串作为代码来执行**（一般用于读配置文件（字典形式））

- 将字典放在文件中，读取出来后直接作为参数传给`eval()`，将会直接变为字典变量
- 语句：`eval("1+1")`执行结果为2

### 19. `is`与`==`的区别

`is`用于判断两个变量**引用的对象是否为同一个**（内存地址是否一致）`

> `is not`同理

`==`用于判断引用变量的**值是否相等**

### 20. 浅cpoy与深copy

图解：

<img src="https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260213011114515.png" alt="image-20260213011114370" style="zoom:67%;" />

<img src="https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260213011124669.png" alt="image-20260213011124512" style="zoom:75%;" />

```python
def use_copy():
    a = [1, 2]
    b = [10, 20]
    c = [a, b]
    d = c.copy() # 浅拷贝
    a[0] = 5 # 修改a时c,d都会变
    
    print(id(c[0]))
    print(id(d[0]))# c[0]和d[0]的id相同

def use_deepcopy():
    a = [1, 2]
    b = [10, 20]
    c = [a, b]
    d = c.deepcopy() # 深拷贝
    a[0] = 5 # 修改a时c会变，a不会变
    
    print(id(c[0]))
    print(id(d[0]))# c[0]和d[0]的id相同
```

浅拷贝：

<img src="https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260213011954846.png" alt="浅copy" style="zoom:150%;" />

深拷贝：

<img src="https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260213011957055.png" alt="深copy" style="zoom:150%;" />

> 列表和字典中自带的`copy()`都是浅拷贝
>
> 深拷贝是 “彻底的拷贝”，原数据和拷贝数据完全独立，无任何关联。

> `import copy`
>
> 浅拷贝对不可变类型和可变类型的copy不同。
>
> - `copy.copy()`对于可变类型，会进行浅拷贝
>
> - `copy.copy()`对于不可变类型，不会拷贝数据，仅仅是拷贝引用并指向对象

## <span style="color:red">Day7</span>

### 1. 正则表达式

**匹配单个字符：**

| 字符  | 功能                                       | 示例      | 匹配结果                   |
| :---- | :----------------------------------------- | :-------- | :------------------------- |
| `.`   | 匹配任意1个字符（除了`\n`）                | `a.b`     | aab, acb, alb（不匹配 ab） |
| `[ ]` | 匹配`[ ]`中列举的字符                      | `a[0-9]b` | a0b, a5b（不匹配 aab）     |
| `\d`  | 匹配数字，即0-9，等价于`[0-9]`             | `a\d`     | a1, a9（不匹配 aa）        |
| `\D`  | 匹配非数字，即不是数字                     | `a\D`     | aa, ab（不匹配 a1）        |
| `\s`  | 匹配空白，即空格，tab键                    | `a\sb`    | a b, a\tb（不匹配 aab）    |
| `\S`  | 匹配非空白                                 | `a\Sb`    | aab, alb（不匹配 a b）     |
| `\w`  | 匹配字母、数字、下划线，即a-z、A-Z、0-9、_ | `\w\w`    | a1, _3, Ab（不匹配 @#）    |
| `\W`  | 匹配非单词字符                             | `\W`      | @, #, _（不匹配 a1）       |

**匹配多个字符：**

| 字符    | 功能                                                | 示例      | 匹配结果    |
| :------ | :-------------------------------------------------- | :-------- | :---------- |
| `*`     | 匹配前一个字符出现0次或者无限次，即可有可无         | `a*b`     | b, ab, aaab |
| `+`     | 匹配前一个字符出现1次或者无限次，即至少有1次        | `a+b`     | ab, aaab    |
| `?`     | 匹配前一个字符出现1次或者0次，即要么有1次，要么没有 | `a?b`     | b, ab       |
| `{n}`   | 匹配前一个字符出现n次                               | `a{3}b`   | aaab        |
| `{m,n}` | 匹配前一个字符出现从m到n次                          | `a{1,2}b` | ab, aab     |

**匹配开头结尾：**

| 字符 | 功能           | 示例   | 匹配结果                                 |
| :--- | :------------- | :----- | :--------------------------------------- |
| `^`  | 匹配字符串开头 | `^abc` | 匹配 abc123（开头是 abc），不匹配 123abc |
| `$`  | 匹配字符串结尾 | `abc$` | 匹配 123abc（结尾是 abc），不匹配 abc123 |

**匹配分组：**

| 字符   | 功能                                  | 示例                | 匹配结果                             |
| :----- | :------------------------------------ | :------------------ | :----------------------------------- |
| `|`    | 匹配左右任意一个表达式                | `^[a-z]+$|^[A-Z]+$` | abc、ABC 匹配，不匹配 Abc            |
| `()`   | 将括号中字符作为一个分组              | `(ab)+`             | ab、abab（1次或多次ab），不匹配 aab  |
| `\num` | 引用分组num匹配到的字符串（替换时用） | `(a)(b)\1\2`        | abab（`\1`是a，`\2`是b，组合为abab） |

****

**反向匹配**

```python
# 判断字符串是否由同一个单词重复两次构成
def match_group3():
    texts = [
        "hello hello",
        "test test",
        "hello world"
    ]
    pattern = r'^(\w+)\s+\1$'
    # '\1'反向引用：必须与第一个分组内容完全一致

    for text in texts:
        ret = re.match(pattern, text)
        if ret:
            print(f'{text}由同一个单词重复两次构成')
        else:
            print(f'{text}不由同一个单词重复两次构成')
```

**正则拆解说明**：

- `^`
    - 字符串开始
- `(\w+)`
    - 捕获一个或多个字母 / 数字 / 下划线
    - 这是 **分组 1**
- `\s+`
    - 一个或多个空白字符（空格、tab 等）
- `\1`
    - **反向引用**：必须与第一个分组内容完全一致
- `$`
    - 字符串结束

### 2. re模块

使用re模块通过正则表达式对字符串进行匹配

**基本使用步骤：**

```python
# 第一步：导入re模块
import re

# 第二步：使用match方法(或其他方法)进行匹配操作
result = re.match(pattern正则表达式, string要匹配的字符串, flags=0)
# flags：可选，表示匹配模式，比如忽略大小写，多行模式等

# 第三步：如果数据匹配成功，使用group方法来提取数据
result.group()
```

****

#### 2.1 match

语法格式：==`re.match(pattern, text, flags=0)`==

- **功能**：从字符串 **开头** 开始匹配，仅验证“开头是否符合规则”
- **返回值**：匹配成功返回 `Match` 对象，失败返回 `None`
- **参数**：
    - `pattern`：正则规则字符串（**必加 r 原始字符串，避免转义**）
    - `text`：待匹配的目标字符串
    - `flags`：匹配模式（如 `re.IGNORECASE` 忽略大小写，后续进阶讲）

**示例：验证手机号格式**

```python
import re

# 规则：11位数字，以13/14/15/17/18开头，且是完整字符串

# ^1：表示以1开头
# [34578]：第二位是3,4,5,7,8中的一个
# \d：匹配任意数字
# {9}：任意数字出现9次
# $：结束符，表示到此结束
pattern = r"^1[34578]\d{9}$"
text1 = "13812345678"  # 合法手机号
text2 = "12345678901"  # 非法手机号（开头不符）

print(re.match(pattern, text1))  # 输出：<re.Match object; ...>（成功）
print(re.match(pattern, text2))  # 输出：None（失败）
```

****

#### 2.2 search

语法格式：==`re.search(pattern, text, flags=0)`==

- **功能**：从字符串 **任意位置** 匹配，找到“第一个符合规则的内容”即停止
- **区别 match**：`match` 只看开头，`search` 遍历整个字符串

**示例：提取文本中第一个手机号**

```python
import re

text = "我的手机号：13812345678，备用号：13987654321"
pattern = r"1[34578]\d{9}"  # 不限制位置，只匹配手机号格式

result = re.search(pattern, text)
if result:
    print("第一个手机号：", result.group())  # 输出：第一个手机号：13812345678
    print("位置：", result.span())           # 输出：位置：(6, 17)（起始/结束索引）
```

> - `group()` - 获取匹配到的完整字符串
> - `span()` - 返回匹配的起止索引位置（元组形式）

****

#### 2.3 findall

语法格式：==`re.findall(pattern, text, flags=0)`==

- **功能**：从字符串中找到 **所有符合规则的内容**，返回列表
- **返回值**：列表（元素为匹配的字符串，若有分组则返回分组内容）

**示例：批量提取所有手机号**

```python
import re

text = "我的手机号: 13812345678，备用号: 13987654321"
pattern = r"1[34578]\d{9}"

phones = re.findall(pattern, text)
print("所有手机号:", phones)  # 输出：所有手机号: ['13812345678', '13987654321']
```

****

#### 2.4 sub

语法格式：==`re.sub(pattern, repl, text, count=0, flags=0)`==

- **功能**：将匹配到的内容替换为 `repl`（字符串或函数）
- **参数**：
    - `count=0`：替换所有匹配内容
    - `count=1`：只替换第一个

**示例：敏感词替换**

```python
import re

text = "这个内容是垃圾，不要传播垃圾信息"
pattern = r"垃圾"
new_text = re.sub(pattern, "*", text)  # 替换所有“垃圾”为*
print(new_text)  # 输出：这个内容是*，不要传播*信息
```

**示例：手机号格式美化**

```python
import re

text = "13812345678"

# ()：表示分组匹配，将内部字符视为一个整体，后续可以提取
pattern = r"(\d{3})(\d{4})(\d{4})"  # 分3个分组（前3/中4/后4位）

new_text = re.sub(pattern, r"\1 \2 \3", text)  # \1代表第1个分组
print(new_text)  # 输出：138 1234 5678
```

****

#### 2.5 split

语法格式：==`re.split(pattern, text, maxsplit=0, flags=0)`==

- **功能**：用 **“匹配到的内容”作为分隔符**，分割字符串，返回列表
- **参数**：
    - `maxsplit=0`：全部分割
    - `maxsplit=1`：只分割一次

**示例：按“空格 / 逗号 / 分号”分割字符串**

```python
import re

text = "apple banana,orange;grape"
pattern = r"[ ,;]"  # 匹配空格、逗号、分号中的任意一个

result = re.split(pattern, text)
print("分割结果:", result)  # 输出：分割结果: ['apple', 'banana', 'orange', 'grape']
```

### 3.  re.compile (pattern, flags=0)：预编译正则

将正则规则预编译为 Pattern 对象，后续多次使用时提升效率（避免重复解析规则）

**适用场景**：同一正则规则需要匹配多次（如循环处理大量文本）

**示例：**预编译手机号正则，在多个文本中搜索

```python
import re

# 预编译正则规则（只编译一次）
pattern = re.compile(r"1[34578]\d{9}")

# 多次使用预编译的 Pattern 对象
texts = ["文本1: 13812345678", "文本2: 13987654321", "文本3: abc123"]
for text in texts:
    result = pattern.search(text)  # 直接用 Pattern 对象调用 search
    if result:
        print(f"{text}: 提取到手机号: {result.group()}")
```



### 4. flags 参数：匹配模式控制

常用`flags`参数值（直接使用简称即可）：

- `re.IGNORECASE`（简称 `re.I`）：忽略大小写匹配
- `re.DOTALL`（简称 `re.S`）：让 `.` 匹配换行符 `\n`（默认 `.` 不匹配 `\n`）
- `re.MULTILINE`（简称 `re.M`）：让 `^` 和 `$` 匹配 **每行的开头和结尾**（默认只匹配整个字符串的开头结尾）

**示例：**忽略大小写匹配hello

```python
import re

pattern = r"hello"
text = "Hello HELLO hello"

# 不忽略大小写：只匹配小写 hello
print(re.findall(pattern, text))     # 输出: ['hello']

# 忽略大小写：匹配所有大小写形式
print(re.findall(pattern, text, re.I))   # 输出: ['Hello', 'HELLO', 'hello']
```

### 5. 如何查找第二个

`search` 只能查找第一个匹配项。如果要查找第二个，可以使用 `finditer` 配合 `next` 实现：

- `finditer` 返回一个迭代器，包含所有匹配项
- `next()` 用于逐个获取匹配项

```python
import re

def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)
    try:
        next(matches)          # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None

text = "abc123def456ghi789"
pattern = r"\d+"

second = find_second_match(pattern, text)
print("第二个匹配的数字:", second)  # 输出：第二个匹配的数字: 456
```

> `next()`先返回当前所指元素值，再指向下一元素

### 6. 生成器函数（与迭代器类似）

实现一个**生成器函数**，模仿 Python 内置 `range()` 的基本功能：

```python
def my_range(n):
    i = 0
    while i < n:
        yield i  # 冻结当前执行位置，并返回i
        i += 1
    return None
```

> - 当执行到 yield 时，函数会**暂停**，返回当前值
> - 下次调用时会从**暂停的位置**继续执行

**使用示例：**

```python
# 创建生成器对象
g = my_range(3)

# 方式1：使用 next() 逐个获取
print(next(g))  # 0
print(next(g))  # 1  
print(next(g))  # 2
print(next(g))  # StopIteration 异常

# 方式2：使用 for 循环自动处理
for num in my_range(5):
    print(num)  # 输出 0,1,2,3,4
```

当调用 `my_range(3)` 时：

1. **第一次**调用：执行到 `yield 0`，返回0，函数暂停
2. **第二次**调用：从 `i += 1` 继续，`i=1`，循环，`yield 1`，返回1，暂停
3. **第三次**调用：从 `i += 1` 继续，`i=2`，循环，`yield 2`，返回2，暂停
4. **第四次**调用：从 `i += 1` 继续，`i=3`，循环条件 `i < 3` 不成立，退出循环，返回None，抛出StopIteration

### 7. `iter()`函数

将**可迭代对象**传给`iter`函数进行处理，返回一个**迭代器**

```python
from collections.abc import Iterable, Iterator

def use_for():
    my_list = [1, 2, 3]  # 可迭代对象
    print(isinstance(my_list, Iterable))  # 判断是否是可迭代对象->是
    print(isinstance(my_list, Iterator))  # 判断是否是迭代器->否
    for i in my_list:  # 第一次遍历打印成功
        print(i)
    for i in my_list:  # 第二次遍历打印成功
        print(i)

# 调用函数
use_for()
```

> - 列表是**可迭代对象**，不是迭代器
>     - 对于可迭代对象使用`for`遍历，会自动先将可迭代对象变为迭代器然后进行遍历
> - **可迭代对象**可以遍历多次
> - **迭代器**只能遍历一次

```python
from collections.abc import Iterable, Iterator

def use_for():
    my_list = [1, 2, 3]  # 可迭代对象
    print(isinstance(my_list, Iterable))  # 判断是否是可迭代对象->是
    list_iterator = iter(my_list)  # 将列表转为迭代器
    print(isinstance(my_list, Iterator))  # 判断是否是迭代器->是
    for i in my_list:  # 第一次遍历打印成功
        print(i)
    for i in my_list:  # 第二次遍历无打印内容（迭代器只能遍历一次）
        print(i)

# 调用函数
use_for()
```

### 8. 贪婪与非贪婪

- **贪婪匹配**：默认行为，量词（`* + {n,}`）会**“尽可能多”**地匹配字符
- **非贪婪匹配**：在量词后加？（如 `*? +? {n,}?`），会**“尽可能少”**地匹配字符

| 贪婪量词 | 非贪婪量词 | 含义       | 示例文本 | 贪婪匹配结果 | 非贪婪匹配结果 |
| :------- | :--------- | :--------- | :------- | :----------- | :------------- |
| *        | *?         | 0 次或多次 | aabab    | aabab        | aab            |
| +        | +?         | 1 次或多次 | aabab    | aabab        | aa             |
| {n,}     | {n,}?      | 至少 n 次  | aaaabbb  | aaaabbb      | aaa            |

**示例：从HTML标签中匹配内容的内容**

```python
import re

text = "<div>内容1</div><div>内容2</div>"

# 1. 贪婪匹配（.*尽可能多匹配，从第一个<div>到最后一个</div>）
greedy_pattern = r"<div>.*</div>"  # 注意：这里原文有笔误，应该是.*，不是.*?
print("贪婪匹配:", re.findall(greedy_pattern, text))
# 输出：贪婪匹配: ['<div>内容1</div><div>内容2</div>']（匹配整个字符串）

# 2. 非贪婪匹配（.*?尽可能少匹配，从第一个<div>到最近的</div>）
non_greedy_pattern = r"<div>.*?</div>"
print("非贪婪匹配:", re.findall(non_greedy_pattern, text))
# 输出：非贪婪匹配: ['<div>内容1</div>', '<div>内容2</div>']（匹配两个独立标签）

non_greedy_pattern = r"<div>(.*?)</div>"
print("非贪婪匹配:", re.findall(non_greedy_pattern, text))
# 输出：非贪婪匹配: ['内容1', '内容2']（匹配两个独立标签内的内容）
```

### 9. `r'字符串'`

这里的`r`表示原生字符串，正常打印字符串时对于例如 '\\' 的字符我们需要进行转义，但使用 `r'字符串'`则不需要进行转义

### 10. 新建文件自动加注释

![image-20260214010804585](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260214010804899.png)

```python
# 作者：
# ${YEAR}年${MONTH}月${DAY}日${HOUR}时${MINUTE}分
# ...
```

### 11. 面向对象思想写二叉树

```python
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []  # 辅助队列

    def insert_node(self, value):
        """
        插入一个新结点
        :param value:插入的值
        :return:
        """
        new_node = TreeNode(value)
        self.queue.append(new_node)  # 入队
        if self.root is None:
            self.root = new_node  # 树为空，就作为树根
        else:
            if self.queue[0].left is None:
                self.queue[0].left = new_node  # 新结点作为左孩子
            else:
                self.queue[0].right = new_node  # 新结点作为右孩子
                self.queue.pop(0)  # 出队

    def pre_order(self, current_node: TreeNode):
        """
        前序遍历，深度优先遍历
        :param current_node:
        :return:
        """
        if current_node:
            print(current_node.value, end=' ')
            self.pre_order(current_node.left)
            self.pre_order(current_node.right)

    def mid_order(self, current_node: TreeNode):
        if current_node:
            self.mid_order(current_node.left)
            print(current_node.value, end=' ')
            self.mid_order(current_node.right)

    def last_order(self, current_node: TreeNode):
        if current_node:
            self.last_order(current_node.left)
            self.last_order(current_node.right)
            print(current_node.value, end=' ')

    def level_order(self):
        queue = deque()  # 双端队列，使用双向链表来实现的
        queue.append(self.root)
        while queue:
            node:TreeNode=queue.popleft()
            print(node.value,end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.insert_node(i)
    tree.pre_order(tree.root)
    print('\n-----------------------------')
    tree.mid_order(tree.root)
    print('\n-----------------------------')
    tree.last_order(tree.root)
    print('\n-----------------------------')
    tree.level_order()
```

### 12. 容器：双端队列`deque`

| 操作             | 方法                             | 描述                                                         |
| :--------------- | :------------------------------- | :----------------------------------------------------------- |
| **创建**         | `dq = deque(iterable, maxlen=N)` | 创建一个双端队列，`iterable`是初始元素，`maxlen`是可选的最大长度。 |
| **右侧添加**     | `dq.append(x)`                   | 在右端（尾部）添加一个元素`x`。                              |
| **左侧添加**     | `dq.appendleft(x)`               | 在左端（头部）添加一个元素`x`。                              |
| **右侧移除**     | `dq.pop()`                       | 移除并返回右端的元素。                                       |
| **左侧移除**     | `dq.popleft()`                   | 移除并返回左端的元素。                                       |
| **右侧批量添加** | `dq.extend(iterable)`            | 在右端一次性添加多个元素。                                   |
| **左侧批量添加** | `dq.extendleft(iterable)`        | 在左端一次性添加多个元素。                                   |
| **旋转**         | `dq.rotate(n)`                   | 将队列向右旋转`n`步（`n`为负数则向左旋）。                   |
| **清空**         | `dq.clear()`                     | 删除所有元素。                                               |
| **获取长度**     | `len(dq)`                        | 返回队列中的元素个数。                                       |

> `extendleft()`方法在左侧批量添加元素时，最终结果会是原迭代器顺序的**反转**，因为它是一个一个从左侧添加的。

### 13. 排序函数`sorted()`

对**可迭代对象**（列表、元组、字典等）进行排序，返回一个新的排序后的**列表**，**不改变原对象**。

> 列表内置的`sort()`方法会改变原对象

**基本语法：**

`sorted(iterable, key=None, reverse=False)`

- **`iterable`**: 需要排序的**可迭代对象**（必传，如列表、元组、字符串等）
- **`key`**: 排序的“依据”，接受一个**函数**作为参数，用于指定“按元素的什么特征排序”（可选，默认按元素本身大小排序，字典默认按照key排序）
- **`reverse`**: 排序方向（可选，False 为升序，True 为降序，默认 False）

**key示例：按照元素的长度排序**

```python
words = ["apple", "banana", "cat", "dog"]
# for i in words  i传给len
# 比较 len(i) > len(i1)
# key=len: 按字符串长度排序
sorted_words = sorted(words, key=len)
print(sorted_words)    # ['cat', 'dog', 'apple', 'banana']
# 'banana' (长度2→2→5→6)
```

**key示例：按照字典的某个键的值排序**

```python
students = [
    {"name": "Alice", "age": 18},
    {"name": "Bob", "age": 16},
    {"name": "Charlie", "age": 20}
]

# key=lambda x: x["age"]: 按"age"字段排序
sorted_students = sorted(students, key=lambda x: x["age"])  # 使用匿名函数
print(sorted_students)

# 输出:[{'name': 'Bob', 'age': 16}, {'name': 'Alice', 'age': 18}, {'name': 'Charlie', 'age': 20}]
```

****

#### 多条件排序

当需要按“多个条件”排序时，可让 `key` 返回**元组**（按元组元素顺序依次作为排序依据）。

> 元组的排序规则：先按第一个元素排，第一个元素相等再比较第二个元素，以此类推

**示例：对元组列表进行排序，按照第一个值的升序，第一个值相同则按照第二个值的降序**

```python
tup = [(3, 5), (1, 2), (2, 4), (3, 1), (1, 3)]

sorted_tup = sorted(tup, key=lambda x: (x[0], -x[1]))  # 排序规则不影响原数据
print(sorted_tup)
# 输出: [(1, 3), (1, 2), (2, 4), (3, 5), (3, 1)]
```

**示例：先按年龄进行排序，年龄相同则按照姓名长度进行排序**

```python
students = [
    {"name": "Bob", "age": 18},
    {"name": "Alice", "age": 18},
    {"name": "Charlie", "age": 20}
]

# key返回元组(age, len(name))：先按age升序，再按name长度升序
sorted_students = sorted(students, key=lambda x: (x["age"], len(x["name"])))
print(sorted_students)

# 输出:
[{'name': 'Bob', 'age': 18}, {'name': 'Alice', 'age': 18}, {'name': 'Charlie', 'age': 20}]
```

### 14. 内置方法`__repr__`

与`__str__`类似，但更强大的打印函数

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        """
        与str功能一致，但是更牛的打印函数
        :return:
        """
        return f"Student(name={self.name}, age={self.age}, score={self.score})"


def sorted_object():
    students = [
        {"name": "Bob", "age": 18, 'score': 66},
        {"name": "Alice", "age": 18, 'score': 62},
        {"name": "Charlie", "age": 20, 'score': 77}
    ]

    # 转换,列表中放对象
    students = [Student(**stu) for stu in students]  # 字典解包操作，将字典的键值对作为关键字参数传入

    print(students)  # 将对象放在列表中仍可以正常打印


if __name__ == '__main__':
    sorted_object()
```

打印结果：

```cmd
[Student(name=Bob, age=18, score=66), Student(name=Alice, age=18, score=62), Student(name=Charlie, age=20, score=77)]
```

将`__repr__`换成`__str__`，打印结果：

```cmd
[<__main__.Student object at 0x0000015D0C05ED20>, <__main__.Student object at 0x0000015D0C05ED50>, <__main__.Student object at 0x0000015D0C05EF30>]
```

