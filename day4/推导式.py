#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       列表推导式
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-20
#    Change Activity:  2019-04-20:


#### 列表推导式
#
#
# list = ["python周末%s期" % i for i in range(1,27) if i%2==1 ]
# print(list)
#
# lst = ["欧阳娜娜", "张崔猛", "欧阳难过", "张亚无照", "胡一飞", "胡怎么飞", "张炸辉"]
#
# new_list =[ i for i in lst if i[0] == '张' ]
# print(new_list)
#
# # 使用列表推导式得到            [1, 4, 9, 16, 25, 36]
# # 在[3,6,9]的基础上推到出[[1,2,3], [4,5,6],[7,8,9]]
#
#
#
# lst1 = [ i**2 for i in range(1,7)]
# print(lst1)
#
# l2 = [3,6,9]
# list2 = [[i-2,i-1,i] for i in l2 ]
# print(list2)

### 字典推导式

list1 = ["张三丰", "张无忌", "赵敏"]

# 非推导式
# dict1 = {}
# for i in range(len(list1)):
#     dict1[i] = list1[i]
#
# print(dict1)
# 推导式
print({i:list1[i] for i in range(len(list1))})

### 集合推导式 基本不用

## 生成器表达式
# g = (i for i in range(10))
# print(g)
#
# for i in g:
#     print(i)

def func():
    print('111')
    yield 222

g = func()
g1 = (i for i in g)
g2 = (i for i in g1)

# print(list(g))
# print(list(g1))
# print(list(g2))


print(list(g1))
print(list(g2))
print(list(g))




"""
生成器的惰性机制，在第一个print 的时候list 已经把取空
"""