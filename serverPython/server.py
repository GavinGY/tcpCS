#!/usr/bin/env python
# coding=utf8

from socket import *

host = ''
port = 12345
bufsiz = 1024

tcpSerSock = socket(AF_INET, SOCK_STREAM)   # 开启套接字
tcpSerSock.bind((host, port))               # 绑定服务端口
tcpSerSock.listen(5)                        # 开始监听

while True:
    print 'Please waiting for connection...'      # 等待客户端连接
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpCliSock.recv(bufsiz)      # 接收客户端信息
        if not data:
            break
        tcpCliSock.send('[%s] %s' % ("You send:", data))    # 给客户端发送信息
    tcpCliSock.close()

tcpSerSock.close()
