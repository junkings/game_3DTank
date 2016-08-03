#!/usr/bin/python
#encoding:utf-8
#author:jim
import socket
import struct
'''
class test_str():
    def test(self):
        a = [0,'ab',2.7]
        print len(a)
        p = struct.Struct('I 2s f')
        data = p.pack(*a)
        print len(data)
        return data
'''
HOST='127.0.0.1'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
while 1:
    cmd=raw_input("Please input cmd:")       #与人交互，输入命令

    try:
        #pack_t = struct.pack('<I',int(cmd))
        #a = test_str()
        s.sendall(cmd)      #把命令发送给对端
        data=s.recv(1024)     #把接收的数据定义为变量
        print data         #输出变量
        if data == 'done':
            break
    except Exception as e:
        print e

s.close()   #关闭连接
'''
class test_str():
    def test(self):
        return self.__setattr__([1,2,3])
'''