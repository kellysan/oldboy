#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       验证码
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-01
#    Change Activity:  2019-05-01:

import random

print(ord("A"))
print(ord("Z"))
print(ord("0"))
print(ord("9"))
print(ord("a"))
print(ord("z"))

"""
刺刀练习题主要考察的是 random随机数和ord chr 内置函数的使用
"""

def auto_code(n=6):
    """
    输出验证码
    :param n: 验证码位数
    :return:
    """
    code = ""
    c = 0
    while c <= n:
        num = random.randrange(48,123)
        if  48 <= num <=57 or 65 <= num <= 90 or 97 <= num <= 122:
            code += chr(num)
        c += 1
    return code

#num = random.randrange(48,123)
print(auto_code(10))
