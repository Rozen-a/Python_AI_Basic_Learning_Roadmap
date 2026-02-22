# 2、练习上课的search，findall,sub等案例

import re


def use_match():
    """
    验证字符串开头是否符合规则
    """
    pattern = r'^1[34578]\d{9}$'
    texts = ['13456798743', '123456789', '156fsdf6']
    for text in texts:
        ret = re.match(pattern, text)
        if ret:
            print(f'{text}符合规则')
        else:
            print(f'{text}不符合规则')


def use_search():
    """
    从任意位置开始匹配，找到第一个符合规则的子串
    """
    text = '我的手机号：13627846847，备用号：18368495216'
    pattern = r'1[34578]\d{9}'

    result = re.search(pattern, text)
    if result:
        print(f'第一个手机号：{result.group()}')
        print(f'位置：{result.span()}')


def use_findall():
    """
    找到所有符合规则的内容
    """
    text = '我的手机号：13627846847，备用号：18368495216'
    pattern = r'1[34578]\d{9}'

    phones = re.findall(pattern, text)
    print(f'所有手机号：{phones}')


def use_sub1():
    """
    敏感词替换
    """
    text = '这个内容是垃圾，不要传播垃圾信息'
    pattern = r'垃圾'
    new_text = re.sub(pattern, '**', text)
    print(f'替换结果:{new_text}')


def use_sub2():
    """
    手机号格式美化
    """
    text = '13845679215'
    pattern = r'(\d{3})(\d{4})(\d{4})'
    new_text = re.sub(pattern, r'\1 \2 \3', text)  # \1代表第一个分组
    print(new_text)


def use_split():
    """
    将匹配到的内容做为分隔符，分割字符串返回列表
    """
    text = 'apple banana,orange;grape'
    pattern = r'[ ,;]'  # 匹配空格、逗号、分号中任意一个
    result = re.split(pattern, text)
    print(f'分割结果：{result}')


if __name__ == '__main__':
    # use_match()
    # use_search()
    # use_findall()
    # use_sub1()
    # use_sub2()
    use_split()