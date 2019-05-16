#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       思路
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-15
#    Change Activity:  2019-05-15:


"""
1. 登陆状态需要一个数据字典  在一个终端登陆还是唯一的


2. 人员信息是一个数据字典
{"stu1":{"role:student", "login_count":0, "course课程":[1,2,3,4]},"tea1":{"role":"teacher"}}

3. 需要一个课程的数据字典
"""

course = {
    "L1":1000,
    "L2":2000
}

for item in enumerate(course.items()):
    print(item)
