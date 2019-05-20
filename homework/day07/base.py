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

class Message:

    @staticmethod
    def welcome():
        message = """
        欢迎来到老男孩学员信息管理系统
                1. 登录
                2. 注册
                3. 注销
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

class Base:
    @staticmethod
    def write_file(file, file_info):
        with open(file, "2") as f:
            f.write(file_info)

    @staticmethod
    def read_file(file):
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
    def name():
        res = input("请输入姓名：")
        return res

    @staticmethod
    def age():
        age_rgx = re.compile(r"\d{1,3}$")
        res = input("请输入的年龄：")
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

class InfoMode(Base):

    def create_mode(self, prefix, value):
        return dict(zip(prefix, value))

    def info_mode(self, type):
        """

        :return: 根据输入的类型返回对应模板信息
        """
        if type == "staff":
            prefix_list = ["password","login_count","age","position","ctime","type","class"]
            value_list = [None, 0, None, None, self.get_timestamp, None, []]
            return self.create_mode(prefix_list, value_list)

        elif type == "stu":
            prefix_list = ["password","login_count","age","ctime","type","class", "ctime"]
            value_list = [None, 0, None, self.get_timestamp, "stu", [], self.get_timestamp]
            return self.create_mode(prefix_list, value_list)

        elif type == "course":
            prefix_list = ["price", "hour", "outline", "ctime"]
            value_list = [None, None, [], self.get_timestamp]
            return self.create_mode(prefix_list, value_list)

        elif type == "class":
            prefix_list = ["semester", "course", "teacher", "student", "ctime"]
            value_list = [None, None, [], [], self.get_timestamp]
            return  self.create_mode(prefix_list, value_list)


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
            staff_dict = self.info_mode(type)
            staff_dict["password"] = kwargs["password"]
            staff_dict["age"] = kwargs["age"]
            staff_dict["position"] = kwargs["position"]
            staff_dict["type"] = kwargs["type"]
            return staff_dict

        elif type == "stu":
            stu_dict = self.type_mode(type)
            stu_dict["password"] = kwargs["password"]
            stu_dict["age"] = kwargs["age"]

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
    s = Service()
    print(s.write_info(type="class"))
