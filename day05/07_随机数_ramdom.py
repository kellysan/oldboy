#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       07_随机数_ramdom
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:


import random

"""
随机数是0-1
"""
# print(random.random())
#
# # 从1- 20 之间的小数
# print(random.uniform(1,20))
#
# #1,20的整数，包括1和20
# print(random.randint(1,20))
#
# #随机取出列表中的一个
lst = ["张三丰", "张翠山", "张无忌"]
# print(random.choice(lst))
#
# #在列表中随机取出两个
# print(random.sample(lst,2))


# 打破列表数据 洗牌
random.shuffle(lst)
print(lst)