#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ftp_server
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-28
#    Change Activity:  2019-05-28:


import hmac,os
import socket
import hmac

user_info = {'sanyapeng':871623,'user01':123456}



def user_auth(conn, buffer_size):
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


def server_handler(ip_port, buffer_size, backlog=5):
    """
    只处理连接
    :param ip_port: 端口和绑定地址
    :param buffer_size: 读取的字节
    :param backlog: 连接客户端数
    :return:
    """
    ftp_socket_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)   # ipv4 tcp协议
    ftp_socket_server.bind(ip_port)
    ftp_socket_server.listen(backlog)
    while True:
        conn, addr = ftp_socket_server.accept()
        failed_msg = False
        access_msg = True
        print("新连接[%s:%s]" % (addr[0],addr[1]))
        if user_auth(conn, buffer_size) is False:
            print(22222)
            conn.send(b'False')
            continue
        conn.send(b'True')

        while True:
            data = conn.recv(buffer_size)
            print("需要转换的字符为：{}".format(data.decode('utf-8')))
            if not data:break
            conn.sendall(data.upper())


if __name__ == '__main__':
    ip_port = ("127.0.0.1",8100)
    buffer_size = 1024
    server_handler(ip_port, buffer_size)
