#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       main.py
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-17
#    Change Activity:  2019-05-17:
import os
from base import Database,Base,Message
#from homework.day06.zuoye import school
from account import login
class Servcie:
    def __init__(self):
        self.b = Base()
        self.db = Database()
        self.message = Message()


    def run(self):
        while True:
            self.message.Welcome()
            num = int(input("请输入您要的操作："))
            if num == 1:
                login()
            elif num == 2:
                pass
            elif num == 3:
                self.b.logout()




if __name__ == '__main__':
    s = Servcie()
    s.run()
