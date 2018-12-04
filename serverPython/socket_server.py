#!/usr/bin/env python
# coding=utf8

import socketserver

class myTCPhandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).decode('UTF-8', 'ignore').strip()
            if not self.data : break
            print(self.data)
            self.feedback_data =("回复\""+self.data+"\":\n\t你好，我是Server端").encode("utf8")
            self.request.sendall(self.feedback_data)

host = ''
port = 10087
server = socketserver.ThreadingTCPServer((host,port),myTCPhandler)
server.serve_forever()
