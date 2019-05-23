#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       base
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-15
#    Change Activity:  2019-05-15:

import json
import re
import time
import hashlib
import os

class Message:

    @staticmethod
    def welcome():
        message = """
        欢迎来到老男孩学员信息管理系统
                1. 登录
                2. 注册
                """
        print(message)

    @staticmethod
    def admin():
        message = """
                1. 创建课程
                2. 创建学生账号
                3. 查看所有课程
                4. 查看所有学生
                5. 查看所有学生选课情况
                6. 创建讲师
                7. 为讲师指定班级
                8. 创建班级
                9. 为学生指定班级
                10. 退出程序
                  """
        print(message)
    @staticmethod
    def teacher():
        message = """
                1. 查看所有课程
                2. 查看所教班级
                3. 查看班级中的学生
                4. 退出程序
        """
        print(message)

    @staticmethod
    def student():
        message = """
        1. 查看所有课程
        2. 选择课程
        3. 查看所选课程
        4. 退出程序
        """
        print(message)

class Base:
    def __init__(self):
        self.db = Database()

    def write_file(self, file, file_info):
        with open(file, "2") as f:
            f.write(file_info)

    def read_file(self, file):
        with open(file) as f:
            return f.read().strip('\n')

    @property
    def get_timestamp(self):
        return int(time.time())

    @staticmethod
    def md5_password(password):
        obj = hashlib.md5()
        obj.update(password.encode("utf-8"))
        return obj.hexdigest()

    @staticmethod
    def num():

        num_rgx = re.compile(r"(\d{1}$|10)")
        while True:
            num = input("请您输入操作选项")
            if num_rgx.match(num):
                return int(num)
            else:
                print("您输入的选项有误，操作选项必须是数字，请重新输入:")
                continue



    @staticmethod
    def name():
        """
        优化方向，将这些输入的功能单独出去
        :return:
        """
        res = input("请输入姓名：").strip().lower()
        return res

    @staticmethod
    def age():
        age_rgx = re.compile(r"\d{1,3}$")
        while True:
            res = input("请输入的年龄：")
            if age_rgx.match(res):
                print(res)
                return res
            else:
                print("输入的年龄不合法：")
                continue
    @staticmethod
    def password():
        """
        需要优化的功能 1 密码复杂度验证
        :return: 返回加密密码
        """
        user_password = input("请输入用户密码")
        return Base.md5_password(user_password)

    @staticmethod
    def position():
        res = input("请输入员工的职位：")
        return res

    @staticmethod
    def salary():
        res = input("请输入员工的工资：")
        return res

    # @staticmethod
    # def school_obj():
    #     res = input("请输入员工所属校区：")
    #     return res
    # @staticmethod
    # def dept():
    #     res = input("请输入员工所属部门：")
    #     return res
    @staticmethod
    def allot_class_name():
        str_class = input("请您输入要分配的班级")
        return str_class


    def check_login_account(self, type):
        """
        根据type 类型检测返回需要的结果
        :param type: name 登录用户，mold 返回用户类型
        :return:
        """
        account = self.read_file("login.lock")
        user_info = self.db.db_select("user_info.json")
        if type == "mold":
            return user_info[account][type]
        if type == "name":
            return account

class InfoMode(Base):

    def __create_mode(self, prefix, value):
        return dict(zip(prefix, value))

    def __info_mode(self, type):
        """

        :return: 根据输入的类型返回对应模板信息
        """
        if type == "staff":
            prefix_list = ["password","login_count","age","position","ctime","mold","class"]
            value_list = [None, 0, None, None, self.get_timestamp, None, []]
            return self.__create_mode(prefix_list, value_list)

        elif type == "stu":
            prefix_list = ["password","login_count","age","ctime","mold","class", "course"]
            value_list = [None, 0, None, self.get_timestamp, "stu", [], []]
            return self.__create_mode(prefix_list, value_list)

        elif type == "course":
            prefix_list = ["price", "hour", "outline", "ctime"]
            value_list = [None, None, [], self.get_timestamp]
            return self.__create_mode(prefix_list, value_list)

        elif type == "class":
            prefix_list = ["course", "teacher", "student", "ctime"]
            value_list = [None, [], [], self.get_timestamp]
            return  self.__create_mode(prefix_list, value_list)


    def write_info_to_dict(self, type, *args, **kwargs):
        """
        为写入json 配置字典
        :param type: 生成字典模板的类型分为 staff，stu，course， class
        :param args:
        :param kwargs:  所有信息参数
        :return:
        """
        if not type:
            print("没有指定生成模板类型，请添加type类型")
            exit(1)
        if type == "staff":
            staff_dict = self.__info_mode(type)
            staff_dict["password"] = kwargs["password"]
            staff_dict["age"] = kwargs["age"]
            staff_dict["position"] = kwargs["position"]
            staff_dict["mold"] = kwargs["mold"]
            return staff_dict

        elif type == "stu":
            stu_dict = self.__info_mode(type)
            stu_dict["password"] = kwargs["password"]
            stu_dict["age"] = kwargs["age"]
            return stu_dict

        elif type == "course":
            course_dict = self.__info_mode(type)
            course_dict["price"] = kwargs["price"]
            course_dict["hour"] = kwargs["hour"]
            course_dict["outline"] = kwargs["outline"]
            return course_dict

        elif type == "class":
            class_dict = self.__info_mode(type)
            class_dict["course"] = kwargs["course"]
            return class_dict

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

if __name__ == '__main__':
    b = Base()
    print(b.all_class("stu"))