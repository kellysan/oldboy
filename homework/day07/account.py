#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       user
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-17
#    Change Activity:  2019-05-17:

import os
from base import Database
from wrapper import  account,check_count

db = Database()


def create_login_lock_file(file_info):
    """
    创建锁文件
    :param file_info:
    :return:
    """
    with open("login.lock", "w") as f:
        f.write(file_info)


@check_count
@account("login")
def login(user_name, user_password, count):
    user_info = db.db_select("user_info.json")
    if user_name not in user_info:
        print("用户没有注册请注册用户,请去注册页面注册用户")
        return False, 0
    else:
        if user_info[user_name]['login_count'] >= 3:
            print("您的账户已经被锁定，不能登录")
            return False, 0
        else:
            if user_password == str(user_info[user_name].get("password")):

                # 登录成功后，创建所文件，文件是可以覆盖的
                create_login_lock_file(user_name)
                if os.path.exists("login.lock"):
                    print("{}登陆成功".format(user_name))
                    # 登陆成功后改变用户信息状态  n
                    user_info[user_name]["login_count"] = 0
                    # 调试 print('登录成功信息', user_info)

                    # 将登陆后的信息写入数据库
                    db.db_insert("user_info.json", user_info)
                    return True, 0

                else:
                    print("{}登录失败,系统错误".format(user_name))
                    return False, 0


            else:
                if user_info[user_name].get("mold") == "admin":
                    print("登陆失败{}管理员账户密码不匹配".format(user_name))
                    return False, 0
                else:
                    count += 1
                    user_info[user_name]["login_count"] = count
                    print('登录失败,您输入的账户和密码不匹配！')
                    # 写入数据
                    db.db_insert("user_info.json", user_info)
                    return False, count



# def register(name, password):
#     """
#     注册用户，并将数据写入信息数据库，并创建登录锁，表示系统已经登录
#     :param name: 注册用户
#     :param password: 注册密码
#     :return: 成功返回 True 存在返回 False
#     """
#     # 获取的注册的user信息
#     user_register = db.db_select("user_info.json")
#
#     # 定义一个用户注册信息模板
#     user_info_dict = {"password": password, "login_count": 0}
#
#     # 将用户信息写入注册信息字典
#     user_register[name] = user_info_dict
#
#     # 把用户信息写入文件中
#     db.db_insert("",user_register)
#
#     # 创建用户登录的锁文件，要求注册即登录
#     create_login_lock_file(name)
#
#     # 提示注册成功
#     print("{}用户注册成功.".format(name))
#     return True

def logout():
    with open('login.lock', "r") as f:
        name = f.read().split('\n')
    os.remove('login.lock')
    print("{}用户已经注销".format(name))