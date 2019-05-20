#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       main.py
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-17
#    Change Activity:  2019-05-17:

from homework.day06.zuoye.base import Database,Base,Message
from homework.day06.zuoye import school
from homework.day06.zuoye.user import login
class Servcie:
    def __init__(self):
        self.b = Base()
        self.db = Database()
        self.message = Message()

    def run(self):
        self.message.Welcome()
        login()


if __name__ == '__main__':
    s = Servcie()
    s.run()