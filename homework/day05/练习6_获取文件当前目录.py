#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       练习6_获取文件当前目录
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-01
#    Change Activity:  2019-05-01:


import sys

#获取当前列表
path= sys.path[0]

print(path)

#获取脚本名称
print(sys.argv[0])


