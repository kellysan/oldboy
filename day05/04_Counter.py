#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       04_Counter
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:

from collections import  Counter

c = Counter("alex is not a good man")
print(c)

list1 = ["周杰伦", "周杰伦", "周杰伦", "周杰伦", "周杰伦", "周杰伦", "周杰伦",]
d = Counter(list1)
print(d.get("周杰伦"))