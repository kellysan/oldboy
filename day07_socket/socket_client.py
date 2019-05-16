#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       socket_client
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-06
#    Change Activity:  2019-05-06:

import socket
import os
client = socket.socket()
client.connect(('localhost', 6969))

# 单发单收
# client.send(b"hello  world")

# 多发
while True:
    msg = input(">>:").strip()
    if len(msg) == 0: continue
    # client.send(msg.encode("utf-8"))
    client.send(msg.encode("utf-8"))
    data = client.recv(1024) # 字节 1k
    print(data.decode())

client.close()
