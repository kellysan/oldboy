#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       10_json
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-27
#    Change Activity:  2019-04-27:


import json
#
# dic = {"伞亚朋":"九公子", "霍文彬":"霍爷","美术":None, "历史":False, "数学":True}
#
# j = json.dumps(dic, ensure_ascii=False)
#
# print(j)

s = '{"伞亚朋": "九公子", "霍文彬": "霍爷", "美术": null, "历史": false, "数学": true}'
dic = json.loads(s)

print(dic)