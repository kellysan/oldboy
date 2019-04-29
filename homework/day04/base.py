#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       base
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-21
#    Change Activity:  2019-04-21:


import json
import os
import time
from homework.day04.log_conf import logger

def welcome():
    message = """
    欢迎来到博客园首页
    1. 登录
    2. 注册
    3. 文章页面
    4. 日记页面
    5. 评论页面
    6. 收藏页面
    7. 注销
    8. 退出程序
    """
    print(message)



"""
 基础函数区
"""
def now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def login_user():
    with open("login.lock","r") as f:
        return f.read().strip("\n")

def write_json(user_info):
    file = "register.json"
    with open(file,"w") as f:
        json.dump(user_info, f)


def read_json():
    file = "register.json"
    with open(file, "r") as f:
        return json.load(f)


def read_file():
    with open("login.lock", "r") as f:
        return f.read().strip("\n")


def create_login_lock_file(file_info):
    """
    创建锁文件
    :param file_info:
    :return:
    """
    with open("login.lock", "w") as f:
        f.write(file_info)

"""
装饰器
"""

# def account(func):
#     def wrapper(*args, **kwargs):
#         user_name = input("请输入您的账户:").strip()
#         user_password = input("请输入您的密码：").strip()
#         return func(user_name, user_password, *args , **kwargs)
#     return wrapper

def account(flag):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            if flag == "sign_up":
                user_info = read_json()
                print(user_info)
                user_name = input("请输入你要注册的账户:").strip()
                if user_name not in user_info:
                    user_password1 = input("请输入您的密码：").strip()
                    user_password2 = input("请再次输入您的密码").strip()
                    if user_password1 == user_password2:
                        user_password = user_password2
                        return func(user_name, user_password, *args, **kwargs)
                    else:
                        print("用户名密码不一致，请重新输入！")
                        return False
                else:
                    print("该用户已经注册，请登录")
                    return False
            elif flag == "login":
                user_name = input("请输入您的账户:").strip()
                user_password = input("请输入您的密码：").strip()
                return func(user_name, user_password, *args , **kwargs)
        return inner_wrapper
    return wrapper

def check_count(func):
    def wrapper():
        count = 0
        while count <= 3:
            res = func(count)
            if res[0]:
                break
            else:
                count = res[1]
                continue
    return wrapper


def check_login_status(func):
    def wrapper():
        if os.path.exists('login.lock'):
            func()
        else:
            print("您还没有登录，请登录")
            return False
    return wrapper


"""
功能函数去
"""

@account("sign_up")
def sign_up(name, password,):
    """
    注册用户，并将数据写入信息数据库，并创建登录锁，表示系统已经登录
    :param name: 注册用户
    :param password: 注册密码
    :return: 成功返回 True 存在返回 False
    """
    # 获取的注册的user信息
    user_register = read_json()

    # 定义一个用户注册信息模板
    user_info_dict = {"password":password, "login_count":0}

    # 将用户信息写入注册信息字典
    user_register[name] = user_info_dict

    # 把用户信息写入文件中
    write_json(user_register)

    # 创建用户登录的锁文件，要求注册即登录
    create_login_lock_file(name)

    # 提示注册成功
    print("{}用户注册成功.".format(name))
    return True


@check_count
@account("login")
def login(user_name, user_password, count):
    user_info = read_json()
    if user_name not in user_info:
        print("用户没有注册请注册用户,请去注册页面注册用户")
        return True, 0

    if user_info[user_name]['login_count'] >= 3:
        print("您的账户已经被锁定，不能登录")
        return True, 0

    if user_password == str(user_info[user_name].get("password")):

        # 登录成功后，创建所文件，文件是可以覆盖的
        create_login_lock_file(user_name)
        print("{}登陆成功".format(user_name))

        # 登陆成功后改变用户信息状态  n
        user_info[user_name]["login_count"] = 0
        # 调试 print('登录成功信息', user_info)

        # 将登陆后的信息写入数据库
        write_json(user_info)
        return True, 0
    else:
        count += 1
        user_info[user_name]["login_count"] = count
        print('登录失败,您输入的账户和密码不匹配！')
        # 写入数据
        write_json(user_info)
        return False, count


@check_login_status
def logout():
    user_name = read_file()
    os.remove('login.lock')
    print("{} 用户注销成功".format(user_name))


@check_login_status
def article():
    message = """
    您正在访问文章列表页面
    1. python的数据类型
    2. python的函数
    3. python字符串的基本操作
    """
    print(message)
    logger.info("欢迎{}用户访问文章页面。".format(login_user()))


@check_login_status
def diary():
    print("您正在访问日记页面")
    logger.info("欢迎{}用户访问日记页面。".format(login_user()))


@check_login_status
def comment():
    print("您正在访问评论页面")
    logger.info("欢迎{}用户访问评论页面。".format(login_user()))


@check_login_status
def collect():
    print("您正在访问收藏页面")
    logger.info("欢迎{}用户访问收藏页面。".format(login_user()))


if __name__ == '__main__':
    pass
