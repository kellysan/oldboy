#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       11_os
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:

import os

#os.makedirs("abc/def") # 创建多级文件夹
#os.removedirs("abc/def")  # 删多级目录，前提上层必须为空
#os.rmdir("abc/def")  #删东西尽可能少

#print(os.listdir("abc"))  #列出所有文件和文件
# os.stat()

# os.system("ls")
# res = os.popen("ls")  #执行命令有返回值
# res = os.getcwd()  #获取当前脚本执行目录
# print(res)
#
# os.chdir('/Users/kelly/code/oldboy/')  # 改变工作目录
# res = os.getcwd()
# print(res)

# print(os.path.abspath('abc'))  #获取绝对路径
# print(os.path.split("/Users/kelly/code/oldboy/day05")) #将路径切割，区分文件和路径，加/ 是目录，不加是文件
#
# print(os.path.exists("abc")) #判断文件或目录是否存才
#
# print(os.path.isfile("abc"))
# print(os.path.isdir("abc"))
# print(os.path.join("/User/kelly","code","oldboy"))
# print(os.path.getsize("abc"))

#### 树形遍历

def func(filepath, n):
    os.listdir(filepath)
