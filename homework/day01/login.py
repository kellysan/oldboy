#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       login
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-25
#    Change Activity:  2019-04-25:


import getpass

count = 0
while count < 3:
    user_name = input("请输入您的姓名")
    user_password = input("请输入您的密码")
    if user_name == "sanyapeng" and user_password == 123:
        print("登录成功")
    else:
        count += 1
        print("您还剩余 %d" %(3 - count))

