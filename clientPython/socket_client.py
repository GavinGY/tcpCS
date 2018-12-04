#!/usr/bin/env python
# coding=utf8

import socket,time

host = 'gavin.science'
port = 10087

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect((host,port))

for i in range(10):
    #sk.sendall(("你好，我是RaspberryPi No.%d" %i).encode("utf8"))
    sk.sendall(("openled").encode("utf8"))
    data = sk.recv(1024)
    print(data.decode('UTF-8', 'ignore'))
    time.sleep(2)
    i = i + 1
sk.close()
