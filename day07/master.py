#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       master.py
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-18
#    Change Activity:  2019-05-18:


name = "alex"

def func():
    print("我是func")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def chi(self):
        print("人喜欢吃东西")


# if __name__ == '__main__':
#     print(__name__)
#     p = Person("alex", 18)
#     p.chi()