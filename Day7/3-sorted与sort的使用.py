# 3、练习sorted的使用

def use_sorted1():
    """
    sorted对可迭代对象进行排序，返回一个排序后的列表，不改变原对象
    sort改变原对象
    """
    nums = [5, 9, 1, 4]
    sorted_nums = sorted(nums)
    print(f'排序前：{nums}')
    print(f'排序后：{sorted_nums}')


def sorted_str_list():
    """
    对字符串列表排序
    """
    strs = ['adfsf', 'sdf', '1357sdf', 'ost', 'a']
    sorted_strs = sorted(strs, key=len)  # 根据字符串长度排列
    print(f'排序结果：{sorted_strs}')


def get_grade(a:dict):
    return a['grade']


def sorted_list_dict():
    """
    对字典列表排序
    """
    students = [
        {"name": "Alice", "age": 18, "grade":89},
        {"name": "Bob", "age": 16, "grade":59},
        {"name": "Charlie", "age": 20,"grade":60}
    ]

    # 使用匿名函数作为key
    result1 = sorted(students, key=lambda student:student['grade'], reverse=True)
    print(result1)

    # 使用自定义函数作为key
    result2 = sorted(students, key=get_grade, reverse=True)
    print(result2)


def sorted_more_column():
    """
    根据元组中多个数据排列
    """
    tuples = [(3, 5), (1, 2), (2, 4), (3, 1), (1, 3)]
    result = sorted(tuples, key=lambda x: (x[0], -x[1]))
    print(result)


def sorted_dict_more():
    """
    排序字典中多个键
    """
    students = [
        {"name": "Bob", "age": 18, 'score': 66},
        {"name": "Alice", "age": 18, 'score': 62},
        {"name": "Charlie", "age": 20, 'score': 77}
    ]
    # 先按age升序，再按name长度排序
    sorted_students = sorted(students, key=lambda x: (x['age'], -len(x['name'])))
    print(sorted_students)


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, score={self.score})'


def sorted_object():
    """
    对对象列表排列
    """
    students = [
        {"name": "Bob", "age": 18, 'score': 66},
        {"name": "Alice", "age": 18, 'score': 62},
        {"name": "Charlie", "age": 20, 'score': 77}
    ]

    # 转换，列表中放对象
    students = [Student(**stu) for stu in students]
    print(students)

    result = sorted(students, key=lambda x: x.score)
    print(result)


if __name__ == '__main__':
    # use_sorted1()
    # sorted_str_list()
    # sorted_list_dict()
    # sorted_more_column()
    # sorted_dict_more()
    sorted_object()