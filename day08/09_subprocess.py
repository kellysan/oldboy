#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       09_subprocess
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-25
#    Change Activity:  2019-05-25:

import subprocess

cmd = input("请输入命令：")

conn = subprocess.Popen(
    cmd,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
print("正确输出：{}".format(conn.stdout.read().decode("utf-8")))
print("错误输出：{}".format(conn.stderr.read().decode("utf-8")))