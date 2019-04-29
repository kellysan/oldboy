#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       判断
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-20
#    Change Activity:  2019-04-20:

from collections.abc import Iterable, Iterator
#from collections import Iterable, Iterator

list = ["中国", "日本", "美国"]

print(isinstance(list, Iterable))
print(isinstance(list, Iterator))