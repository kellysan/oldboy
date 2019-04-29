#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       内置函数
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-20
#    Change Activity:  2019-04-20:

# l1 = lambda x,y: x+y
#
# print(l1(1,1))
#
# f2 = lambda x: len(str(x))
#
#
# print(f2(111))

# for i in range(99999):
#     print(chr(i), end="")
#
###
#### sorted()

# lst = ["高进", "波多野结衣", "苍老师", "仓木麻衣", "红狗"]

# s2 = sorted(lst, key=lambda i:len(i))
# print(s2)

lst = [{"id":1, "name":'alex', "age":18},
 {"id":2, "name":'wusir', "age":16},
 {"id":3, "name":'taibai', "age":17}]
# 用age排序

s3 = sorted(lst, key=lambda d:d['age'])
#
# #### filter
# """
# 1. 返回迭代器，把可迭代对象中的每一项数据交给前面的函数，有函数决定
#
# """
#
#lst = [18,20,33,66,1,48]
#
f = filter(lambda n:n>20, lst)
print(f)

f1 = filter(lambda x:x.get('age') >= 17, lst)

print(list(f1))

print(list(filter(lambda d: d.get('age') >= 18, lst)))



### map

lst = [1,2,3,4,5,6]
m = map(lambda x:x**2, lst)
print(list(m))