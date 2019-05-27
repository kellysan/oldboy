#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       02_server
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-25
#    Change Activity:  2019-05-25:

import socket

server = socket.socket()
ip_port = ("127.0.0.1", 8001)
server.bind(ip_port)
server.listen(1024)


conn, addr = server.accept()
from_client_message = conn.recv(1024)
print(from_client_message)

conn.send(b"sever send")
conn.close()
server.close()