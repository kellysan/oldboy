#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ftp_client2
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-28
#    Change Activity:  2019-05-28:
#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       ftp_client
#    Description :
#    Author :          SanYapeng
#    date：            2019-05-28
#    Change Activity:  2019-05-28:

import socket
import hmac

def user_auth(conn, buffer_size = 1024):
    user_name = input("请输入名称：")
    hash_user_name = user_name.encode('utf-8')
    conn.send(user_name.encode('utf-8'))
    user_password = input("请输入密码：")
    h = hmac.new(hash_user_name, user_password.encode('utf-8'))
    digest = h.digest()
    conn.send(digest)
    server_res = conn.recv(buffer_size)
    print(server_res)
    if server_res.decode('utf-8'):
        return True
    else:
        return False

def client_handler(ip_port, buffer_size=1024):
    ftp_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    ftp_client.connect(ip_port)
    if user_auth(ftp_client):

        while True:
            data = input("请输入要转换的字符>>").strip()
            if not data:continue
            if data == 'q' or data == 'quit':break
            ftp_client.send(data.encode('utf-8'))
            res = ftp_client.recv(buffer_size)
            print(res.decode('utf-8'))

    # 关闭socket 连接
    ftp_client.close()
    return

if __name__ == '__main__':
    ip_port = ("127.0.0.1", 8100)
    buffer_size = 1024
    client_handler(ip_port, buffer_size)