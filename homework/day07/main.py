#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       main.py
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-17
#    Change Activity:  2019-05-17:
import os
from base import Database, Base, Message
from manager import Manager
from account import login, logout
class Servcie:
    def __init__(self):
        self.b = Base()
        self.db = Database()
        self.message = Message()
        self.manager = Manager()


    def run(self):
        while True:
            self.message.welcome()
            num = self.b.num()
            if num == 1:
                login()
                mold = self.b.check_login_account_mold()
                if mold == "admin":
                    while True:
                        self.message.admin()
                        num = self.b.num()
                        if num == 1:
                            self.manager.create_course()
                        elif num == 2:
                            pass
                        elif num == 3:
                            pass
                        elif num == 4:
                            pass
                        elif num == 5:
                            pass
                        elif num == 6:
                            pass
                        elif num == 7:
                            pass
                        elif num == 8:
                            pass
                        elif num == 9:
                            pass
                        elif num == 10:
                            pass
                        else:
                            print("您输入的选项有误，请重新输入")
                            continue
                if mold == "stu":
                    while True:
                        self.message.student()
                        num = self.b.num()
                        if num == 1:
                            pass
                        elif num == 2:
                            pass
                        elif num == 3:
                            pass
                        elif num == 4:
                            pass
                        else:
                            print("您输入的选项有误，请重新输入")
                            continue
                if mold == "teacher":
                    while True:
                        self.message.teacher()
                        num = self.b.num()
                        if num == 1:
                            pass
                        elif num == 2:
                            pass
                        elif num == 3:
                            pass
                        elif num == 4:
                            pass
                        else:
                            print("您输入的选项有误，请重新输入")
                            continue
            elif num == 2:
                pass
            elif num == 3:
                logout()
                continue




if __name__ == '__main__':
    s = Servcie()
    s.run()
