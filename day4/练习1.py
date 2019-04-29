#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       练习1
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-20
#    Change Activity:  2019-04-20:



def func():
    print('第一个yield')
    s1 = yield 1
    print('s1=', s1)

    print('第二个yield')
    s2 = yield 2
    print('s2=', s2)

    print('第三个yield')
    s3 = yield 3
    print('s3=', s3)

    print('第四个yield')
    yield 4

o = func()

# print(o.__next__())
# print(o.__next__())
print(o.__next__())
print(o.send("天子"))
print(o.send("宰相"))
print(o.send("九卿"))