

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

#### **导包并使用的方式：**

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

## <span style='color:red'>Day8</span>

### 1. Jupyter Notebook快捷键

![image-20260215010223249](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215010223496.png)

### 2. Matplotlib

![image-20260215012719567](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215012719849.png)

```python
# 导入模块
import matplotlib.pyplot as plt

# 传入x和y, 通过plot画图
plt.plot([1, 0, 9], [4, 5, 6])

# 在执行程序的时候展示图形
plt.show()
```

![output](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215023610572.png)

#### 2.1 折线图

```python
# 1. 绘制基本的折线图
from matplotlib import pyplot as plt

x = range(1, 8)  # x轴的位置
y = [17, 17, 18, 15, 11, 11, 13]
# 传入x和y, 通过plot画折线图
plt.plot(x, y)
plt.show()
```

![output1](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215023701605.png)

```python
# 2. 折线的颜色和形状设置、折点的样式
"""
color='red' : 折线的颜色
alpha=0.5	: 折线的透明度(0-1) 
linestyle='--' : 折线的样式
linewidth=3		: 折线的宽度—粗细
marker :折点样式
"""
x = range(1, 8)  # x轴的位置
y = [17, 17, 18, 15, 11, 11, 13]
# 传入x和y, 通过plot画折线图
plt.plot(x, y, color='red', alpha=0.3, linestyle='--', linewidth=3, marker='o')
plt.show()
```

![output2](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215023923449.png)

#### 2.2 设置保存图片

```python
from matplotlib import pyplot as plt
import random

x = range(2, 26, 2)  # x轴的位置
y = [random.randint(15, 30) for i in x]

# 设置图片的大小
'''
figsize:指定figure的宽和高，单位为英寸；                                                                     dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80，1英寸等于2.5cm,A4纸是 21*30cm的纸张
'''
# 设置画布对象，figsize中对应的单位是英寸，dpi是每英寸有多少像素点
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)  # 传入x和y, 通过plot画图
#plt.show() 
#  保存(注意：要放在绘制的下面,并且plt.show()会释放figure资源，如果在显示图像之后保存图片将只能保存空图片。)
# plt.savefig('./t1.png') 
#保存矢量图
plt.savefig('./t1.svg')
```

![output3](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215023928103.png)

#### 2.3 设置x轴与y轴刻度

```python
from matplotlib import pyplot as plt

x = range(2, 26, 2)  # x轴的位置
y = [random.randint(15, 30) for i in x]
plt.figure(figsize=(20, 8), dpi=80)

# 设置x轴和y轴刻度的API
# plt.xticks(x)
# plt.xticks(range(1,25)) # 设置x轴的刻度
# plt.yticks(y)
# plt.yticks(range(min(y),max(y)+1))


# 构造x轴刻度标签
x_ticks_label = ["{}:00".format(i) for i in x]
# rotation = 45 # 让字旋转45度
plt.xticks(x, x_ticks_label, rotation=45)
# 设置y轴的刻度标签
y_ticks_label = ["{}℃".format(i) for i in range(min(y), max(y) + 1)]
plt.yticks(range(min(y), max(y) + 1), y_ticks_label)

plt.plot(x, y)
plt.show()
```

![output4](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215024006084.png)

#### 2.4 设置显示中文

```python
from matplotlib import pyplot as plt
from matplotlib import font_manager

x = range(2, 26, 2)  # x轴的位置
y = [random.randint(15, 30) for i in x]
plt.figure(figsize=(20, 8), dpi=80)

# 构造x轴刻度标签
x_ticks_label = ["{}:00".format(i) for i in x]
# rotation = 45 # 让字旋转45度
plt.xticks(x, x_ticks_label, rotation=45)
# 设置y轴的刻度标签
y_ticks_label = ["{}℃".format(i) for i in range(min(y), max(y) + 1)]
plt.yticks(range(min(y), max(y) + 1), y_ticks_label)

# 设置坐标轴标签与字体样式
my_font = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\STSONG.TTF', size=18)
# 下面是mac电脑的
# my_font = font_manager.FontProperties(
#     fname='/System/Library/Fonts/PingFang.ttc',
#     size=18
# )
plt.title('上海天气', fontproperties=my_font)
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度', fontproperties=my_font)

plt.plot(x, y)
plt.show()
```

![output5](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215024037832.png)

#### 2.5 一图多线

```python
from matplotlib import pyplot as plt
from matplotlib import font_manager

y1 = [1, 0, 1, 1, 2, 4, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 4, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
x = range(11, 31)
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y1, color='red', alpha=1, linestyle='-', linewidth=2, label='小王')
plt.plot(x, y2, color='blue', alpha=1, linestyle='-', linewidth=2, label='小张')
# 引入字体
my_font = font_manager.FontProperties(fname='c:\\windows\\fonts\\msyh.ttc', size=16)
# 
# 设置刻度
xtick_labels = ['{}岁'.format(i) for i in x]
plt.xticks(x, xtick_labels, fontproperties=my_font, rotation=45)
# 添加图例
plt.legend(prop=my_font)
plt.grid(alpha=0.4)

plt.show()
```

![output6](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215024110520.png)

#### 2.6 一个画布多个子图

**第一种方式：**

```python
import matplotlib.pyplot as plt
# 引入numpy, 需要先安装numpy的包
import numpy as np

# 设置x的值为1到99
x = np.arange(1, 100)

# 创建父图，设置画布
fig, axes = plt.subplots(2, 2, figsize=(20, 10), dpi=80)
ax1 = axes[0, 0]
ax2 = axes[0, 1]
ax3 = axes[1, 0]
ax4 = axes[1, 1]

# 子图1
ax1.plot(x, x)

# 子图2
ax2.plot(x, -x)

# 子图3
ax3.plot(x, x ** 2)

# 子图4
ax4.plot(x, np.log(x))

plt.show()
```

![output7](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215024139463.png)

**第二种方式：**

```python
# 第二种方式
# 使用 plt.subplot() 添加子图

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 100)
plt.figure(figsize=(20, 10), dpi=80)
# 创建子图
# 2,2,1 ==> 两行两列，放在第一个位置
plt.subplot(2, 2, 1)
plt.plot(x, x)

plt.subplot(2, 2, 2)
plt.plot(x, -x)

plt.subplot(2, 2, 3)
plt.plot(x, x ** 2)

plt.subplot(2, 2, 4)
plt.plot(x, np.log(x))

plt.show()
```

![output8](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215024221584.png)

#### 2.7 散点图

```python
'''
题干:3月份每天最高气温
a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
'''

from matplotlib import pyplot as plt
from matplotlib import font_manager

y = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22,
     23]
x = range(1, 32)

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 使用scatter绘制散点图
plt.scatter(x, y, label='3月份')

# 调整x轴的刻度
my_font = font_manager.FontProperties(fname='c:\\windows\\fonts\\msyh.ttc', size=16)

xticks_labels = ['3月{}日'.format(i) for i in x]
plt.xticks(x[::3], xticks_labels[::3], fontproperties=my_font, rotation=45)

# 设置坐标轴标签
plt.xlabel(' 日 期 ', fontproperties=my_font)
plt.ylabel('温度', fontproperties=my_font)
# 设置图例
plt.legend(prop=my_font)

plt.show()
```

![output9](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215024252745.png)

#### 2.8 柱状图

```python
import matplotlib.pyplot as plt
from matplotlib import font_manager

a = ['流浪地球', '疯狂的外星人', '飞驰人生', '大黄蜂', '熊出没·原始时代', '新喜剧之王']
b = [38.13, 19.85, 14.89, 11.36, 6.47, 5.93]

# 引入字体
my_font = font_manager.FontProperties(fname='c:\\windows\\fonts\\msyh.ttc', size=16)

# 绘制画布
plt.figure(figsize=(20, 8), dpi=80)

# 绘制条形图
rects = plt.bar(range(len(b)), b, width=0.3, color='r')

# 绘制x轴标签
plt.xticks(range(len(a)), a, fontproperties=my_font, rotation=45)

# 给条形图添加标签
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 0.3, str(height), ha='center')

plt.show()
```

![output10](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215024316460.png)

#### 2.9 直方图

```python
time = [131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130,
        124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 136, 126, 134, 95, 138, 117, 111, 78, 132, 124, 113, 150, 110,
        117, 86, 95, 144, 105, 126, 130, 126, 130, 126, 116, 123, 106, 112, 138, 123, 86, 101, 99, 136, 123, 117, 119,
        105, 137, 123, 128, 125, 104, 109, 134, 125, 127, 105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120,
        114, 105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134, 156, 106, 117, 127, 144, 139, 139, 119,
        140, 83, 110, 102, 123, 107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133, 112, 114, 122, 109,
        106, 123, 116, 131, 127, 115, 118, 112, 135, 115, 146, 137, 116, 103, 144, 83, 123, 111, 110, 111, 100, 154,
        136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141, 120, 117, 106, 149, 122, 122, 110, 118, 127,
        121, 114, 125, 126, 114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137, 92, 121, 112, 146, 97, 137, 105,
        98, 117, 112, 81, 97, 139, 113, 134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110, 105, 129, 137,
        112, 120, 113, 133, 112, 83, 94, 146, 133, 101, 131, 116, 111, 84, 137, 115, 122, 106, 144, 109, 123, 116, 111,
        111, 133, 150]

import matplotlib.pyplot as plt

# 画布
plt.figure(figsize=(20, 8), dpi=80)

print((max(time) - min(time)) / 20)
# 绘制直方图
# bins=20 表示将数据分为20个区间，也就是20组，当然，这个数据也可以计算出来
plt.hist(time, bins=20, color='green')

# 添加x轴标签
plt.xlabel('播放时长', fontproperties=my_font)
# 添加y轴标签
plt.ylabel('电影数目', fontproperties=my_font)

# 修改x轴刻度显示
plt.xticks(range(min(time), max(time) + 1, 4), [str(i) + '分钟' for i in range(min(time), max(time) + 1, 4)],
           fontproperties=my_font, rotation=45)

plt.show()
```

![output11](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215024353935.png)

#### 2.10 饼状图

```python
"""
参数解释:
    explode： 设置各部分突出多少
    label: 设置各部分标签
    labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
    autopct：设置圆内文本
    shadow：设置是否有阴影
    startangle：起始角度，默认从0开始逆时针转
    pctdistance：设置圆内文本距圆心距离返回值
"""

import matplotlib.pyplot as plt
import matplotlib

label_list = ["第一部分", "第二部分", "第三部分"]  # 各部分标签
size = [55, 35, 10]  # 各部分大小
color = ["red", "green", "blue"]  # 各部分颜色
explode = [0, 0.05, 0]  # 各部分突出值

#设置汉字显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1, autopct="%1.1f%%", shadow=True,
        startangle=90, pctdistance=0.6)

plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
plt.show()
```

![output12](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260215024412225.png)

### 3. format()方法

**语法：=="字{}符{}串".format(参数1, 参数2)==**

将参数按位置填到`{}`中

可使用元组：

```python
data = (5, 10)
"现在时间是：{}:{}".format(*data)  # 对元组进行拆包传参
```

## <span style='color:red'>Day9</span>

### 1. Junyter 中写在单元格最后一行的内容会直接输出，无需使用`print()`

### 2. time.time()

``` python
import time
time.time()  # 获得当前时间戳，单位：秒，1970年1月1日0时0分0秒至今的时间
```

### 3. zip()

zip的功能是创建一个迭代器，迭代器中包含两个列表的元素，两个列表的元素一一对应

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

for a, b in zip(list1, list2):  # 将list1和list2组合在一起
    print(a, b)
"""
输出结果：
1 4
2 5
3 6
"""
    
print(list(zip(list1, list2)))
"""
输出结果：
[(1, 4), (2, 5), (3, 6)]
"""
```

### 4. Numpy核心：ndarray数组

> ndarray数组中的所有元素必须是相同类型
>
> python列表中可以同时存放不同类型的元素

#### 4.1 创建

**使用列表创建**

创建语法：==`np.array(列表对象)`==

```python
import numpy as np

# 创建一个一维ndarray
arr1 = np.array([1, 2, 3])

print(arr1)
print(type(arr1))

# 创建一个二维ndarray
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(type(arr2))

# 创建一个三维ndarray
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)
print(type(arr3))
```

> 最外侧的方括号是0轴，往内依次是1、2、...轴

****

**使用函数创建特殊数组**

```python
print(np.zeros((2)))  # 创建一个2行3列全0数组
print(np.ones((2, 3)))  # 创建一个2行3列全1数组
print(np.full((2, 3), 10))  # 创建一个2行3列全10数组
print(np.eye(3))  # 创建一个3行3列单位矩阵
print(np.empty((2, 3)))  # 创建一个2行3列空数组
```

> 注意：默认创建的数组中的数据类型(dtype)都是: float64

****

**arrange创建一维数组**

arrange() 类似 python 的 range()，用于创建一个一维 ndarray 数组。

```python
# 创建一个一维数组，起始值0，结束值10，步长2，元素类型: float32
# 左闭右开
arr4 = np.arange(0, 10, 2, dtype=np.float32)

# 数组
# [0., 2., 4., 6., 8.]
```

****

**matrix创建二维数组**

matrix是ndarray的子类，只能生成2维的矩阵

```python
arr4 = np.matrix([[1, 2, 3], [4, 5, 6]])

# 注意，只能创建二维矩阵
# 会报错 ValueError: matrix must be 2-dimensional
# arr5 = np.matrix([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]])
```

****

**创建随机数矩阵**

```python
import numpy as np

# 1. 创建一个0-1的【随机数】矩阵，矩阵是2行3列
arr5 = np.random.random((2,3))
print(arr5)
print(type(arr5))

# 2. 创建一个0-10的【随机整数】矩阵，矩阵是2行3列
arr6 = np.random.randint(0, 10, (2,3))
print(arr6)
print(type(arr6))

# 3. 创建一个0-10的随机浮点数矩阵，矩阵是2行3列，是【均匀分布】
arr7 = np.random.uniform(0, 10, (2,3))
print(arr7)
print(type(arr7))
```

#### 4.2 属性

```python
# 创建一个2行3列的矩阵，
arr8 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr8.shape)    # 形状（行数，列数）→ (2, 3)
print(arr8.ndim)    # 维度 → 2（二维数组）
print(arr8.dtype)    # 数据类型 → int64（默认）
print(arr8.size)    # 总元素数 → 6
```

```python
# 创建一个3维数组
arr9 = np.arange(24).reshape(2, 3, 4)

print(arr9)
'''
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]
'''

print(arr9.shape) # 形状（0轴,1轴，2轴）-> (2, 3, 4)
print(arr9.ndim)  # 3
print(arr9.dtype)  # int32
print(arr9.size)  # 24
```

### 5. Numpy基本操作

#### 5.1 形状改变

`reshape()`, 改变ndarray的形状

```python
# 一维变多维
arr9 = np.arange(0, 12)
arr10 = arr9.reshape(3,4)

# 说明: 不改变原有矩阵，返回改变之后的新矩阵
print(arr9)  #  [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(arr10)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
```

```python
# 默认情况下‘C’以行为主的顺序展开，‘F’（Fortran风格）意味着以列的顺序展开,不重要，用不上
arr15 = arr10.reshape((12,),order='F')
print(arr15)  # [ 0  4  8  1  5  9  2  6 10  3  7 11]
```

```python
arr11=arr10+2
print(arr11)
'''
[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]]
'''

arr12=arr11.reshape(12)  #再变回一维，元素位置不变
print(arr12)  # [ 2  3  4  5  6  7  8  9 10 11 12 13]
```

#### 5.2 类型转换`astype()`

```python
  # [1. 2. 3. 4. 5. 6.]arr12 = np.array([1, 2, 3, 4, 5, 6])
print(arr12.dtype)  # int32
print(arr12)  # [1 2 3 4 5 6]

# astype(), 转换ndarray的类型
arr13 = arr12.astype(np.float32)		# 转为浮点型 → [1. 2. 3. 4. 5. 6.]
print(arr13.dtype)  # float32
print(arr13)  # [1. 2. 3. 4. 5. 6.]
```

#### 5.3 索引与切片

```python
# 1. 列表的索引与切片
# list[start:end:step]
arr = [1, 2, 3, 4, 5, 6]
print(arr[0:4:2])           # [1, 3]

# 2. 一维ndarray的索引与切片， 和列表的索引与切片一样
arr14 = np.arange(0, 12)
print(arr14[0:4:2])         # [0,2]

print('-'*50)

# 3. 多维ndarray的索引与切片
arr15 = np.arange(0, 12).reshape(3,4)
print(arr15)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# 取一行(下标为1的一行, 也就是第二行)
print(arr15[1,:])  # [4 5 6 7]

# 取一列(下标为1的一列, 也就是第二列)
print(arr15[:,1])  # [1 5 9]

# 取不连续的多行
print(arr15[[0,2],:])
'''
[[ 0  1  2  3]
 [ 8  9 10 11]]
'''

# 取从第2行开始的所有行
print(arr15[1:,:])
'''
[[ 4  5  6  7]
 [ 8  9 10 11]]
'''
```

#### 5.4 元素访问与修改

```python
# 元素访问
import numpy as np
arr15 = np.arange(0, 12).reshape(3,4)
print(arr15)
arr15[[1,2],[0,3]]
```

> `[[ 0  1  2  3]
>  [ 4  5  6  7]
>  [ 8  9 10 11]]`
>
> `array([ 4, 11])`

```python
arr15 = np.arange(0, 12).reshape(3,4)
arr15>5
```

> `array([[False, False, False, False],
>        [False, False,  True,  True],
>        [ True,  True,  True,  True]])`

```python
# 元素修改
arr15 = np.arange(0, 12).reshape(3,4)
print(arr15)

# 修改单个值
arr15[1,1] = 100
print(arr15)

print('-'*50)
arr15 = np.arange(0, 12).reshape(3,4)

# 修改某一行的值
arr15[1,:] = 100
print(arr15)

print('-'*50)
arr15 = np.arange(0, 12).reshape(3,4)

# 修改某一列的值
arr15[:,1] = 100
print(arr15)

print('-'*50)
arr15 = np.arange(0, 12).reshape(3,4)

# 修改某一个块的值
arr15[0:2,0:2] = 100
print(arr15)

print('-'*50)
arr15 = np.arange(0, 12).reshape(3,4)

# 修改多个不相邻的点 (0,0) (1,1) (2,3)
arr15[[0,1,2],[0,1,3]] = 99
print(arr15)

print('-'*50)
arr15 = np.arange(0, 12).reshape(3,4)

# 根据条件修改
arr15[arr15>5] = 0
print(arr15)
'''
[[0 1 2 3]
 [4 5 0 0]
 [0 0 0 0]]
'''

print('-'*50)

# 三目运算
result = np.where(arr15>0,10,20)
print(result)
'''
[[20 10 10 10]
 [10 10 20 20]
 [20 20 20 20]]
'''
```

### 6. Numpy矢量运算：矩阵的运算（数组）

**广播机制**

由于numpy的广播机制，在运算过程中，ndarray数组加减乘除的值被广播到所有元素上

例如：arr1 是一个 ndarray 数组，`arr1 + 10` 会令 arr1 中所有元素加10

```python
arr16 = np.arange(0, 12).reshape(3,4)
print(arr16)
print('-' * 20)
print(arr16 + 10) # 加法，有广播机制，每一个元素都加上10
print('-'*20)
print(arr16 - 5)
print('-'*20)
print(arr16 * 2)
print('-'*20)
print(arr16 / 2)
```

****

**同种形状的矩阵运算，运算结果是按位进行加减乘除运算**

```python
arr17 = np.arange(10, 22).reshape(3,4)
print(arr17)
arr18 = np.arange(1, 13).reshape(3,4)
print(arr18)

# 加法
print('-'*50)
print(arr17 + arr18)
# 减法
print('-'*50)
print(arr17 - arr18)
# 乘法
print('-'*50)
print(arr17 * arr18)
# 除法
print('-'*50)
print(arr17 / arr18)
```

****

**不同形状的矩阵，不能计算**

```python
arr19 = np.arange(0, 12).reshape(3,4)
arr20 = np.arange(0, 4).reshape(2,2)

# 报错: ValueError: operands could not be broadcast together with shapes (3,4) (2,2)
# print(arr19 + arr20)
```

****

**行数或者是列数相同的一维数组和多维数组之间可以进行计算（广播特性）**

```python
# 列数相同（行形状相同）
arr21 = np.arange(0, 12).reshape(3,4)       # 3行4列
print(arr21)
arr22 = np.arange(0, 4).reshape(1,4)                
print(arr22)

# 依然是广播的特性
print(arr22-arr21)
```

> `[[ 0  1  2  3]
>  [ 4  5  6  7]
>  [ 8  9 10 11]]`
>
> `[[0 1 2 3]]`
>
> `[[ 0  0  0  0]
>  [-4 -4 -4 -4]
>  [-8 -8 -8 -8]]`

```python
# 行数相同（列形状相同）
arr23 = np.arange(0, 12).reshape(3,4)
print(arr23)
arr24 = np.arange(0, 3).reshape(3,1)
print(arr24)
# 依然是广播的特性
print(arr23-arr24)
```

> `[[ 0  1  2  3]
>  [ 4  5  6  7]
>  [ 8  9 10 11]]`
>
> `[[0]
>  [1]
>  [2]]`
>
> `[[0 1 2 3]
>  [3 4 5 6]
>  [6 7 8 9]]`

****

**有一个以上维度值相同的三维数组相加**

```python
arr25 = np.arange(0, 24).reshape(2,3,4)
arr26 = np.arange(0, 8).reshape(2,1,4)
result=arr25+arr26
print(result.shape)  # (2, 3, 4)

arr25 = np.arange(0, 24).reshape(2,3,4)
arr26 = np.arange(0, 2).reshape(2,1,1)
result=arr25+arr26
print(result.shape)  # (2, 3, 4)

arr25 = np.arange(0, 6).reshape(2,3,1)
arr26 = np.arange(0, 8).reshape(2,1,4)
result=arr25+arr26
print(result.shape)  # (2, 3, 4)
```

### 7. Numpy 统计函数

按哪一个轴进行运算，对应的轴就会发生改变

#### 7.1 求和

```python
import numpy as np
arr25 = np.arange(1, 13).reshape(3, 4)
print(arr25)

# 求所有数据的和
print(arr25.sum())

# 按轴求和
# axis = 0, 表示按列求和
print(arr25.sum(axis=0))

# axis=1, 表示按行求和
print(arr25.sum(axis=1))
```

#### 7.2 求平均值

```python
arr25 = np.arange(1, 13).reshape(3, 4)
print(arr25)
# 1. 求所有数的平均值
print(arr25.mean())

# 2. 按轴求平均值
# axis = 0, 按列求平均值
print(arr25.mean(axis=0))
```

#### 7.3 求最大值

```python
arr25 = np.arange(1, 13).reshape(3, 4)
print(arr25)

# 1. 求所有数的最大值
print(arr25.max())

# 2. 按轴求最大值
# axis = 0, 按列求最大值
print(arr25.max(axis=0))
```

#### 7.4 求最小值

```python
arr25 = np.arange(1, 13).reshape(3, 4)
print(arr25)

# 1. 求所有数的最小值
print(arr25.min())

# 2. 按轴求最小值
# axis = 1，按行求最小值
print(arr25.min(axis=1))
```

#### 7.5 求前缀和

即当前数与当前数之前的所有数的和

eg：1, 2, 3, 4, 5, 6

​	5的前缀和是 1+2+3+4+5 = 15

```python
arr25 = np.arange(1, 13).reshape(3, 4)
print(arr25)

# 1. 求所有数的前缀和，不写轴会被展平，就是变为1维
print(arr25.cumsum())

# 2. 按轴求前缀和
# axis = 1, 按行求前缀和
print(arr25.cumsum(axis=1))
```

#### 7.6 求最小值索引

```python
arr25 = np.random.randint(0, 100, (3, 4))
print(arr25)

# 1. 求所有数的最小值索引（展开成一维后最小值的下标）
print(arr25.argmin())
# 2. 按轴求最小值索引
# axis = 1, 按行求最小值索引（本行最小值的下标）
print(arr25.argmin(axis=1))
```

#### 7.7 求标准差

标准差是一组数据平均值分散程度的一种度量。

- 如果标准差较大，那么代表大部分数值和其平均值之间的差异较大
- 如果标准差较小，那么代表大部分数值和其平均值之间的差异较小

标准差越大，代表数据波动越大，越不稳定；标准差越小，代表数据波动小，越稳定。

```python
arr25 = np.arange(1, 13).reshape(3, 4)
print(arr25)

# 1. 求所有数的标准差
print(arr25.std())

# 2. 按轴求标准差
# axis = 1, 按行求标准差
print(arr25.std(axis=1))
```

#### 7.8 求极值（最大值与最小值的差）

```python
arr25 = np.arange(1, 13).reshape(3, 4)
print(arr25)

# 1. 求所有数的极值
print(np.ptp(arr25))

# 2. 按轴求极值
# axis = 1，按行求极值
print(np.ptp(arr25, axis=1))
```

### 8. Numpy的其他操作

#### 8.1 数组的添加

基本语法：==`np.append(数组, 待添加的元素, [指定轴])`==

```python
arr27 = np.array([[1,2,3],[4,5,6]])
print(arr27)

# 数组的添加
# 1. 默认情况下，展开为一维数组再添加
arr28 = np.append(arr27, np.array([7,8,9]))
print(arr28)

# 2. 指定轴添加
# axis = 0, 沿着0轴添加元素
arr29 = np.append(arr27, np.array([[7,8,9]]), axis=0)
print(arr29)

# axis=1, 沿着1轴添加元素
arr30 = np.append(arr27, np.array([[7],[8]]), axis=1)
print(arr30)
```

> `[[1 2 3]
>  [4 5 6]]`
>
> `[1 2 3 4 5 6 7 8 9]`
>
> `[[1 2 3]
>  [4 5 6]
>  [7 8 9]]`
>
> `[[1 2 3 7]
>  [4 5 6 8]]`

#### 8.2 数组的插入

基本语法：==`np.insert(数组, 索引, 元素, [指定轴])`==

```python
arr28 = np.array([[1,2,3],[4,5,6]])
print(arr28)

# 数组的插入
# 1. 默认情况下，展开为一维数组再插入
# 2. 插入的元素必须和数组的元素形状相同

# 2表示位置2
# 7表示插入7
arr29 = np.insert(arr28, 2, 7)
print(arr29)

# 指定轴插入
# axis = 0，沿着0轴插入元素
# 索引0，表示插入第一行
arr30 = np.insert(arr28, 0, np.array([[7,8,9]]), axis=0)
print(arr30)
```

#### 8.3 数组的删除

基本语法：==`np.delete(数组, 下标, [指定轴])`==

```python
# 数组的删除
arr28 = np.array([[1,2,3],[4,5,6]])
print(arr28)

# 1. 默认情况下，展开为一维数组再删除, 2表示删除索引为2的元素
arr31 = np.delete(arr28, 2)
print(arr31)

# 2. 指定轴删除
# axis = 0, 沿着0轴删除元素
# 0表示删除索引为0的元素, 也就是删除第一行
arr32 = np.delete(arr28, 0, axis=0)
print(arr32)
```

> `[[1 2 3]
>  [4 5 6]]`
>
> `[1 2 4 5 6]`
>
> `[[4 5 6]]`

#### 8.4 数组的去重

基本语法：==`np.unique(数组, [指定轴])`==

```python
# 数组的去重
arr29 = np.array([1,2,3,4,5,5,5,6,7,8,9,9]).reshape(3,4)
print(arr29)

# 1. 直接去重
# 默认情况下，展开一维数组再去重，得到的也是一维数组
arr30 = np.unique(arr29)
print(arr30)

# 2. 按轴去重
# axis = 0, 沿着0轴去重
# 添加一行重复数据
arr31 = np.append(arr29, np.array([[1,2,3,4]]), axis=0)
print(arr31)

# 去重，去除重复数据
arr32 = np.unique(arr31, axis=0)
print(arr32)
```

> `[[1 2 3 4]
>  [5 5 5 6]
>  [7 8 9 9]]`
>
> `[1 2 3 4 5 6 7 8 9]`
>
> `[[1 2 3 4]
>  [5 5 5 6]
>  [7 8 9 9]
>  [1 2 3 4]]`
>
> `[[1 2 3 4]
>  [5 5 5 6]
>  [7 8 9 9]]`

#### 8.5 数组的拼接、堆叠与分割

**数组的拼接`concatenate()`**

```python
# 数组的拼接，非拼接轴，对应的size必须一致  不会增加维度
arr33 = np.array([[1,2,3],[4,5,6]])
arr34 = np.array([[7,8,9],[10,11,12]])

# 默认情况下，沿着轴0进行拼接
arr35 = np.concatenate((arr33, arr34))
print(arr35)

# 指定轴了之后，按轴1拼接
print(np.concatenate((arr33, arr34), axis=1))
```

> `[[ 1  2  3]
>  [ 4  5  6]
>  [ 7  8  9]
>  [10 11 12]]`
>  
> `[[ 1  2  3  7  8  9]
> [ 4  5  6 10 11 12]]`

****

**数组的堆叠`stack()`**

按哪个轴堆叠，就会增加一个维度，对应维度的size是数组的个数

```python
import numpy as np
a = np.array([1, 2, 3])  # shape: (3,)
b = np.array([4, 5, 6])  # shape: (3,)
c= np.array([7, 8, 9])
# axis = 0，沿着0轴进行堆叠
print(np.stack([a, b, c], axis=0))
```

> `array([[1, 2, 3],
>        [4, 5, 6],
>        [7, 8, 9]])`

```python
print(np.stack([a, b], axis=-1))
```

> `[[1 4]
>  [2 5]
>  [3 6]]`

```python
# 二维数组的堆叠
a = np.arange(12).reshape(3, 4)
b = np.arange(12,24).reshape(3, 4)


# axis = 0，沿着0轴进行堆叠, （新轴在第0位，长度=2）
np.stack([a, b], axis=0).shape
```

> `(2, 3, 4)`

```python
np.stack([a, b], axis=1).shape
```

> `(3, 2, 4)`

```python
np.stack([a, b], axis=2).shape
```

> `(3, 4, 2)`

****

**数组的分割`split()`**

```python
arr36 = np.arange(1, 10).reshape(3, 3)
print(arr36)

# 1. 默认情况下，按轴0进行分割
# 3表示分割成3份
arr37 = np.split(arr36, 3)
print(arr37)
print(type(arr37))

# 2. 按轴1进行分割
arr38 = np.split(arr36, 3, axis=1)
print(arr38)
```

> 输出结果：
>
> `[[1 2 3]
> [4 5 6]
> [7 8 9]]`
>
> `[array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]`
>
> `<class 'list'>`
>
> `[array([[1],
>     [4],
>     [7]]), 
> array([[2],
>     [5],
>     [8]]), 
> array([[3],
>     [6],
>     [9]])]`

#### 8.6 数组的转置与轴滚动

```python
arr39 = np.arange(0, 12).reshape(3, 4)
print("原始数组:")
print(arr39)

# 1. 转置第一种方式
arr40 = arr39.T
print("转置第一种方式:")
print(arr40)

# 2. 转置第二种方式
arr41 = np.transpose(arr39)
print("转置第二种方式:")
print(arr41)

# 3. 对换数组的轴
arr42 = np.transpose(arr39)
print("对换轴:")
print(arr42)
```

> 输出结果：
>
> `原始数组:
> [[ 0  1  2  3]
> [ 4  5  6  7]
> [ 8  9 10 11]]
> 转置第一种方式:
> [[ 0  4  8]
> [ 1  5  9]
> [ 2  6 10]
> [ 3  7 11]]
> 转置第二种方式:
> [[ 0  4  8]
> [ 1  5  9]
> [ 2  6 10]
> [ 3  7 11]]
> 对换轴:
> [[ 0  4  8]
> [ 1  5  9]
> [ 2  6 10]
> [ 3  7 11]]`

```python
# 4. 轴滚动
arr39 = np.arange(0, 12).reshape(3, 4)
print("原始数组:")
print(arr39)

# 表示把1轴滚动到0轴的位置
arr43 = np.rollaxis(arr39, 1, 0)
print("轴滚动:")
print(arr43.shape)

# 轴滚动第二个案例
arr44 = np.ones((3, 4, 5, 6))
print(arr44.shape)

# 表示把3轴滚动到1轴的位置
arr45 = np.rollaxis(arr44, 3, 1)
print(arr45.shape)
```

> 输出结果：
>
> `原始数组:
> [[ 0  1  2  3]
> [ 4  5  6  7]
> [ 8  9 10 11]]`
>
> `轴滚动:
> (4, 3)`
>
> `(3, 4, 5, 6)`
>
> `(3, 6, 4, 5)`

#### 8.7 读取文件数据

从文件中读取数据的API：==`np.loadtxt()`==

只能读 .csv 或 .txt 文件

`np.loadtxt(fname, dtype=float, delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)`

- fname: 文件名
- dtype: 数据类型
- delimiter: 分隔符，默认为None，表示使用空格进行分隔
- converters: 转换函数，默认为None，表示没有转换函数
- skiprows: 跳过行数，默认为0，表示没有跳过行
- usecols: 使用列数，默认为None，表示使用所有列
- unpack: 是否将数据进行解包，默认为False，表示不进行解包，也就是有多少条记录，就返回多少个数组
- ndmin: 最小维度，默认为0，表示没有最小维度

#### 8.8 数组中的特殊值

numpy中的特殊值：

- nan: not a number, 通常表示确实的数据
- inf: 表示正无穷大
- -inf: 表示负无穷大

```python
import numpy as np

# 创建一个nan和inf #
a = np.nan
b = np.inf
c = -np.inf
print(a, type(a))
print(b, type(b))
print(b > c)
```

> 输出结果：
>
> `nan <class 'float'>`
>
> `inf <class 'float'>`
>
> `True`

```python
np.inf==np.inf  # 正无穷与正无穷相等

np.nan== np.nan  # 非数与非数不相等
```

> 输出结果：
>
> `True`
>
> `False`

```python
t = np.arange(24, dtype=float).reshape(4, 6)

# 将三行四列的数改成nan
t[3, 4] = np.nan
print(t)

# 可以使用np.count_nonzero() 来判断非零的个数
print(np.count_nonzero(t))

# 并且 np.nan != np.nan     结果 是TRUE
# 所以我们可以使用这两个结合使用判断nan（缺失值）的个数
print(np.count_nonzero(t != t))  # 只有nan是Ture，其余都是False

# 将nan替换为0
t[np.isnan(t)] = 0
print(t)
```

> 输出结果：
>
> `[[ 0.  1.  2.  3.  4.  5.]
> [ 6.  7.  8.  9. 10. 11.]
> [12. 13. 14. 15. 16. 17.]
> [18. 19. 20. 21. nan 23.]]`
> `23`
> `1`
> `[[ 0.  1.  2.  3.  4.  5.]
> [ 6.  7.  8.  9. 10. 11.]
> [12. 13. 14. 15. 16. 17.]
> [18. 19. 20. 21.  0. 23.]]`

### 9. Pandas 核心数据结构

#### 9.1 Series：带标签的一维数组

Series 对象由“索引（index）”和“数据（values）”两个列表构成，索引默认从 **0** 开始递增。

**创建**主要有以下两种方式：

- 通过**列表**创建（可以手动指定索引，也可以不指定索引）
- 通过**字典**创建（key是索引，value是值）

```python
import pandas as pd

# Series的定义
# 1. 列表创建，默认索引
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

print('-'*50)
# 2. 列表创建，自定义索引
s2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'c', 'e'])
print(s2)

print('-'*50)
# 3. 字典创建(key是索引，value是值)
s3 = pd.Series({"Alice":85, "Bob":90, "Charlie":78, "David":92})
print(s3)
```

> 输出结果：
>
> `0    10
> 1    20
> 2    30
> 3    40
> 4    50
> dtype: int64`
> `--------------------------------------------------`
> `a    10
> b    20
> c    30
> c    40
> e    50
> dtype: int64`
> `--------------------------------------------------`
> `Alice      85
> Bob        90
> Charlie    78
> David      92
> dtype: int64`

核心**属性**有：

- `index`: 索引
- `values`: 数据
- `dtype`: 数据类型
- `shape`: 形状

```python
s3 = pd.Series({"Alice":85, "Bob":90, "Charlie":78, "David":92})


print(s3.index)   # 索引 → Index(['Alice', 'Bob', 'Charlie', 'David'], dtype='object')
print(s3.values)  # 数据 → [85 90 78 92]
print(s3.dtype)   # 数据类型 → int64
print(s3.shape)   # 形状（长度）→ (4,)
```

**基本操作：**

```python
# 通过索引获取值,官方不建议这么使用
s3 = pd.Series({"Alice":85, "Bob":90, "Charlie":78, "David":92})
print(s3["Alice"])
print(s3["Bob"])

# 通过索引修改值
s3["Bob"] = 100
print(s3)
```

> 输出结果：
>
> `85`
> `90`
> `Alice       85
> Bob        100
> Charlie     78
> David       92
> dtype: int64`

****

**索引操作**

Series中的取值有两种方式：

1 根据索引的名字取值

- 可以直接 `对象名[索引名]` 来取值
- 建议使用 `对象名.loc[索引名]` 来取值

2 根据索引的位置取值

- 可以直接使用 `对象名[位置值]` 来取值
- 建议使用 `对象名.iloc[位置值]` 来取值

3 支持使用切片的方式来取值



1. index指定索引的名称

```python
import pandas as pd
import numpy as np

# s = pd.Series(['A','B','C','D'],index=['001','002','003','004'])

# 创建一个Series
s=pd.Series(['A','B','C','D'])

# 1. Index指定索引的名称
s.index = [1,2,3,4]
print(s)
```

2. 根据索引名取值

```python
s2 = pd.Series(['A','B','C','D'],index=['001','002','003','004'])

# 通过索引名取值
print(s2['002'])          # B
print(s2.loc['002'])      # B     #推荐的方式
```

3. 根据位置取值

```python
s2 = pd.Series(['A','B','C','D'],index=['001','002','003','004'])

# 通过位置取值
# print(s2[1])            # FutureWarning: 已被废弃
print(s2.iloc[1])         # 推荐的方式
```

4. 取多个值

```python
# 3. 通过多个索引取多个值
# print(s2[['002','004']])
# print('-'*20)

print(s2.loc[['002','004']])
print('-'*20)

# print(s2[[1,3]])

print(s2.iloc[[1,3]])
print('-'*30)
```

5. 根据切片取值

```python
print(s2.loc['002':'004'])        # 通过索引名取值是【左闭右闭】
print('-'*20)
print(s2.iloc[0:2])               # 通过索引位置取值是【左闭右开】
```

#### 9.2 DataFrame

DataFrame可以理解为是：带标签的二维表格。

DataFrame 类似 Excel 表格，由“行索引（index）”、“列名（columns）”和“数据（values）”组成，是 Pandas 最常用的数据结构。

![image-20260225155016654](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260225155016849.png)

DataFrame本质其实就是二维数组（ndarray），**创建方式**有两种：

- 通过**字典**创建（键为列名，值为列数据，行索引可以自定义，也可以默认）
- 通过**二维的ndarray**创建

```python
import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [20, 22, 21, 20],
    "score": [85, 90, 78, 92],
    "gender": ["女", "男", "男", "男"]
}

# 1. 字典创建（字典键为列名，值为列数据）
df = pd.DataFrame(data)
print(df)
```

> 输出结果：
>
> `      name  age  score gender
> 0    Alice   20     85      女
> 1      Bob   22     90      男
> 2  Charlie   21     78      男
> 3    David   20     92      男`

```python
# 2. 自定义行索引
df = pd.DataFrame(data,index=['s1', 's2', 's3', 's4'])
print(df)
```

> 输出结果：
>
> `       name  age  score gender
> s1    Alice   20     85      女
> s2      Bob   22     90      男
> s3  Charlie   21     78      男
> s4    David   20     92      男`

```python
# 3. 通过ndarray构建Datafrane
arr1 = np.arange(12).reshape(3,4)
df2 = pd.DataFrame(arr1,index=['a', 'b', 'c'],columns=['A', 'B', 'C', 'D'])
print(df2)
```

> 输出结果：
>
> `   A  B   C   D
> a  0  1   2   3
> b  4  5   6   7
> c  8  9  10  11`

```python
# 注意: 依然具有广播的特性
data2 = {
    "name":['zs','ls','ww'],
    "gender":"男",
    "height":[180,180,190]
}
df2 = pd.DataFrame(data2)
df2
```

> 输出结果：
>
> `   name  gender  height
> 0   zs      男     180
> 1   ls      男     180
> 2   ww      男     190`

**核心属性**有：

- `index`: 行索引
- `columns`: 列索引（列名）
- `values`: 数据
- `shape`: 形状
- `info`: 整体概览

```python
import pandas as pd
import numpy as np

# 1. 创建一个DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [20, 22, 21, 20],
    "score": [85, 90, 78, 92],
    "gender": ["女", "男", "男", "男"]
}

df = pd.DataFrame(data)

# 2. 输出核心属性
# 行索引
print(df.index)     # 输出: RangeIndex(start=0, stop=4, step=1)

# 列索引
print(df.columns)   # 输出: Index(['name', 'age', 'score', 'gender'], dtype='object')

# 数据
print(df.values)    # 输出: [['Alice' 20 85 '女'] ['Bob' 22 90 '男'] ['Charlie' 21 78 '男'] ['David' 20 92 '男']]
print(type(df.values))  # 输出: <class 'numpy.ndarray'>

# 形状
print(df.shape)     # 输出: (4, 4)

# 数据概览
print(df.info())    # 输出包括: 类型、行索引、列索引、数据、数据类型、内存占用等
```

**基本操作：**

```python
dict = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [20, 22, 21, 20],
    "score": [85, 90, 78, 92],
    "gender": ["女", "男", "男", "男"]
}
df = pd.DataFrame(dict)

# 1. 获取前几行数据
print(df.head(2))
print('-'*20)

# 2. 获取后几行数据
print(df.tail(1))
print('-'*20)

# 3. 获取指定列的数据
name_data = df["name"]
print(name_data)
print(type(name_data))      # 单列数据是 Series
print('-'*20)

# 4. 获取指定多列的数据
age_data = df[["age", "gender"]]
print(age_data)
print(type(age_data))       # 多列数据是 DataFrame
print('-'*20)

# 5. 增加列
df["new_column"] = [1, 2, 3, 4]
print(df)
df["new_column2"] = df["new_column"] + 20
print(df)
print('-'*20)

# 6. 删除列
del df["new_column"]
print(df)
```

****

**索引操作**

DataFrame的索引，分为行索引和列索引，每一列都构成了一个Series对象。

![image-20260225162847247](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260225162847438.png)

索引取值方式：

1. `df.loc[]`：根据索引名来取值，如果是切片，**左闭右闭**
2. `df.iloc[]`：根据索引的位置来取值，如果是切片，**左闭右开**
3. 在DataFrame中，`df.loc()` 和 `df.iloc()` 默认都是取**行数据**

```python
df = pd.DataFrame(np.arange(12).reshape(3,4),index=['s1','s2','s3'],columns=['c1','c2','c3','c4'])
print("原始数据:")
print(df)

# 1. 通过列索引获取值
print("通过列索引获取值:")
print(df['c2'])

# 2. 通过多个列索引获取多个列的值
print("通过多个列索引获取多个列的值")
print(df[['c2','c4']])

# 3. 通过行索引获取行数据
print("通过行索引获取行数据:")
print(df.loc['s2'])

# 4. 通过多个行索引获取多个行数据
print("通过多个行索引获取多个行数据:")
print(df.loc[['s1','s3']])
```

> 输出结果：
>
> `原始数据:
>  c1  c2  c3  c4
> s1   0   1   2   3
> s2   4   5   6   7
> s3   8   9  10  11`
>
> `通过列索引获取值:
> s1    1
> s2    5
> s3    9
> Name: c2, dtype: int64`
>
> `通过多个列索引获取多个列的值
>  c2  c4
> s1   1   3
> s2   5   7
> s3   9  11`
>
> `通过行索引获取行数据:
> c1    4
> c2    5
> c3    6
> c4    7
> Name: s2, dtype: int64`
>
> `通过多个行索引获取多个行数据:
>  c1  c2  c3  c4
> s1   0   1   2   3
> s3   8   9  10  11`

```python
# 5. 通过位置索引获取一行的值
print("通过位置索引获取一行的值:")
print(df.iloc[1])

# 6. 通过位置索引获取多行数据
print("通过位置索引获取多行数据:")
print(df.iloc[[0,2]])

# 7. 获取具体位置的值
print("获取具体位置的值:")
print(df.iloc[1,2])         # 前面是行，后面是列
# print(df.iloc[1][2])      # FutureWarning
```

> 输出结果：
>
> `通过位置索引获取一行的值:
> c1    4
> c2    5
> c3    6
> c4    7
> Name: s2, dtype: int64`
>
> `通过位置索引获取多行数据:
>  c1  c2  c3  c4
> s1   0   1   2   3
> s3   8   9  10  11`
>
> `获取具体位置的值:
> 6`

```python
# 8. 通过位置索引切片获取数据
print("通过位置索引切片获取数据:")
print(df.iloc[0:2,1:3])     # 前面是行，后面是列，左闭右开

# 9. 通过名字索引切片获取数据
print("通过名字索引切片获取数据:")
print(df.loc['s1':'s3','c2':'c4'])  # 前面是行，后面是列，左闭右闭

# 10. 一次取多个不连续的行或者列
print("一次取多个不连续的行或者列:")
print(df.iloc[[1,2],[0,3]])  # 前面是行，后面是列
#改为loc实现上一行
print(df.loc[['s2','s3'],['c1','c4']])
```

> 输出结果：
>
> `通过位置索引切片获取数据:
>  c2  c3
> s1   1   2
> s2   5   6`
>
> `通过名字索引切片获取数据:
>  c2  c3  c4
> s1   1   2   3
> s2   5   6   7
> s3   9  10  11`
>
> `一次取多个不连续的行或者列:`
>
> `    c1  c4
> s2   4   7
> s3   8  11`
>
> `    c1  c4
> s2   4   7
> s3   8  11`

### 10. Pandas 数据清洗

#### 10.1 重复值处理

**1. 检测重复值 `duplicated()`**

```python
data = {
    "name": ["Alice", "Alice", "Charlie", "David", "Alice", "Charlie"],
    "age": [20, 22, 21, 20, 20, 21],
    "score": [85, 90, 78, 92, 85, 78],
    "gender": ["女", "男", "男", "男", "女", "男"]
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4', 's5', 's6'], columns=['name', 'age', 'score', 'gender'])
print(df)
print('-'*20)

# 1. 检测重复值
print(df.duplicated())      # 返回布尔Series，True表示重复行
print('-'*20)

# 2. 指定列检测重复值(可以指定多列)
# 参数 keep, 默认值为'first', 表示只保留第一个重复行, 'last'表示只保留最后一个重复行, False表示标记所有重复行
df_dup_by_col = df.duplicated(subset=['age'], keep='first')
print(df_dup_by_col)
```

> 输出结果：
>
> `       name  age  score gender
> s1    Alice   20     85      女
> s2    Alice   22     90      男
> s3  Charlie   21     78      男
> s4    David   20     92      男
> s5    Alice   20     85      女
> s6  Charlie   21     78      男`
> `--------------------`
> `s1    False
> s2    False
> s3    False
> s4    False
> s5     True
> s6     True
> dtype: bool`
> `--------------------`
> `s1    False
> s2    False
> s3    False
> s4     True
> s5     True
> s6     True
> dtype: bool`

**2. 删除重复值 `drop_duplicates()`**

```python
# 创建一个数据表
data = {
    "name": ["Alice", "Alice", "Charlie", "David", "Alice", "Charlie"],
    "age": [20, 22, 21, 20, 20, 21],
    "score": [85, 90, 78, 92, 85, 78],
    "gender": ["女", "男", "男", "男", "女", "男"]
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4', 's5', 's6'], columns=['name', 'age', 'score', 'gender'])
print("原数据:")
print(df)

# 1. 删除完全重复的行
df_drop_dup = df.drop_duplicates()
print("删除完全重复的行:")
print(df_drop_dup)

# 2. 删除部分列重复的行
df_drop_dup_by_col = df.drop_duplicates(subset=['name'], keep='first')
print("删除部分列重复的行:")
print(df_drop_dup_by_col)

# 3. 直接在原数据上删除
df.drop_duplicates(inplace=True)
print("直接在原数据上删除:")
print(df)
```

> 输出结果：
>
> `原数据:
>     name  age  score gender
> s1    Alice   20     85      女
> s2    Alice   22     90      男
> s3  Charlie   21     78      男
> s4    David   20     92      男
> s5    Alice   20     85      女
> s6  Charlie   21     78      男`
> `删除完全重复的行:
>     name  age  score gender
> s1    Alice   20     85      女
> s2    Alice   22     90      男
> s3  Charlie   21     78      男
> s4    David   20     92      男`
> `删除部分列重复的行:
>     name  age  score gender
> s1    Alice   20     85      女
> s3  Charlie   21     78      男
> s4    David   20     92      男`
> `直接在原数据上删除:
>     name  age  score gender
> s1    Alice   20     85      女
> s2    Alice   22     90      男
> s3  Charlie   21     78      男
> s4    David   20     92      男`

#### 10.2 缺失值处理

先评估缺失程度，再选修复策略（删除 / 填充 / 插值）

**1. 检测缺失值 `isnull()`**

```python
# 1. 创建一个数据表
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "age": [20, 22, 21, 20, 20, np.nan],
    "score": [85, 90, np.nan, 92, 85, np.nan],
    "gender": ["女", "男", "男", np.nan, np.nan,np.nan]
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4', 's5', 's6'], columns=['name', 'age', 'score', 'gender'])
print(df)

# 2. 检测缺失值
print(df.isnull())

# 3. 计算缺失个数
print("每一列缺失个数:")
print(df.isnull().sum())

print("每一行缺失个数:")
print(df.isnull().sum(axis=1))

# 4. 计算缺失率
print("每一列缺失率:")
print(df.isnull().sum() / len(df))

print("每一行缺失率:")
print(df.isnull().sum(axis=1) / len(df.columns) )
```

> 输出结果：
>
> `       name   age  score gender
> s1    Alice  20.0   85.0      女
> s2      Bob  22.0   90.0      男
> s3  Charlie  21.0    NaN      男
> s4    David  20.0   92.0    NaN
> s5      Eva  20.0   85.0    NaN
> s6    Frank   NaN    NaN    NaN`
>
> `     name    age  score  gender
> s1  False  False  False   False
> s2  False  False  False   False
> s3  False  False   True   False
> s4  False  False  False    True
> s5  False  False  False    True
> s6  False   True   True    True`
>
> `每一列缺失个数:
> name      0
> age       1
> score     2
> gender    3
> dtype: int64`
>
> `每一行缺失个数:
> s1    0
> s2    0
> s3    1
> s4    1
> s5    1
> s6    3
> dtype: int64`
>
> `每一列缺失率:
> name      0.000000
> age       0.166667
> score     0.333333
> gender    0.500000
> dtype: float64`
>
> `每一行缺失率:
> s1    0.00
> s2    0.00
> s3    0.25
> s4    0.25
> s5    0.25
> s6    0.75
> dtype: float64`

**2. 删除缺失值 `dropna()`**

```python
# 1. 创建一个数据表
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "age": [20, 22, 21, 20, 20, np.nan],
    "score": [85, 90, np.nan, 92, 85, np.nan],
    "gender": ["女", "男", "男", np.nan, np.nan,np.nan]
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4', 's5', 's6'], columns=['name', 'age', 'score', 'gender'])
print("原数据：")
print(df)

# 2. 删除含有缺失值的行或列(谨慎操作，可能会丢失大量数据)
df_drop_na = df.dropna()
print("删除含有缺失值的行:")
print(df_drop_na)

df_drop_na_by_col = df.dropna(axis=1)
print("删除含有缺失值的列:")
print(df_drop_na_by_col)

# 3. 删除 score数据缺失的行
df_drop_na_by_col = df.dropna(subset=['score'])
print("删除 score数据缺失的行:")
print(df_drop_na_by_col)
```

> 输出结果：
>
> `原数据：
>     name   age  score gender
> s1    Alice  20.0   85.0      女
> s2      Bob  22.0   90.0      男
> s3  Charlie  21.0    NaN      男
> s4    David  20.0   92.0    NaN
> s5      Eva  20.0   85.0    NaN
> s6    Frank   NaN    NaN    NaN`
>
> `删除含有缺失值的行:
>   name   age  score gender
> s1  Alice  20.0   85.0      女
> s2    Bob  22.0   90.0      男`
>
> `删除含有缺失值的列:
>     name
> s1    Alice
> s2      Bob
> s3  Charlie
> s4    David
> s5      Eva
> s6    Frank`
>
> `删除 score数据缺失的行:
>   name   age  score gender
> s1  Alice  20.0   85.0      女
> s2    Bob  22.0   90.0      男
> s4  David  20.0   92.0    NaN
> s5    Eva  20.0   85.0    NaN`

**3. 填充缺失值 `fillna()`**

```python
#填充缺失值
# 1. 创建一个数据表
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "age": [20, 22, 21, 20, 20, np.nan],
    "score": [85, 90, np.nan, 92, 85, np.nan],
    "gender": ["女", "男", "男", np.nan, np.nan,np.nan]
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4', 's5', 's6'], columns=['name', 'age', 'score', 'gender'])
print("原数据:")
print(df)

# 2. 填充全局缺失值
df_fill_na = df.fillna(0)
print("填充缺失值为0:")
print(df_fill_na)

# 3. 填充某一列的缺失值
df_fill_na_by_col = df.fillna({'gender': '男','score':80})
print("填充【gender】缺失值为男，【score】缺失值为80:")
print(df_fill_na_by_col)


# 4.单独把某列取出来，填充缺失值
df['score'] = df['score'].fillna(80)
print("单独把【score】列取出来，填充缺失值为80:")
print(df)
```

> 输出结果：
>
> `原数据:
>     name   age  score gender
> s1    Alice  20.0   85.0      女
> s2      Bob  22.0   90.0      男
> s3  Charlie  21.0    NaN      男
> s4    David  20.0   92.0    NaN
> s5      Eva  20.0   85.0    NaN
> s6    Frank   NaN    NaN    NaN`
>
> `填充缺失值为0:
>     name   age  score gender
> s1    Alice  20.0   85.0      女
> s2      Bob  22.0   90.0      男
> s3  Charlie  21.0    0.0      男
> s4    David  20.0   92.0      0
> s5      Eva  20.0   85.0      0
> s6    Frank   0.0    0.0      0`
>
> `填充【gender】缺失值为男，【score】缺失值为80:
>     name   age  score gender
> s1    Alice  20.0   85.0      女
> s2      Bob  22.0   90.0      男
> s3  Charlie  21.0   80.0      男
> s4    David  20.0   92.0      男
> s5      Eva  20.0   85.0      男
> s6    Frank   NaN   80.0      男`
>
> `单独把【score】列取出来，填充缺失值为80:
>     name   age  score gender
> s1    Alice  20.0   85.0      女
> s2      Bob  22.0   90.0      男
> s3  Charlie  21.0   80.0      男
> s4    David  20.0   92.0    NaN
> s5      Eva  20.0   85.0    NaN
> s6    Frank   NaN   80.0    NaN`

## <span style='color:red'>Day10</span>

### 1. Pandas 数据转换：函数应用

#### 1.1 `apply()`应用函数

基本语法：==`Series.apply(func, args=(), **kwargs)`==

- 既支持 **Series**（一维），也支持**DataFrame**（二维） 
- 作用：按规则批量处理数据

**处理 Series数据**

```python
# 使用案例
# 创建一个学生表
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [20, 22, 21, 20],
    "score": [85, 90, 78, 92],
    "gender": ["女", "男", "男", "男"]
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'], columns=['name', 'age', 'score', 'gender'])
print(df)
print(type(df['age'])) # 某一列取出是 Series

# 比如需要把年龄数据乘以2
def mul_two(x):
    return x * 2

df['age'] = df['age'].apply(mul_two)
# 再次打印一下看看变化
print(df)

# 也可以直接使用匿名函数
df['age'] = df['age'].apply(lambda x: x * 2)
print(df)
```

> 输出结果：
>
> `       name  age  score gender
> s1    Alice   20     85      女
> s2      Bob   22     90      男
> s3  Charlie   21     78      男
> s4    David   20     92      男`
>
> `<class 'pandas.core.series.Series'>`
>
> `    name  age  score gender
> s1    Alice   40     85      女
> s2      Bob   44     90      男
> s3  Charlie   42     78      男
> s4    David   40     92      男`
>
> `    name  age  score gender
> s1    Alice   80     85      女
> s2      Bob   88     90      男
> s3  Charlie   84     78      男
> s4    David   80     92      男`

**处理 DataFrame 数据**

```python
df = pd.DataFrame(np.arange(12).reshape(3,4), index=['s1', 's2', 's3'], columns=['c1', 'c2', 'c3', 'c4'])
print(df)

# 1. 统计每个列的数据个数
print(df.apply(lambda x: x.count(), axis=0))        # 默认轴是0，即列

# 2. 统计每个列的最大值
print(df.apply(lambda x: x.max(), axis=0))          # 默认轴是0，即列

# 3. 统计每个行的数据个数
print(df.apply(lambda x: x.count(), axis=1))        # 轴1, 是行
```

> 输出结果：
>
> `    c1  c2  c3  c4
> s1   0   1   2   3
> s2   4   5   6   7
> s3   8   9  10  11`
>
> `c1    3
> c2    3
> c3    3
> c4    3
> dtype: int64`
>
> `c1     8
> c2     9
> c3    10
> c4    11
> dtype: int64`
>
> `s1    4
> s2    4
> s3    4
> dtype: int64`

#### 1.2 `map()`映射

map 映射函数，核心作用是 “按规则逐元素转换数据”，一般用于 **Series**

语法格式：==`Series.map(arg, na_action=None)`==
- arg：可传入字典，函数(匿名函数)
- na_action：缺失值处理参数，默认为None

```python
# 使用案例
# 创建一个学生二维表
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [20, 22, 21, 20],
    "score": [85, 90, 78, 92],
    "gender": ["女", "男", "男", "男"]
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'], columns=['name', 'age', 'score', 'gender'])
print(df)

# 案例1: 将性别数据映射为male和female
# 通过字典映射
gender_map = {
    "男": "male",
    "女": "female"
}
df['gender'] = df['gender'].map(gender_map)
print(df)

# 案例2: 将性别数据映射为1和0
# 通过函数映射
df['gender'] = df['gender'].map(lambda x: 1 if x == "male" else 0)
print(df)

# 案例3: 给所有的数据乘以2
df2 = pd.DataFrame(np.arange(12).reshape(3,4), index=['s1', 's2', 's3'], columns=['c1', 'c2', 'c3', 'c4'])
print(df2)
df2 = df2.map(lambda x: x * 2)
print(df2)
```

> 输出结果：
>
> `       name  age  score gender
> s1    Alice   20     85      女
> s2      Bob   22     90      男
> s3  Charlie   21     78      男
> s4    David   20     92      男
> ` 
>
> `       name  age  score  gender
> s1    Alice   20     85  female
> s2      Bob   22     90    male
> s3  Charlie   21     78    male
> s4    David   20     92    male
> ` 
>
> `       name  age  score  gender
> s1    Alice   20     85       0
> s2      Bob   22     90       1
> s3  Charlie   21     78       1
> s4    David   20     92       1
> ` 
>
> `    c1  c2  c3  c4
> s1   0   1   2   3
> s2   4   5   6   7
> s3   8   9  10  11
> ` 
>
> `    c1  c2  c3  c4
> s1   0   2   4   6
> s2   8  10  12  14
> s3  16  18  20  22`

### 2. Pandas 数据分析：统计与计算

#### 2.1 描述性统计 `df.describe()`

`describe()` 是 pandas 提供的 **描述性统计函数**，用于快速查看数据的整体情况。

不同数据类型，`describe()` 给出的统计信息是不一样的：

- **数值型列**（int / float）：均值、标准差、最大值等
- **object 列（字符串 / 类别）**：出现频率、唯一值数量等

```python
# 创建一个数据表
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "age": [20, 22, 21, 20, 20, 30],
    "score": [85, 90, 88, 92, 85, 72],
    "gender": ["女", "男", "男", '男', '女', '男']
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4', 's5', 's6'], columns=['name', 'age', 'score', 'gender'])
print(df)

# 1. 单列统计
print("单列统计:")
print(df['age'].describe())
print('-'*20)

# 2. 多列统计
print("多列统计:")
print(df[['age', 'score']].describe())
print('-'*20)

# 3. 所有列进行统计(只会对，也只能对数值列进行统计)
print(df.describe())

# 4. 常用统计函数
print("常用统计函数:")
print(df['age'].mean())        # 平均数
print(df['age'].median())      # 中位数
print(df['age'].min())         # 最小值
print(df['age'].max())         # 最大值
print(df['age'].std())         # 标准差
print(df['age'].sum())         # 求和
```

> 输出结果：
>
> `        name  age  score  gender
> s1    Alice   20     85      女
> s2      Bob   22     90      男
> s3  Charlie   21     88      男
> s4    David   20     92      男
> s5      Eva   20     85      女
> s6    Frank   30     72      男`
>
> `单列统计:
> count     6.000000
> mean     22.166667
> std       3.920034
> min      20.000000
> 25%      20.000000
> 50%      20.500000
> 75%      21.750000
> max      30.000000
> Name: age, dtype: float64`
>
> `--------------------`
>
> `多列统计:
>        age      score
> count   6.000000   6.000000
> mean   22.166667  85.333333
> std     3.920034   7.089899
> min    20.000000  72.000000
> 25%    20.000000  85.000000
> 50%    20.500000  86.500000
> 75%    21.750000  89.500000
> max    30.000000  92.000000`
>
> `--------------------`
>
> `          age      score
> count   6.000000   6.000000
> mean   22.166667  85.333333
> std     3.920034   7.089899
> min    20.000000  72.000000
> 25%    20.000000  85.000000
> 50%    20.500000  86.500000
> 75%    21.750000  89.500000
> max    30.000000  92.000000`
>
> `常用统计函数:`
> `22.166666666666668`
> `20.5`
> `20`
> `30`
> `3.920034013457877`
> `133`

`include` 用来 **指定要统计哪些数据类型的列**。

常见的有：

- `df.describe(include=['number'])   # 数值型`
- `df.describe(include=['object'])   # 字符串/类别型`
- `df.describe(include='all')        # 所有列`

不加`include` 的默认情况下：

- **只统计数值型列**
- `object` 列会被直接忽略

对于 `object` 类型列，`describe()` **不会计算均值、最大值这些数值统计**，而是返回下面 4 项：

| 字段     | 含义                 |
| -------- | -------------------- |
| `count`  | 非空值数量           |
| `unique` | 不重复值的个数       |
| `top`    | 出现次数最多的值     |
| `freq`   | `top` 对应的出现次数 |

```python
print(df.describe(include=['object']))  # 对数据类型为 object 的列进行统计描述
```

> 输出结果：
>
> `         name gender
> count       6      6
> unique      6      2
> top     Alice      男
> freq        1      4`

#### 2.2 聚合计算 `agg()`

对同一列 / 多列同时应用多个统计函数，高效生成汇总结果。

```python
# 创建一个数据表
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "age": [20, 22, 21, 20, 20, 30],
    "score": [85, 90, 88, 92, 85, 72],
    "gender": ["女", "男", "男", '男', '女', '男']
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4', 's5', 's6'], columns=['name', 'age', 'score', 'gender'])
print(df)

# 1. 单列多函数聚合
score_stats = df['score'].agg([
    "mean", "max", "min"
])
print(score_stats)

# 2. 多列分别聚合
multi_col_stats = df.agg({
    "age": ["mean", "count"],    # age列：均值、非空计数
    "score": ["median", "std"]   # score列：中位数、标准差
})
print(multi_col_stats)
```

> 输出结果：
>
> `       name  age  score gender
> s1    Alice   20     85      女
> s2      Bob   22     90      男
> s3  Charlie   21     88      男
> s4    David   20     92      男
> s5      Eva   20     85      女
> s6    Frank   30     72      男`
>
> `mean    85.333333
> max     92.000000
> min     72.000000
> Name: score, dtype: float64
> `
>
> `              age      score
> mean    22.166667        NaN
> count    6.000000        NaN
> median        NaN  86.500000
> std           NaN   7.089899`

### 3. `add_prefix()`：pandas 重命名方法

基本语法：==`对象.add_prefix('前缀')`==

作用：在现有列名（或索引名）前面统一加上一个**前缀字符串**

### 4. Pandas 分组

```python
# 创建一个数据表
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "age": [20, 22, 21, 20, 20, 30],
    "score": [85, 90, 88, 92, 82, 72],
    "gender": ["女", "男", "男", '男', '女', '男']
}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4', 's5', 's6'], columns=['name', 'age', 'score', 'gender'])
print(df)

# 1. 分组
group_by_gender = df.groupby('gender')
print(group_by_gender)  # 分组后不聚合，获得的只是一个分组后的对象

# 2. 分组之后统计
print("分组之后统计:")
print(group_by_gender.describe())

# 3. 分组之后求均值
print("分组之后求均值:")
mean_score = df.groupby('gender')['score'].mean().add_prefix('mean_')  # add_prefix('mean_') 给结果的“列名或索引名”加前缀'mean_'
print(mean_score)


```

> 输出结果：
>
> `       name  age  score gender
> s1    Alice   20     85      女
> s2      Bob   22     90      男
> s3  Charlie   21     88      男
> s4    David   20     92      男
> s5      Eva   20     82      女
> s6    Frank   30     72      男`
>
> `<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001D2E7CD9E80>`
>
> `分组之后统计:
>         age                                                    score        \
>         count   mean     std    min    25%   50%   75%   max   count  mean   
> gender                                                                     
> 女        2.0  20.00  0.000000  20.0  20.00  20.0  20.0  20.0   2.0  83.5   
> 男        4.0  23.25  4.573474  20.0  20.75  21.5  24.0  30.0   4.0  85.5   `
>
> `             std   min    25%   50%    75%   max  
> gender                                            
> 女       2.121320  82.0  82.75  83.5  84.25  85.0  
> 男       9.146948  72.0  84.00  89.0  90.50  92.0  `
>
> `分组之后求均值:
> gender
> mean_女    83.5
> mean_男    85.5
> Name: score, dtype: float64`

`agg()`和`transform()`都能传入多个函数，对同一列 / 多列同时应用多个统计函数（包括自定义函数）

区别在结果不同

```python
df.groupby("gender")["score"].agg('max')
```

输出结果：

<img src="C:/Users/MSI-NB/AppData/Roaming/Typora/typora-user-images/image-20260226011510287.png" alt="image-20260226011510287" style="zoom:80%;" />

> 按分组给出最大值

```python
df.groupby("gender")["score"].transform('max')
```

输出结果：

![image-20260226011629001](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260226011629200.png)

> 与原DF格式一致，给出每个样例所在组的最大值

```python
# 4. 分组之后进行转换
# 需求: 按性别分组, 求每个组的最高分 (传入已有聚合函数)
df["max_score"] = df.groupby("gender")["score"].transform("max")
print(df[["name", "gender", "score", "max_score"]])

# 需求: 按性别分组, 计算每个学生分数在组内的降序排名 (传入自定义函数)
# ascending=False 表示降序
df["score_rank"] = df.groupby("gender")["score"].transform(lambda group: group.rank(ascending=False))
print(df[["name", "gender", "score", "score_rank"]])
```

> 输出结果：
>
> `       name   gender   score   max_score
> s1    Alice      女     85         85
> s2      Bob      男     90         92
> s3  Charlie      男     88         92
> s4    David      男     92         92
> s5      Eva      女     82         85
> s6    Frank      男     72         92`
>
> `       name   gender   score   score_rank
> s1    Alice      女     85         1.0
> s2      Bob      男     90         2.0
> s3  Charlie      男     88         3.0
> s4    David      男     92         1.0
> s5      Eva      女     82         2.0
> s6    Frank      男     72         4.0`

### 5. `rank()`方法

`rank()` 是 pandas 中用于 **计算排名** 的方法：

- 给每个值分配一个“名次”
- 默认 **从小到大排名**

语法：==`group.rank(ascending=False, method="average")`==

- `ascending`：升序 / 降序
    - `ascending=True`（默认）：升序，小的排名靠前
    - `ascending=False`：降序，大的排名靠前
- `method`：并列值怎么排

`method`常见取值如下：

| method    | 含义                   | 示例：对[92, 88, 88, 75]中的（88, 88） |
| --------- | ---------------------- | -------------------------------------- |
| `average` | 并列取平均名次（默认） | 2.5, 2.5                               |
| `dense`   | 紧凑排名，不跳号       | 2, 2                                   |
| `min`     | 并列取最小名次         | 2, 2                                   |
| `max`     | 并列取最大名次         | 3, 3                                   |
| `first`   | 按出现顺序             | 2, 3                                   |

### 6. 独热编码（one-hot）

独热码是一种**一位有效编码**，其核心特征是：在一组编码中，**任意时刻只有一个二进制位为 1，其余所有位均为 0**。这种编码方式不依赖数值大小表示信息，而是通过“哪一位为 1”来唯一标识一个状态或类别，因此也被称为“独一热码”或“一位有效码”。

- 例如，“猫、狗、鸟”三类标签，独热码表示为 `[1,0,0]`（猫）、`[0,1,0]`（狗）、`[0,0,1]`（鸟）
- 避免标签的“数值大小关联”（如二进制码 `00`、`01`、`10` 可能被模型误解为“猫 < 狗 < 鸟”，而独热码无此问题），同时适配神经网络的输出层（如 Softmax 层输出与独热码标签的交叉熵计算）

**优势**：解码简单，时序性能好，适合状态数较少、对速度要求高的场景

![image-20260226201515419](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260226201515663.png)

### 7. ⚠scikit-learn 特征提取

在sklearn中常见的特征提取工具：

- 字典数据：DictVectorizer
- 文本数据：CountVectorizer、TfidfVectorizer
- 图像数据：PatchExtractor（了解，参考官方文档）

#### 7.1 从字典加载特征 `DictVectorizer()`

用于处理**字典形式特征数据**，核心功能是将由字典组成的特征列表转换为机器学习模型可直接使用的**数值矩阵**（特征向量）。

```python
# 导入字典提取器
from sklearn.feature_extraction import DictVectorizer
import pandas as pd

# 准备字典数据
data = [
    {'颜色': '红', '尺寸': '大', '价格': 100},
    {'颜色': '蓝', '尺寸': '中', '价格': 80},
    {'颜色': '红', '尺寸': '小', '价格': 50}
]

# 初始化字典提取器
# sparse=False 表示返回的矩阵是二维的，而不是稀疏矩阵
# sparse=True 默认值，返回的矩阵是稀疏矩阵，稀疏矩阵只保存非零的元素，可以节省内存
# 稀疏矩阵：矩阵中，大多数值都为0的矩阵
dict_vec = DictVectorizer(sparse=False)

# 提取特征
X = dict_vec.fit_transform(data)

# 查看结果
print(X)

# 查看特征名
print(dict_vec.get_feature_names_out())

# 结合DataFrame查看结果
pd.DataFrame(X, columns=dict_vec.get_feature_names_out())
```

**结果说明：**

- 数值特征“价格”直接保留原值（第一列）；
- 类别特征“颜色”被独热编码为“颜色=红”“颜色=蓝”
- 类别特征“尺寸”被独热编码为“尺寸=大”“尺寸=中”“尺寸=小”

<img src="https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260226211606941.png" alt="image-20260226211606685" style="zoom:80%;" />

#### 7.2 从英文文本加载特征 `CountVectorizer()`

在自然语言处理（NLP）中，`CountVectorizer` 是 scikit-learn 库中常用的文本特征提取工具，它的核心功能是将英文文本（或其他语言文本）转换为**基于词频的数值特征矩阵**（即统计每个词在文档中出现的次数）。

```python
# 举个例子

# 导入包
from sklearn.feature_extraction.text import CountVectorizer

# 样本文本（3个文档）
documents = [
    "I love machine learning. Machine learning is interesting.",
    "I love coding. Coding is fun and useful.",
    "Machine learning and coding are my favorite skills."
]

# 创建CountVectorizer对象（默认参数：小写化文本、按空格/标点分词、不过滤停用词）
# min_df/max_df参数解释：
# min_df: 最小文档频率，即单词至少出现的次数或比例，低于此阈值的单词将被忽略
# max_df: 最大文档频率，即单词在文档中的次数或比例，高于此阈值的单词将被忽略
# 当min_df和max_df都为整数时，表示单词出现的次数，当min_df和max_df都为小数时，表示单词在文档中的比例
count_vec = CountVectorizer(min_df = 2)

# 训练并转换文档
X = count_vec.fit_transform(documents)

# 查看结果
print(X.toarray())

# 查看特征名
print(count_vec.get_feature_names_out())

# 结合DataFrame查看
df = pd.DataFrame(X.toarray(), columns = count_vec.get_feature_names_out())
print(df)
```

此示例中，不设置 “ min_df ” 值时会发现这种方法认为 “I” 不是一个有含义的单词（特征名中没有 “I” ），不计算它的词频，因此这种方法适用于分类任务，而不适用于大模型的生成场景。

#### 7.3 从中文文本加载特征

对于中文词汇，`CountVectorizer`并没有那么“聪明”，不能正确的对中文进行分词之后再提取特征。

所以需要我们**先对中文进行分词，然后再使用`CountVectorizer()`提取特征**。

```python
# 导入分词
import jieba
# 导入特征提取对象
from sklearn.feature_extraction.text import CountVectorizer
# 导入pandas
import pandas as pd

# 1. 文本
documents = [
    "人生苦短，我喜欢 python",
    "人生漫长，不用 python python",
    "人生漫漫，不用 python python python"
]

# 2. 文本分词，得到一个分词之后的文本列表
# 使用jieba分词，把每个句子分词，然后通过空格再合并成一个句子
# CountVectorizer()是根据空格分词的，所以需要添加空格
cut_documents = [ " ".join(jieba.cut(document)) for document in documents]
print(cut_documents)

# 3. 创建特征提取对象
vectorizer = CountVectorizer(min_df=2)

# 4. 创建特征矩阵
X = vectorizer.fit_transform(cut_documents)

# 5. 使用DataFrame查看结果
pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
```

#### 7.4 中文分词工具

在 Python 中，中文分词是自然语言处理（NLP）的基础任务之一，常用的工具库有很多，各自有不同的特点和适用场景。以下是最常用的几种中文分词工具及其使用方法：

- **jieba（结巴分词）**
    最流行的中文分词工具之一，轻量、高效，支持三种分词模式，可自定义词典，支持词性标注
- **SnowNLP**
- **THULAC（清华研发）**
- **pyltp（哈工大研发）**

**安装**

```python
pip install jieba
```

**使用**

```python
import jieba

text = "我爱自然语言处理"

# 得到的结果是一个可迭代的生成器对象
result = jieba.cut(text)
# for i in result:
#     print(i)

# 合并
text = " ".join(result)
print(text)
```

> jieba.lcut 和 jieba.cut 的区别如下：
>
> - jieba.lcut(sentence) 直接返回分词后的列表。
> - jieba.cut(sentence) 返回的是一个可迭代的生成器，需要用 list() 转换成列表才可查看全部分词结果。

#### 7.5 ⚠TF-IDFVectorizer

`TF-IDFVectorizer` 是 scikit-learn 中另一种常用的文本特征提取工具，它在 **词频（TF）** 的基础上引入了 **逆文档频率（IDF）** 权重，能更合理地衡量词语在文本中的“重要性”，避免高频但无实际意义的词（如 “the”、“is”）过度影响特征。

****

**1. TF-IDF是什么？**

TF-IDF 是 **Term Frequency – Inverse Document Frequency** 的缩写，由两部分组成：

- **词频（TF）**：某个词在当前文档中出现的频率，计算公式为：

  \[
  TF(t, d) = \frac{\text{词}t\text{在文档}d\text{中出现的次数}}{\text{文档}d\text{的总词数}}
  \]

  实际实现中，scikit-learn 默认直接用“出现次数”作为 TF，而非频率，更简单直观。

- **逆文档频率（IDF）**：衡量一个词的**“稀有度”**——如果一个词在多数文档中都出现，它的 IDF 会较低（比如 “is”、“and”）；如果只在少数文档中出现，IDF 会较高（比如 “machine learning”、“coding”）。计算公式为：
\[
  IDF(t) = \log\left(\frac{\text{总文档数}}{\text{包含词}t\text{的文档数} + 1}\right)
\]

分母加 1 是为了避免“包含词 t 的文档数为 0（测试集）”时的除零错误，即“平滑处理”，  log 是以 10 为底的。

最终，**TF-IDF 值 = TF × IDF**，它综合了词在当前文档中的“出现频率”和在所有文档中的“稀有度”，值越高说明该词对当前文档的区分度越重要。

---

**2. 与 CountVectorizer 的区别？**

- `CountVectorizer` 只统计词频，高频词（即使无意义）权重会很高；
- `TF-IDFVectorizer` 通过 IDF 降低高频通用词的权重，突出稀有但关键的词，更适合作为文本特征（如分类、检索等任务）

---

**3. TF-IDFVectorizer的使用**

```python
# 1. 导入包
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 样本文本（3个文档）
documents = [
    "I love machine learning. Machine learning is interesting.",
    "I love coding. Coding is fun and useful.",
    "Machine learning and coding are my favorite skills."
]

# 2. 创建TF-IDF对象
# stopwords='english' 忽略英文中的停用词
# 停用词：指文本中频繁出现，但通常对语义理解帮助不大的虚词或常见词
tfidf = TfidfVectorizer(min_df=1, stop_words='english')

# 3. 创建特征矩阵
X = tfidf.fit_transform(documents)

# 4. 显示结果
pd.DataFrame(X.toarray(), columns=tfidf.get_feature_names_out())
```

### 8. Cursor / VS Code / Trae 中 Jupyter NoteBook运行结果显示自动换行设置

![image-20260226220947192](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260226220947520.png)

搜索 word wrap

![image-20260226221126523](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260226221127081.png)

## <span style='color:red'>Day11</span>

### 1. scikit-learn 数值特征预处理

在机器学习中，**数值特征预处理**是模型训练前的关键步骤，其核心目标是通过调整数据的尺度、分布或补全缺失值，让数据更符合模型的假设（如线性模型假设特征分布相近），从而提升模型的稳定性和性能。

#### 1.1 ⚠归一化（区间缩放）

将特征值线性映射到**指定的有限区间**（如 [0,1] 或 [-1,1]），消除不同特征的量纲差异。

**核心工具：`MinMaxScaler()`**

**⚠原理**：通过特征的最小值（`x_min`）和最大值（`x_max`）进行线性变换，公式为：
$$
X_{\text{scaled}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}
\times (\text{max\_range} - \text{min\_range})
+ \text{min\_range}
$$
含义说明：

- $X_{\min}$：最小值
- $X_{\max}$：最大值
- $\text{min\_range}, \text{max\_range}$：目标区间上下界

>  默认区间为 **[0,1]**

这种线性变换的**特点**是：

- 不改变数据的**分布形状**（如原始数据是均匀分布，归一化后仍是均匀分布）
- 不改变数据间的**相对关系**（如原始数据中 A > B，归一化后仍 A' > B'）
- 仅改变数据的**绝对数值范围**，从而消除尺度差异

> 机器学习假设：所有样本都是**独立同分布**的（即一个样本变化不会影响其它样本，样本之间没有联系）
>
> 算法是要**学习数据的分布**

**示例：**

```python
import numpy as np
# 导入归一化类
from sklearn.preprocessing import MinMaxScaler

# 1. 创建数据
data = np.array([[1,200],[2,300],[3,400]])
print(data)

# 2. 创建归一化类
scaler = MinMaxScaler(feature_range=(0,1))

# 3. 训练并归一化数据
data_scaled = scaler.fit_transform(data)

# 4. 显示结果
print(data_scaled)
```

**注意事项：**

[1] 归一化容易受到**异常点**的影响
[2] 归一化处理数据，鲁棒性较差（也就是在异常点的影响下波动较大），只适合**精确、数据量小**的场景
[3] 归一化处理之后，更容易通过**梯度下降法**找最优解

#### 1.2 ⚠标准化（Z-score缩放）

标准化的核心是将特征转换为**均值为 0、标准差为 1**的分布（也就是 Z-score 分布），保留数据的相对离散程度，数据的分布仍然是原有分布，更适合近似正态分布的数据。

![image-20260228020258448](C:/Users/MSI-NB/AppData/Roaming/Typora/typora-user-images/image-20260228020258448.png)

> **标准差（Standard Deviation）**是用来衡量一组数据离散程度（波动大小）的统计量，反映数据**相对于平均值偏离得有多远**。
>
> 简单说一句话：
>  👉 **标准差越大，数据越分散；标准差越小，数据越集中在平均值附近。**
>
> 公式：
> $$
> \sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2}
> $$
> 取值范围：**σ≥0**

**核心工具：StandardScaler**

**原理**：基于特征的均值（μ）和标准差（σ）进行变换，公式为：


$$
X_{\text{scaled}} = \frac{X - \mu}{\sigma}
$$
含义说明：

- $X$：原始数据
- $\mu$：均值（mean）
- $\sigma$：标准差（standard deviation）

**解释：**

[1] 该公式会将符合正态分布的数据，转化为标准正态分布，会保留原始数据对称、集中的特性
[2] 如果原始数据严重偏离正态分布，那么该公式虽能统一尺度，转化为均值为0，方差为1的数据，但是无法使得转换之后的数据符合正态分布的特性
[3] 为什么我们总是希望数据更加符合正态分布呢？

很多经典统计模型和机器学习算法的设计依赖于“数据近似正态分布”的假设，或者在正态分布下表现更稳定。

原因在于：

- 符合模型的数学假设，提升参数估计的可靠性（比如线性回归的核心假设之一就是：误差项服从正态分布）
- **减少极端值的影响**，让模型更稳健（大白话来说其实就是正态分布的数据，不容易受到极值影响）
- 便于数据解读和阈值设定（符合正态分布的数据，更容易判断异常程度，从而设置异常阈值）

**示例：**

```python
import numpy as np
# 1. 导入标准化类
from sklearn.preprocessing import StandardScaler

# 2. 创建数据
data = np.array([[1,200],[2,300],[3,400]])

# 3. 创建标准化类
scaler = StandardScaler()

# 4. 训练并标准化数据
data_scaled = scaler.fit_transform(data)

# 5. 显示结果
data_scaled
```

#### 1.3 缺失值处理

现实数据常存在缺失值（`NaN`），而大多数模型（如线性回归、SVM）无法直接处理 `NaN`，需提前补全。sklearn 的 `impute` 模块提供了多种工具，比如 `SimpleImputer`、`KNNImputer` 等，我们在这里学习 `SimpleImputer`

**SimpleImputer：简单填充**

- **原理**：用指定策略（如均值、中位数、众数）填充缺失值
- **关键参数：strategy（填充策略）**
    - `mean`：均值填充（适用于近似正态分布的连续特征）；
    - `median`：中位数填充（适用于含异常值的连续特征）；
    - `most_frequent`：众数填充（适用于分类特征或离散特征）；
    - `constant`：常数填充（需指定 `fill_value`）。

**示例：**

```python
import numpy as np
# 1. 导入缺失值处理的类
from sklearn.impute import SimpleImputer

# 2. 创建数据(包含缺失值)
data = np.array([[1, np.nan], [2, 300], [np.nan, 400]])

# 3. 创建缺失值处理类
# strategy: mean, median, most_frequent, constant
# mean: 使用数据的平均值填充缺失值
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# 4. 训练模型并预测
data_new = imputer.fit_transform(data)

# 5. 输出结果
print(data_new)
```

### 2. scikit-learn 特征选择

**从原始特征中筛选子集（保留一些特征 / 剔除一些特征），找出对目标值有影响的特征，去掉冗余和噪声信息。**

这样，可以带来的**好处**是：

- 降低模型复杂度
- 提高模型的泛化能力
- 提升模型的可解释性

**特征值选择方法：**

- **过滤法**
    基于特征“统计属性”筛选（如方差、相关性），代表工具：**方差阈值（VarianceThreshold）**
- **嵌入法**
    利用模型**自身的特征重要性指标**来进行筛选，比如：线性模型（Lasso、Ridge）、决策树、随机森林
- **包裹法**
    用模型“反馈”迭代筛选（如递归消除 RFE）

****

**方差阈值进行特征选择**

✅ 此方法会剔除那些在所有样本中取值几乎不变（方差极小）的特征，因为它们无法提供区分信息。

```python
from sklearn.feature_selection import VarianceThreshold

# 创建特征数据
X = np.array([[0, 2, 0, 3],
              [0, 1, 4, 3],
              [0, 1, 1, 3]])

# 初始化方差阈值选择器（默认阈值为0，去除方差为0的特征）
selector = VarianceThreshold(threshold=0.5)

# 拟合并转换数据
X_selected = selector.fit_transform(X)

print("原始数据:\n", X)
print("方差阈值特征选择后的数据:\n", X_selected)
print("保留下来的特征索引:", selector.get_support(indices=True))
```

> 输出结果：
>
> `原始数据:
>  [[0 2 0 3]
>  [0 1 4 3]
>  [0 1 1 3]]`
>
> `方差阈值特征选择后的数据:
>  [[2 0]
>  [1 4]
>  [1 1]]`
>
> `保留下来的特征索引: [1 2]`

### 3. ⚠scikit-learn 特征降维

特征降维是通过线性或非线性数学变换，将高维特征映射到低维空间，生成全新的低维特征（非原始特征子集），核心是在降维的同时最大化保留原始数据信息。

![image-20260228045538389](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260228045538708.png)

**特征降维与特征选择的核心区别在于：**

- **特征选择**：保留原始特征，仅剔除无用项；
    **降维**：生成新特征，改变特征表达形式。
- **特征选择**可解释性强（保留原始特征含义）；
    **降维后**新特征的物理意义可能不明确。

****

#### ⚠PCA（主成分分析）降维

PCA 是最常用的线性降维方法，属于无监督学习，不依赖标签信息。



**1. PCA（Principal components analysis）降维是什么呢？**

**核心思想**：主成分分析（PCA）是一种无监督学习方法，旨在通过线性变换将原始的高维数据映射到一个低维空间，同时**尽可能保留数据的方差（即信息量）**。简单来说，PCA 的目标是找到一组新的坐标轴（称为主成分），这些坐标轴能够捕捉数据中最大的变异性，并**用更少的维度来近似表示原始数据**。

**关键名词解释：**

- **维度**：就是数据的“特征数量”。比如，房子的面积、房间数是 2 个维度，加个价格就变成 3 维。
- **降维**：把维度变少。比如，原来有 10 个特征，降维后只剩 2 个。
- **主成分**：PCA 找到的“新坐标轴”。这些新坐标轴是原来特征的某种组合，能抓住数据里最大的变化。比如：如果数据是一堆散乱的点，主成分就像是你找到的最粗的那根“趋势线”，能概括大部分点的走向。
- **方差**：数据的“散乱程度”。方差越大，说明数据点越分散，越能体现差异。比如：如果所有学生的数学成绩都是 80 分，方差就很小；如果有人 100 分，有人 20 分，方差就很大。



**2. 如何计算一组新的坐标轴呢？**

![image-20260228050128965](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260228050129162.png)

PCA 降维的本质就是找新的坐标系。那么如何找到新的坐标系呢？

假如存在新的坐标系，使得**原始数据的各个样本点和在新的坐标系下的投影点的距离和最小**，那么我们认为：

[1] 沿着轴1方向，数据分散，方差最大，最能反应数据的变化趋势，这就是应该保留的主成分
[2] 沿着轴2方向，数据集中，方差小，不能表示数据的差异，这就是应该舍弃的主成分

✅ **PCA 在降维时，只保留前几个主成分（即方差值最大的那些主成分），从而减少特征数据的维度，同时保留主要（差异）信息**

![image-20260228050208455](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260228050208672.png)



**3. 使用 sklearn 进行 PCA 降维**

```python
# 1. 导入 PCA 类
from sklearn.decomposition import PCA
import numpy as np

# 2. 创建 PCA 对象
# n_components 是整数时：保留的维度
# n_components 是小数 (0~1) 时：保留的主成分解释的方差比例
pca = PCA(n_components=2)

# 3. 准备数据
X = np.array([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])

# 4. 训练 PCA 模型
X_pca = pca.fit_transform(X)

# 5. 输出结果
print(f"原始数据结构: {X.shape[0]} 个数据, {X.shape[1]} 维")
print(f"降维后特征数: {X_pca.shape[0]} 个数据, {X_pca.shape[1]} 维")
```

> **主成分解释的方差比例**
>
> - 方差 = 数据信息量
> - 解释的方差比例 = 某主成分的方差 ÷ 总方差
> - 含义：该主成分能**保留原始数据多少信息**
>
> **要点：**
>
> - 主成分按解释方差从大到小排序
> - 常用累计解释方差 ≥ 90% / 95% 来决定保留的维度
>
> **sklearn：**
>
> ```python
> pca.explained_variance_ratio_      # 各主成分比例
> pca.explained_variance_ratio_.cumsum()  # 累计比例
> ```
>
> **一句话**：
> ✅解释的方差比例越大，该主成分越重要。

### 4. ⚠分类与回归概念区分

**分类（Classification）**：
 目标是预测**离散的类别标签**。输出是有限、可枚举的类别。
 例子：垃圾邮件判断（是 / 否）、手写数字识别（0–9）、肿瘤良性或恶性。
 常见算法：逻辑回归、决策树、朴素贝叶斯、支持向量机、KNN。

**回归（Regression）**：
 目标是预测**连续的数值**。输出是一个具体的数。
 例子：房价预测、气温预测、销量预测。
 常见算法：线性回归、多项式回归、岭回归、Lasso 回归。

**核心区别**：

- 输出类型：分类 → 类别；回归 → 数值
- 评估方式：分类常用准确率、精确率；回归常用均方误差、R²
