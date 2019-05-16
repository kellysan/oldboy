#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       08_继承
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-11
#    Change Activity:  2019-05-11:

class Father(object):
    def run(self):
        print("飞")

class Son(Father):
    pass


erzi = Son()
erzi.run()