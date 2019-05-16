#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       05_面向对象
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-11
#    Change Activity:  2019-05-11:

class Persion:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print("人会跑")

    def chi(self, food):
        print("{}正在吃{}".format(self.name, food))



if __name__ == '__main__':
    c = Persion("tom", 24, "男")
    c.chi("烤鸭")
