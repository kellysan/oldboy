#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       base
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-15
#    Change Activity:  2019-05-15:

import json
import os
import re

class Message:

    @staticmethod
    def Welcome():
        message = """
        欢迎来到老男孩北京校区学员信息管理系统
                1. 登录
                2. 注册
                3. 注销
                """
        print(message)

    def Staff(self):
        message = """
                1. 
                  """

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
    def logout():
        with open('login.lock', "r") as f:
            name = f.read().split('\n')
        os.remove('login.lock')
        print("{}用户已经注销".format(name))

    # @staticmethod
    # def name():
    #     res = input("请输入员工\学生您的姓名：")
    #     return res
    #
    # @staticmethod
    # def age():
    #     age_rgx = re.compile(r"\d{1,3}$")
    #     res = input("请输入员工\学生的年龄：")
    #     if age_rgx.match(res):
    #         print(res)
    #         return res
    #     else:
    #         print("输入的年龄不合法：")
    #         exit(1)
    # @staticmethod
    # def position():
    #     res = input("请输入员工的职位：")
    #     return res
    #
    #
    # @staticmethod
    # def salary():
    #     res = input("请输入员工的工资：")
    #     return res
    #
    # @staticmethod
    # def school_obj():
    #     res = input("请输入员工所属校区：")
    #     return res
    # @staticmethod
    # def dept():
    #     res = input("请输入员工所属部门：")
    #     return res

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
    def __init__(self, name):
        self.name = name
        self.b = Base()
        self.d = Database()
        user_info = self.d.db_select("user_info.json")
        print(type(user_info))
        if user_info[self.name].get("type") == "staff":
            self.age = user_info[self.name].get("age")
            self.salary = user_info[self.name].get("salary")
            self.dept = user_info[self.name].get("dept")
            self.position = user_info[self.name].get('position')
            self.school_obj = user_info[self.name]["school"].get("school_name")
            print(self.school_obj)

        # self.age = self.age()
        # self.position = self.position()
        # self.salary = self.salary()
        # self.dept = self.dept()
        # self.db = Database()
        # self.type = "staff"
        # self.user_info = self.db.db_select("user_info.json")
        # self.staff_info = {"age":self.age,
        #                    "position":self.position,
        #                    "salary":self.salary,
        #                    "dept":self.dept,
        #                    "type":self.type,
        #                    "class":None,
        #                    "school":{
        #                        "school_name":None,
        #                        "class":{}
        #                        }
        #                    }
        # self.user_info[self.name] = self.staff_info
        # self.db.db_insert('user_info.json', self.user_info)

class Teacher(Staff):
    def __init__(self, name):
        super().__init__(name)

    def teaching(self, class_obj):
        print("{}老师正在讲{}".format(self.name, class_obj))

class Student:
    def __init__(self, name):
        self.name = name
        self.d = Database()
        user_info = self.d.db_select('user_info.json')
        if user_info[self.name].get("type") == "student":
            self.age = user_info[self.name]["age"]
            self.degree = user_info[self.name]['degree']
            self.class_obj = user_info[self.name]['class_obj']
            self.balance = user_info[self.name]["balance"]

class Class:
    pass

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.d = Database()
        user_info = self.d.db_select("course_info.json")
        print(user_info)
        self.price = user_info[self.course_name].get("price")
        print(self.price)


if __name__ == '__main__':
    pass