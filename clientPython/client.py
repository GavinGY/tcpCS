#!/usr/bin/env python
# coding=utf8

from socket import *

host = 'gavin.science'
port = 12345
bufsiz = 1024

tcpCliSock = socket(AF_INET, SOCK_STREAM)    
tcpCliSock.connect((host, port))             

while True:
    data = raw_input('> ')      
    if not data:
        break
    tcpCliSock.send(data)       
    response = tcpCliSock.recv(bufsiz)
    if not response:
        break
    print response

tcpCliSock.close()
