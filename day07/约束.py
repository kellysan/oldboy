#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       约束
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-18
#    Change Activity:  2019-05-18:

"""
1. 在父类中约束子类
    raise NotImplementedError

2. 抽象类 没有具体的实例
"""

# class Foo:
#     def login(self):
#         raise NotImplementedError("您没有重写login方法")
#
# class Member(Foo):
#     def login(self):
#         print("普通用户登陆")
#
#
# class MemnrtAdmin(Foo):
#     def login(self):
#         print("管理员登陆")
#
#
# m = Member()
# m.login()
# ma = MemnrtAdmin()
# ma.login()

## 抽象方法
from abc import ABCMeta, abstractmethod
class Foo(metaclass=ABCMeta):
    @abstractmethod
    def login(self):pass

class Member(Foo):
    def login(self):
        print("普通用户登陆")

class MemnrtAdmin(Foo):
    def login(self):
        print("管理员登陆")


m = Member()
m.login()
ma = MemnrtAdmin()
ma.login()