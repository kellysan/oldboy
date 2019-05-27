#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       02_client
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-25
#    Change Activity:  2019-05-25:

import socket
client = socket.socket()
ip_port = ("127.0.0.1", 8001)
client.connect(ip_port)

client.send(b"client send")
from_server_msg = client.recv(1024)
print(from_server_msg)
