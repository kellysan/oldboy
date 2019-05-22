#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       main.py
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-17
#    Change Activity:  2019-05-17:
import os
import student
import teacher
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
                status = login()
                # 在登录的时候会写入一个lock文件，lock文件中记录着这次登录的是谁
                print(status)
                if status:
                    mold = self.b.check_login_account("mold")
                    if mold == "admin":
                        while True:
                            self.message.admin()
                            num = self.b.num()
                            if num == 1:
                                self.manager.create_course()
                            elif num == 2:
                                self.manager.create_account('stu')
                            elif num == 3:
                                self.manager.examine_all_course()
                            elif num == 4:
                                self.manager.examine_all_student()
                            elif num == 5:
                                self.manager.examine_all_student_course()
                            elif num == 6:
                                self.manager.create_account("teacher")
                            elif num == 7:
                                self.manager.allot_class("teacher")
                            elif num == 8:
                                self.manager.create_class()
                            elif num == 9:
                                self.manager.allot_class("stu")
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
                                student.examine_all_course()
                            elif num == 2:
                                student.select_course()
                            elif num == 3:
                                student.examine_select_course()
                            elif num == 4:
                                logout()
                                break
                            else:
                                print("您输入的选项有误，请重新输入")
                                continue
                    if mold == "teacher":
                        while True:
                            self.message.teacher()
                            num = self.b.num()
                            if num == 1:
                                teacher.examine_all_course()
                            elif num == 2:
                                teacher.examine_allot_class()
                            elif num == 3:
                                teacher.examine_all_class_student()
                            elif num == 4:
                                logout()
                                break
                            else:
                                print("您输入的选项有误，请重新输入")
                                continue
                elif num == 2:
                    print("注册功能未开放！:)")
                    continue
                elif num == 3:
                    logout()
                    continue

if __name__ == '__main__':
    s = Servcie()
    s.run()
