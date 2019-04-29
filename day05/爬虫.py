#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       爬虫
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:

import re
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# import requests
# import urllib3
#
#content = urlopen("https://www.dytt8.net/html/gndy/dyzz/20190419/58500.html").read().decode("gbk")
content = urlopen("https://www.dytt8.net//html/gndy/dyzz/20091012/22189.html").read().decode("gbk")
#obj = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br />.*?◎主　　演(?P<arts>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<url>.*?)">',re.S)
#obj = re.compile('(?P<url>ftp.*?)">', re.S)
obj = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br />.*?◎主　　演(?P<arts>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><font color="#ff0000"><a href="(?P<url>ftp.*?)">', re.S)
#obj = re.compile(r'◎主　　演(?P<arts>.*?)<br /><br />', re.S)
it = obj.finditer(content)
for item in it:
    print(item.group("name"))
    print(item.group("arts"))
    print(item.group("url"))
# def add(a,b):
#     return a + b
#
# def test():
#     for i in range(4):
#         yield i
#
# g = test()
#
# for n in [2,10]:
#     g = (add(n,i) for i in g)
#
# n = 5
#
# print(list(g))