#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       wrapper
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-17
#    Change Activity:  2019-05-17:

import os
from homework.day06.zuoye import base

db = base.Database()

def account(flag):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            if flag == "sign_up":
                user_info = db.db_select('user_info.json')
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
                return func(user_name, user_password, *args, **kwargs)

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
