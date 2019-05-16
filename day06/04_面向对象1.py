#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       04_面向对象1
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-11
#    Change Activity:  2019-05-11:

class Car:

    def fly(self):
        print("车会飞")

    def run(self):
        print("车会跑")

    def gotohell(self):
        print("上西天")



if __name__ == '__main__':
    c1 = Car()

    c1.run()
    c1.fly()
    c1.gotohell()
