#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       04_qq_client2
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-25
#    Change Activity:  2019-05-25:

import socket

client = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ("127.0.0.1", 8002)
while True:
     msg = input("客户端说：")
     client.sendto(msg.encode("utf-8"),ip_port)
     conn, addr = client.recvfrom(1024)
     print("%s:%s 说:%s" %(addr[0], addr[1],conn.decode("utf-8")))