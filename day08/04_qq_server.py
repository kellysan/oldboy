#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       04_qq_server
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-25
#    Change Activity:  2019-05-25:

import socket

ip_port =("127.0.0.1", 8002)
server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(ip_port)

while True:
    conn, addr = server.recvfrom(1024)
    print(conn, addr)
    print("%s:%s : %s" %(addr[0], addr[1],conn.decode("utf-8")))
    data = input("服务端说：")
    server.sendto(data.encode("utf-8"), addr)