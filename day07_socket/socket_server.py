#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       socket_server
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-06
#    Change Activity:  2019-05-06:


import socket
import os
server = socket.socket()

server.bind(('localhost', 6969))
server.listen()  # 监听
print("我在等待电话")

while True:
    conn, addr = server.accept()  # 等待
    print(conn)
    print(addr)
    print("电话来了")

    while True:
        data = conn.recv(1024)
        if not data:
            print("client is close")
            break
        # print("recv:", data)
        # 执行命令
        res = os.popen(str(data)).read()
        conn.send(res)

    server.close()
