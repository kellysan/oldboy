#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       05生成器
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-20
#    Change Activity:  2019-04-20:

#
# def func():
#     print("hahhah")
#     yield 1    # yield 就是一个生成器函数，会创建一个生成器对象
#
#     print("lallal")
#     yield 2
#
# gen = func()
# # gen.__next__()
# # gen.__next__()
#
# a = next(gen)
# b = next(gen)
#
# print(a, b)


def order():
    for i in range(10000):
        yield "衣服" + str(i)

o = order()
print(o.send('周润发'))

