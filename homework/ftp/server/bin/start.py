#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       start
#    Description :
#    Author :          SanYapeng
#    date：            2019-06-08
#    Change Activity:  2019-06-08:

import os
import sys
import socketserver

base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
#print(base_dir)
sys.path.insert(0, base_dir)



if __name__ == '__main__':
    from core import server
    sock = socketserver.ThreadingTCPServer(('127.0.0.1', 8500),server.Server)
    sock.serve_forever()