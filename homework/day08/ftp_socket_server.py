#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ftp_socket_server
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-28
#    Change Activity:  2019-05-28:
import socketserver
import hmac

user_info = {'sanyapeng':871623,'user01':123456}

class Myserver(socketserver.BaseRequestHandler):

    def user_auth(self, conn, buffer_size):
        """
        用户登录认证
        :param conn:
        :return:
        """
        print("开始验证用户")
        user_name = conn.recv(buffer_size)
        print(user_name)
        if user_name.decode('utf-8') not in user_info:
            return False
        h = hmac.new(user_name, str(user_info[user_name.decode('utf-8')]).encode('utf-8'))
        digest = h.digest()
        res = conn.recv(len(digest))
        print(1111, res)
        return hmac.compare_digest(res, digest)

    def handle(self):
