#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       练习8
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-01
#    Change Activity:  2019-05-01:


import os

# 字符格式转换

def format_size(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字符格式不对")
        return "error"

    if kb > 1024:
        M = kb / 1024
        if M > 1024:
            G = M / 1024
            return "%fG" % G
        else:
            return "%fM" % M
    else:
        return "%fkb" % kb



#获取文件大小

#



print(os.path.getsize('abc/test.i2'))


