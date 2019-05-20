#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       加密
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-18
#    Change Activity:  2019-05-18:

import hashlib


# 加密

obj = hashlib.md5(b'a')
obj.update("alex".encode("utf-8"))
a = obj.hexdigest()
print(a)
