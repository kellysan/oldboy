#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       dytt
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-28
#    Change Activity:  2019-04-28:


# from urllib.request import urlopen
import requests
import re
import ssl
import os
import time
ssl._create_default_https_context = ssl._create_unverified_context


base_domain_name = "https://www.dytt8.net"
#base_url = "https://www.dytt8.net/html/gndy/dyzz/"
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
    return rgx.finditer(content.text)

def get_details_url():

    # dytt_details_rgx = re.compile(r"(?P<page>/\w+/gndy/dyzz/\d+/\d+.html)", re.S)
    dytt_details_rgx = re.compile(r"(?P<url>/\w+/gndy/dyzz/\d+/\d+.html)", re.S)
    dytt_text_rgx = re.compile(r"<!--{start:最新电影下载-->(?P<page>.*)<!--}end:最新电影下载--->", re.S)
    page_text = dytt(base_domain_name, dytt_text_rgx)
    for page in page_text:
        details = dytt_details_rgx.finditer(str(page.group("page")))
        for uri in details:
            yield base_domain_name + str(uri.group("url"))


def get_move_info():
    obj_txt = re.compile(r'<!--Content Start-->(.*?)</a></td>', re.S)
    obj_name = re.compile(r'.*?◎片　　名(?P<name>.*?)<br />◎年　　代.*', re.S)
    movie_info_list = []
    for url in get_details_url():
        movie_info_dict = {}
        for item in dytt(url, obj_txt):
            for i in  obj_name.finditer(item.group(1)):
                print(111, i.group("name"))

            # print(item.group())
            # movie_info_dict["name"] = item.group(1)
            # # movie_info_dict["actor"] = item.group("actor").replace("<br />", " ").replace("&nbsp"," ").split()
            # # movie_info_dict["url"] = item.group("url")
            # print(movie_info_dict)
        # movie_info_list.append(movie_info_dict)
    return movie_info_list

if __name__ == '__main__':
    print(get_move_info())