#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       03
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:


def wrapper_out(flag):
    def wrapper(func):
        def wrapper_inner(*args, **kwargs):
            if flag:
                print("问问alex，市场行情怎么样")
                res = func(*args, **kwargs)
                print("alex不靠谱")
            else:
                res= func(*args, **kwargs)
            return res
        return wrapper_inner
    return wrapper

@wrapper_out(True)
def yue():
    print("约个大美女")


@wrapper_out(False)
def lvxing():
    print("旅行")


yue()
lvxing()