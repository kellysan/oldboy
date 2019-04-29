#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       main
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-21
#    Change Activity:  2019-04-21:

import os
import sys
import time

#
from homework.day04 import base as b
from homework.day04.log_conf import logger

def main():
    while True:
        b.welcome()
        try:
            num = int(input("请输入您要的操作"))
            if num == 1:
                b.login()
            elif num == 2:
                while True:
                    res = b.sign_up()
                    if res:
                        break
                    else:
                        continue
            elif num == 3:
                res = b.article()
                if res:
                    logger.info("用户:{}在{}执行了article函数".format(b.login_user(),b.now_time()))
            elif num == 4:
                res = b.diary()
                if res:
                    logger.info("用户:{}在{}执行了article函数".format(b.login_user(), b.now_time()))
            elif num == 5:
                res = b.comment()
                if res:
                    logger.info("用户:{}在{}执行了article函数".format(b.login_user(), b.now_time()))
            elif num == 6:
                res = b.collect()
                if res:
                    logger.info("用户:{}在{}执行了article函数".format(b.login_user(), b.now_time()))
            elif num == 7:
                b.logout()
            elif num == 8:
                break
            else:
                print("请输入1-8选项")
        except ValueError as e:
            print("您输入的信息有误",e)

if __name__ == '__main__':
    main()