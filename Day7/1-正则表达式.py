# 1、练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例

import re

# 匹配“字母 + 任意数字 + 字母”
def match_single():
    pattern = r'[a-zA-z]\d[a-zA-Z]'
    texts = ['a1b', 'B2C', 'dgs', '4fs', 'a2a4']
    for text in texts:
        print('-'*30)
        ret = re.match(pattern, text)
        if ret:
            print(f'原始字符串:{text}')
            print(f'匹配成功：{ret.group()}')
        else:
            print(f'{text}不符合要求')


# 匹配“1个或多个数字”
def match_more1():
    pattern = r'\d+'
    texts = ['0', '123', 'sadf', '1asd']
    for text in texts:
        print('-'*30)
        ret = re.match(pattern, text)
        if ret:
            print(f'原始字符串:{text}')
            print(f'匹配成功：{ret.group()}')
        else:
            print(f'{text}不符合要求')


# 匹配“3-6位字母”
def match_more2():
    pattern = r'[a-zA-Z]{3,6}'
    texts = ['a', 'abfd', 'a123', 'asdf5']
    for text in texts:
        print('-'*30)
        ret = re.match(pattern, text)
        if ret:
            print(f'原始字符串:{text}')
            print(f'匹配成功：{ret.group()}')
        else:
            print(f'{text}不符合要求')


# 验证完整字符串是邮箱（开头结尾匹配）
def match_start_end():
    pattern = r'^[a-zA-Z0-9_\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$'
    emails = ['user@163.com', 'user1%@gmail.com', 'user.163.com']
    for text in emails:
        ret = re.match(pattern, text)
        if ret:
            print(f'{text}是邮箱')
        else:
            print(f'{text}不是正确的邮箱')


# 提取邮箱中的用户名和域名(匹配分组）
def match_group1():
    pattern = r'(\w+)@(\w+\.\w+)'
    email = 'user123@example.com'
    ret = re.match(pattern, email)
    if ret:
        print(f'邮箱:{ret.group()}')
        print(f'邮箱用户名：{ret.group(1)}')
        print(f'邮箱域名：{ret.group(2)}')
    else:
        print(f'{email}不是正确的邮箱')


# 匹配 0–100 之间的数字字符串（包含前导0）
def match_group2():
    texts = ['09', '90', '001', '99', '1as', 'aa2']
    pattern = r'^(0*\d{1,2}|0*100)$'
    for text in texts:
        ret = re.match(pattern, text)
        if ret:
            print(f'{text}是在0-100之间在数字字符串')
        else:
            print(f'{text}不是在0-100之间在数字字符串')


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


if __name__ == '__main__':
    # match_single()
    # match_more1()
    # match_more2()
    # match_start_end()
    # match_group1()
    # match_group2()
    match_group3()