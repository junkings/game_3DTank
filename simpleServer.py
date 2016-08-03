#!/usr/bin/python
#encoding:utf-8
import socket   #socket模块
import time 
import simpleHost
'''
HOST='127.0.0.1'
PORT=50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(0)
s.bind((HOST, PORT))  # 套接字绑定的IP与端口
s.listen(0)  # 开始TCP监听
'''
class msg():
    pass
simpleclient = simpleHost.simpleHost()



# list_client =[]
while 1:
    time.sleep(0.1)
    simpleclient.process()

            

