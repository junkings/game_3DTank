#!/usr/bin/python
#encoding:utf-8
#author:jim
import socket
import struct
import simpleClient
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
client = simpleClient.simpleClent()

while 1:
    cmd=raw_input("Please input cmd:")       #与人交互，输入命令

    client.sendData(cmd, 0)
    client.ReceiveData()

client.close()   #关闭连接
'''
class test_str():
    def test(self):
        return self.__setattr__([1,2,3])
'''