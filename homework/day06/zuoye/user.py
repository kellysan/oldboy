#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       user
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-17
#    Change Activity:  2019-05-17:


from homework.day06.zuoye.base import Database
from homework.day06.zuoye.wrapper import  account,check_count
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
        db.db_insert("user_info.json", user_info)
        return True, 0
    else:
        count += 1
        user_info[user_name]["login_count"] = count
        print('登录失败,您输入的账户和密码不匹配！')
        # 写入数据
        db.db_insert("user_info.json", user_info)
        return False, count
