#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       lianxi2
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-01
#    Change Activity:  2019-05-01:

import time

def assign_timestamp():

    #获取当前月份
    struct_time =  time.localtime()

    # 拼接所需要时间的格式化时间
    t1 = "{}-{}-1 00:00:00".format(struct_time.tm_year, struct_time.tm_mon)

    # 将格式化时间转换为时间戳 并返回
    return time.mktime(time.strptime(t1,"%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    print(assign_timestamp())
