#!/usr/bin/python
#encoding:utf-8

import socket

class simpleHost(object):

    def __init__(self):
        self.list_client = []
        self.del_list = []
        self.Host_ip = '127.0.0.1'
        self.Port = 50007
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.setblocking(0)
        self.s.bind((self.Host_ip,self.Port))
        self.s.listen(0)

        

    def process(self):
        self.handlerNewClient()
        self.ReceiveData()
    

    def handlerNewClient(self):
        try:
            conn, addr = self.s.accept()  # 接受TCP连接，并返回新的套接字与IP地址
            conn.setblocking(0)
            print("connect by",addr)
            self.list_client.append(conn)
        except Exception as e:
            pass

    def ReceiveData(self):
        flag = False
        # print len(self.list_client)
        for i in range(len(self.list_client)):
            conn = self.list_client[i]
            if conn==None:
                return
            try:
                data = conn.recv(1024)
                if len(data) == 0:
                    conn.close()
                # print len(data)
                print data


                if data == 'close':
                    conn.sendall('done')
                    conn.close()  # 关闭连接
                    print i
                    self.del_list.append(i)
                    print self.del_list
                    flag = True
                else:
                    conn.sendall(data)
            except Exception as e:
                pass

        if flag==True:
            self.DelClient()

    def DelClient(self):
        print self.del_list
        for i in range(len(self.del_list)):
            del self.list_client[self.del_list[i]]

        self.del_list = []


