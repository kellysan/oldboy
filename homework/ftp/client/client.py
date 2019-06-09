#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       client
#    Description :
#    Author :          SanYapeng
#    date：            2019-06-08
#    Change Activity:  2019-06-08:

import hashlib
import socket
import struct
import json
import os

class Client:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 8500

    def _get(self, data):
        """负责下载逻辑"""
        print('get_data', data)
        input()

    def _mk(self, data):
        #print('mk_data', data)
        data['action_type'] = data['choice'][0]
        self.send_msg(data)

    def _del(self, data):
        """delete dir"""
        print('rm_data', data)
        data['action_type'] = data['choice'][0]
        self.send_msg(data)
        del_data = self.recv_msg()
        if del_data.get('status_code') == 400:
            print(del_data.get('status_content'))

    def _cd(self, data):
        """切换目录"""
        print('cd_data', data)
        data['action_type'] = data['choice'][0]
        if len(data['choice']) <= 1:
            print('invalid command')
        else:
            self.send_msg(data)
            cd_data = self.recv_msg()
            if cd_data.get('status_code') == 301:
                print(cd_data.get('status_content'))
            else:
                self.handle(cd_data)


    def handle(self, data):
        """解析指令并交给具体的方法处理"""
        while True:
            #print('handle_data', data)
            #user_path = os.path.basename(data['user_path'])
            user_path = data['user_path'].replace(data['user_dir'], '')
            choice = input("[%s@%s]$" %(data['user'], user_path)).strip().split()
            if not choice:continue
            data['choice'] = choice
            if hasattr(self, '_%s' % choice[0]):
                getattr(self, '_%s' % choice[0])(data)

    def send_msg(self, data):
        head_data = json.dumps(data).encode('utf-8')
        head_size = struct.pack('i', len(head_data))
        self.request.send(head_size)
        self.request.send(head_data)

    def recv_msg(self):
        head_size = self.request.recv(4)
        st_data = struct.unpack('i', head_size)[0]
        head_data = self.request.recv(st_data).decode('utf-8')
        return json.loads(head_data)


    def connect_sock(self):
        self.request = socket.socket()
        self.request.connect((self.host, self.port),)

    def get_md5(self, pwd=None):
        return hashlib.md5(pwd.encode('utf-8')).hexdigest()

    def login(self):
        """登陆逻辑"""
        while True:
            # user, pwd = input("user:").strip(), input('pwd:').strip()
            user, pwd = 'a', 'b'
            if not user: continue
            self.get_md5(pwd=pwd)
            self.connect_sock()

            data = {
                'user': user,
                'pwd': self.get_md5(pwd=pwd),
                'action_type':'login'
            }

            self.send_msg(data)
            login_data = self.recv_msg()
            if login_data['status_code'] == 200:
                print(login_data.get('status_content'))
                print('login_data', login_data)
                self.handle(login_data)

            elif login_data['status_code'] == 201:
                print(login_data.get('status_connect'))


if __name__ == '__main__':
    c = Client()
    c.login()