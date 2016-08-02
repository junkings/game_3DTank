#!/usr/bin/python
#encoding:utf-8
import socket   #socket模块
import time 

HOST='127.0.0.1'
PORT=50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(0)
s.bind((HOST, PORT))  # 套接字绑定的IP与端口
s.listen(0)  # 开始TCP监听

class msg():
    pass
list_client =[]
while 1:
    time.sleep(0.1)
    conn = None
    try:


        conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
        conn.setblocking(0)
        #s = None
        print'Connected by',addr ,conn    #输出客户端的IP地址
        list_client.append(conn)
    except Exception as e:
        #print e
        pass
    #print list_client
    for pos in xrange(len(list_client)):
        #print len(list_client)
        #print pos
        conn = list_client[pos]

        time.sleep(0.1)
        try:
            data=conn.recv(1024)    #把接收的数据实例化
            if len(data)==0:
                conn.close()
            # print len(data)
            #print data
            

            if data =='close':
                conn.sendall('done')
                conn.close()  # 关闭连接
                break
            else:
                conn.sendall(data)

        except Exception as e:
            pass
            #print e
            

