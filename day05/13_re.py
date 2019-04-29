#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       13_re
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:

"""
元字符
. 除了换行符匹配所有的字符
\d 匹配单个数字
\w 匹配数字，字母，下划线
\n 匹配换行
\s 匹配所有空白
^ 字符串的开始
$ 字符串的结束
[] 匹配其中的一个
[^] 取反
() 分组
数量词
* 0次多次，尽肯能的匹配
+ 1次多次
？0次或1次
{n} 表示重复n次
{n，} 表示匹配n次更多次
{n,m} 表示匹配n次到m次
"""
import re


str1 = 'homexue@126.com'
str2 = '448910663@qq.com'

str3 = "<span><div>fdsafasdfasdfsda</div></span>"
print(re.match(r'\w+@\w+\.com$', str1))
print(re.match(r'\w+@\w+\.com$', str2))
print(re.match(r'(<div>.*?</div>)', str3))


obj = re.compile(r"\w+")

print(obj.search(str1))