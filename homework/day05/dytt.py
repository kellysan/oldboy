#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       dytt
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-28
#    Change Activity:  2019-04-28:


from urllib.request import urlopen
import requests
import re
import ssl
import os
import time
ssl._create_default_https_context = ssl._create_unverified_context


base_domain_name = "https://www.dytt8.net/"
base_url = "https://www.dytt8.net/html/gndy/dyzz/"
index_url = "https://www.dytt8.net/html/gndy/dyzz/index.html"
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
##
## 详情 details
def dytt(urlinfo,rgx):
    """
    基础函数用来执行打开网页
    :param urlinfo: url信息
    :param rgx: 正则匹配信息
    :return: 返回匹配到的可迭代信息
    """
    content = requests.get(urlinfo, headers=headers)
    content.encoding = "gbk"
    #content = urlopen(urlinfo).read().decode("gbk")
    #print(content.text)
    return rgx.finditer(content.text)



def get_gndy_list_url():
    dytt_gndy_list_rgx = re.compile(r"(?P<list>list.*?.html)", re.S)
    gndy_uri = dytt(index_url, dytt_gndy_list_rgx)
    for uri in gndy_uri:
        yield os.path.join(base_url, uri.group("list"))



def get_details_url():
    dytt_details_rgx = re.compile(r"(?P<page>/\w+/gndy/dyzz/\d+/\d+.html)", re.S)
    for url in get_gndy_list_url():
        details_uri = dytt(url, dytt_details_rgx)
        for uri in details_uri:
            yield base_domain_name + uri.group("page")


def get_move_info():
    obj = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br />.*?◎主　　演(?P<actor>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><font color="#ff0000"><a href="(?P<url>ftp.*?)">', re.S)
    movie_info_list = []
    for url in get_details_url():
        it = dytt(url, obj)
        movie_info_dict = {}
        for item in it:
            movie_info_dict["name"] = item.group("name")
            movie_info_dict["actor"] = item.group("actor").replace("<br />", " ").replace("&nbsp"," ").split()
            movie_info_dict["url"] = item.group("url")
            print(movie_info_dict)
        movie_info_list.append(movie_info_dict)
        time.sleep(4)

    return movie_info_list

if __name__ == '__main__':

    list = get_move_info()
    print(list)