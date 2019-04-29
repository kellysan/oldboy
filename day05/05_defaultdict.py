#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       05_defaultdict
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:

from collections import  defaultdict

"""
默认值效果，当查询的key 没有的时候回自动的将 查询的key 写入字典
"""


d = defaultdict(lambda:123)

print(d)

d['周杰伦'] = 456

print(d)

print(d['王力宏'])

print(d)