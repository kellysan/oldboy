#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       演唱会
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-11
#    Change Activity:  2019-05-11:

class Singer:
    def __init__(self, name, salary, gender, songs):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.songs = songs

    def chang_ge(self):
        print("{}在唱{}".format(self.name, self.songs))

    def yan_chang_hui(self):
        print("{}在开演唱会".format(self.name))


if __name__ == '__main__':
    wang_feng = Singer("汪峰", 2000, "男" , "汪峰的歌")
    wang_feng.chang_ge()
    wang_feng.yan_chang_hui()