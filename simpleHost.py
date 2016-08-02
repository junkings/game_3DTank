#!/usr/bin/python
#encoding:utf8

import socket

class simpleHost(object):
    list_client = []
    Host_ip = '127.0.0.1'
    Port = 50007

    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.setblocking(0)
        self.s.blid((Host_ip,Port))
        self.s.listen(0)
        

    def process(self):
        conn,addr = self.s.accept()
    

    def handlerNewClient(self):
        pass    
