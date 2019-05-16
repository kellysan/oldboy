#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       银行账户
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-11
#    Change Activity:  2019-05-11:



class account:
    def __init__(self, name, id, password):
        self.name = name
        self.password = password
        self.id = id

    def cun(self, money):
        print("{}存入{}".format(self.name, money))

    def qu(self, money):
        print("{}取出{}".format(self.name, money))

    def cha(self):
        print("{}余额还有xxxx".format(self.name))



if __name__ == '__main__':
    a = account("alex", 2345678 , 123456)
    a.cun(10000)
    a.qu(1000)
    a.cha()