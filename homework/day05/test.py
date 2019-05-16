#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       test
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-01
#    Change Activity:  2019-05-01:

import requests
import re
from urllib.request import urlopen
obj = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br />.*?◎主　　演(?P<arts>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><font color="#ff0000"><a href="(?P<url>ftp.*?)">', re.S)

#obj = re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><font color="#ff0000"><a href="(?P<url>ftp.*?)">', re.S)
#obj = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br />.*?◎主　　演(?P<actor>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><font color="#ff0000"><a href="(?P<url>ftp.*?)">',re.S)
#obj = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br />.*?◎主　　演(?P<actor>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><font color="#ff0000"><a href="(?P<url>ftp.*?)">',re.S)
#obj = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br />.*?◎主　　演(?P<actor>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><font color="#ff0000"><a href="(?P<url>ftp.*?)">',re.S)
url = "https://www.dytt8.net/html/gndy/dyzz/20190429/58530.html"
# content = requests.get(url)
# content.encoding = "gbk"
# print(content.text)
content = urlopen(url).read().decode("gbk")
print(content)
for i in obj.finditer(content):
    print(i)
    print(i.group("url"))
    print(i.group("name"))
    print(i.group("actor"))