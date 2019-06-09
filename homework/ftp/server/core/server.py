#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       awecwe
#    Description :
#    Author :          SanYapeng
#    date：            2019-06-08
#    Change Activity:  2019-06-08:

import socketserver
import struct
import json
import os
import shutil

base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
#print(base_dir)

class Server(socketserver.BaseRequestHandler):

    status_code = {
        200: 'login ok',
        201: 'user or pwd error',
        400: 'del file ok',
        301: 'dir path not exist'
    }

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

    def _login(self, data):
        """负责登陆逻辑"""
        #print('login_data', data)
        with open(os.path.join(base_dir, 'db', 'userinfo'), 'r', encoding='utf-8') as f:
            for i in f:
                cmd = i.strip().split('|')
                if cmd[0] == data['user'] and cmd[1] == data['pwd']:
                    data['status_code'] = 200
                    data['status_content'] = self.status_code[200]
                    data['user_path'] = os.path.join(base_dir, 'home', data['user'])
                    data['user_dir'] = os.path.join(base_dir, 'home')
                    #print('login_in_server', data)
                    self.send_msg(data)
                    break
            else:
                data['status_code'] = 201
                data['status_content'] = self.status_code[201]
                self.send_msg(data)

    def _mk(self, data):
        """新建文件夹"""
        print('mkdir_data', data)
        dir_path = os.path.join(base_dir, 'home', data['user'])
        print('mk_in', dir_path)
        print(os.path.isdir(dir_path))
        abs_dir = os.path.join(dir_path, data['choice'][-1])
        if os.path.isdir(dir_path):
            print('mk_abs_dir', abs_dir)
            os.makedirs(abs_dir)
        else:
            os.makedirs(abs_dir)

    def _del(self, data):
        """ delete dir
        :param data:
        :return:
        """
        print('delete dir', data)
        dir_path = os.path.join(base_dir, 'home', data['user'], data['choice'][1])
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            data['status_code'] = 400
            data['status_content'] = self.status_code['400']
            self.send_msg(data)
    def _cd(self, data):
        """切换目录
        1 cd ..
        2 cd t1/t2/t3 不实现多级目录
        3 cd 不存在目录
        """
        print('cd_in', data)
        # 先判断cd ..   .. 等于 os.pardir
        if data['choice'][-1] == os.pardir:
            home_dir = os.path.join(base_dir, 'home')
            if data['user_path'] < home_dir:
                data['status_code'] = 301
                data['status_content'] = self.status_code['301']
                self.send_msg(data)
            else:
                cd_dir_path = os.path.dirname(data['user_path'])
                data['user_path'] = cd_dir_path
                self.send_msg(data)
        elif os.path.isdir(os.path.join(data['user_path'], data['choice'][-1])):
            data['user_path'] = os.path.join(data['user_path'], data['choice'][-1])
            self.send_msg(data)

        # os.sep == /
        elif data['choice'][-1] == os.sep:
            data['user_path'] = os.path.join(base_dir, 'home', data['user'])
            self.send_msg(data)
        # 切换到未知目录
        else:
            data['status_code'] = 301
            data['status_content'] = self.status_code['301']
            self.send_msg(data)

    def handle(self):
        """"""

        while True:
            data_msg = self.recv_msg()
            #print('handle_in' ,data_msg)
            if hasattr(self,'_%s' %data_msg['action_type']):
                getattr(self,'_%s' % data_msg['action_type'])(data_msg)
            else:
                print('False')
