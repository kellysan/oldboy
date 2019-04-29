#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       09_pickle
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:

import pickle

lst = ["张一山", "杨紫", "周冬雨"]

bs = pickle.dumps(lst)
pickle.dump(lst, open("regedit.dat" ,"wb"))
bs1 = pickle
print(bs)

b = b'\x80\x03]q\x00(X\t\x00\x00\x00\xe5\xbc\xa0\xe4\xb8\x80\xe5\xb1\xb1q\x01X\x06\x00\x00\x00\xe6\x9d\xa8\xe7\xb4\xabq\x02X\t\x00\x00\x00\xe5\x91\xa8\xe5\x86\xac\xe9\x9b\xa8q\x03e.'
obj = pickle.loads(b)

obj1 = pickle.load(open("regedit.dat" ,"rb"))
print(obj)
print(obj1)