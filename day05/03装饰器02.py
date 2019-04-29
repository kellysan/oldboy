#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       04
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:


def log_out(args='default.log'):
    def log(fn):
        def wrapper(*args, **kwargs):
            ret = fn(*args, **kwargs)
            print("文件记录在",args)
            return ret
        return wrapper
    return log


def func1():
    print("我是func1")


def func2():
    print("我是func2")