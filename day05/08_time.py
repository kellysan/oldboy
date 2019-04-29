#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       08_time
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:

import time

# #获取时间戳
# print(time.time())
#
#
# #格式化时间
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
#
# print(time.strftime("%Z"))
#
# #结构化时间
#
# print(time.localtime())
#
# #时间互相转化
# # 1 时间戳获得时间
# n = 10000
# # 把时间转换为结构化时间
# struct_time1 = time.localtime(n)
# # 把结构化时间转化为时间
# s = time.strftime("%Y-%m-%d %H:%M:%S", struct_time1)
# print(s)
#
# """
# 时间戳---time.localtime(时间戳)--->结构化时间----time.strftime(format,结构化时间)--->字符串时间
# 字符串时间---time.strptime(字符串时间，format)--->结构化时间---time.mktime(结构化时间)--->时间戳
# """
# #把时间转化为字符串
# s1 = input("请输入时间格式为 年-月-日 时:分:秒：")
#
# # 把字符串转化为结构化时间
# struct_time2 = time.strptime(s1,"%Y-%m-%d %H:%M:%S")
# print(struct_time2)
# print(struct_time2.tm_year)
#
# # 将结构化时间转化为时间戳
# n = time.mktime(struct_time2)
# print(n)
#
# s1 = "1989-01-01 12:00:00"
# s2 = "1989-01-02 14:35:00"
# # print(time.strptime(s1, "%Y-%m-%d %H:%M:%S"))
# #
# #
# #
# n1 = time.mktime(time.strptime(s1, "%Y-%m-%d %H:%M:%S"))
# n2 = time.mktime(time.strptime(s2, "%Y-%m-%d %H:%M:%S"))
#
# n3 = n2 - n1
#
# hour = int(n3 // 3600)
# min = int(n3 % 3600 // 60)
#
# print("时间差值为：%s:%s" %(hour, min))
# # print(n3)
# # print(time.localtime(n3))


s1 = "1989-01-01 12:00:00"
s2 = "1989-01-02 14:35:00"
s1_miao = time.mktime(time.strptime(s1,"%Y-%m-%d %H:%M:%S"))
s2_miao = time.mktime(time.strptime(s2,"%Y-%m-%d %H:%M:%S"))
s2_s1 = s2_miao - s1_miao
print(time.localtime(s2_s1))
localtime = time.strftime("%H{}%M{}",time.localtime(s2_s1)).format("小时","分钟")
print(localtime)