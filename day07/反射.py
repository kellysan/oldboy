#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       反射
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-18
#    Change Activity:  2019-05-18:

import daniu


while True:
    gn = input("请您输入要测试的功能：")

    if hasattr(daniu, gn):
        fn = getattr(daniu, gn)
        if callable(fn):
            fn()
        else:
            print(fn)
    else:
        print("没有这个功能")