#!/usr/bin/python
# encoding:utf-8

import socket
import cPickle

class simpleClent(object):
    def __init__(self):
        self.Host_ip = '127.0.0.1'
        self.Port = 50007
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.Host_ip,self.Port))
        self.s.setblocking(0)



    def sendData(self,str1,pos):
        try:
            # pack_t = struct.pack('<I',int(cmd))
            # a = test_str()
            # send_data = {
            #     'data':str1,
            #     'uid':pos
            # }
            # dump_data = cPickle.dumps(send_data)
            # print dump_data
            # print cPickle.loads(dump_data)
            # self.s.sendall(cPickle.dumps(send_data))  # 把命令发送给对端
            self.s.sendall(str1)

            # data = self.s.recv(1024)  # 把接收的数据定义为变量
            # print data  # 输出变量
            # if data == 'done':
            #     self.close()
        except Exception as e:
            print e



    def ReceiveData(self):
        try:
            data = self.s.recv(1024)
            print data
        except Exception as e:
            print e

    def close(self):
        self.s.close()


