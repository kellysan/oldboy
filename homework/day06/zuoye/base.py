#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       base
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-15
#    Change Activity:  2019-05-15:

import json
import re

class Base:
    @staticmethod
    def write_file(file, file_info):
        with open(file, "2") as f:
            f.write(file_info)

    @staticmethod
    def read_file(file):
        with open(file) as f:
            return f.read().strip('\n')

    @staticmethod
    def name():
        res = input("请输入员工\学生您的姓名：")
        return res

    @staticmethod
    def age():
        age_rgx = re.compile(r"\d{1,3}$")
        res = input("请输入员工\学生的年龄：")
        if age_rgx.match(res):
            print(res)
            return res
        else:
            print("输入的年龄不合法：")
            exit(1)
    @staticmethod
    def position():
        res = input("请输入员工的职位：")
        return res


    @staticmethod
    def salary():
        res = input("请输入员工的工资：")
        return res

    @staticmethod
    def school_obj():
        res = input("请输入员工所属校区：")
        return res
    @staticmethod
    def dept():
        res = input("请输入员工所属部门：")
        return res



class Database:

    @staticmethod
    def db_insert(file, value):
        with open(file, "w") as f:
            json.dump(value, f, ensure_ascii=False)

    def db_update(self):
        pass

    def db_delete(self):
        pass

    @staticmethod
    def db_select(file):
        with open(file, 'r') as f:
            return json.load(f)

class Staff(Base):
    def __init__(self):
        self.name = self.name()
        self.age = self.age()
        self.position = self.position()
        self.salary = self.salary()
        self.dept = self.dept()
        self.db = Database()
        self.type = "staff"
        self.user_info = self.db.db_select("user_info.json")
        self.staff_info = {"age":self.age,
                           "position":self.position,
                           "salary":self.salary,
                           "dept":self.dept,
                           "type":self.type,
                           "class":None,
                           "school":{
                               "school_name":None,
                               "class":{}
                               }
                           }
        self.user_info[self.name] = self.staff_info
        self.db.db_insert('user_info.json', self.user_info)

class Teacher(Staff):
    def __init__(self):
        super().__init__()

    def teaching(self, class_obj):
        print("{}老师正在讲{}".format(self.name, class_obj))

class Class:
    pass

class Course:
    pass


if __name__ == '__main__':
    #s = Staff()
    shopping = [{"L1":2000}, {"L2":4000}, {"L3":4000}]
    for i in enumerate(shopping):
        print(i)