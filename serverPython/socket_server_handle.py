#!/usr/bin/env python
# coding=utf8

import threading
import getopt
import sys
import time
import socketserver

string_led="openled"
client_addr = []
client_socket = []
NumberCode=0
TargetNumberCode=0
cur_thread=""
N,M=10,3
SendFlag=0
TargrtSN=""

class myTCPhandler(socketserver.BaseRequestHandler):
	def setup(self):
		ip = self.client_address[0].strip()     # 获取客户端的ip        
		port = self.client_address[1]           # 获取客户端的port        
		print(ip+":"+str(port)+" is connect!")        
		#client_addr.append(self.client_address) # 保存到队列中
		#print("\nclient_addr:"+str(client_addr))

	def handle(self):
		global SendFlag,NumberCode,TargrtSN,TargetNumberCode
		while True:
			time.sleep(0.1)
			self.data = self.request.recv(1024).decode('UTF-8', 'ignore').strip()
			if not self.data : break
			cur_thread = str(threading.current_thread())
			print(cur_thread)
			NumberCode = int(cur_thread[15:16])
			print("NumberCode:"+str(NumberCode))
			L[NumberCode][0] = self.data[0:13]
			L[NumberCode][1] = self.request     # 保存套接字socket
			TargrtSN=self.data[14:27]
			print("TargrtSN:%s" %TargrtSN)
			for i in range(len(L)):
				for j in range(len(L[0])):
					if L[i][j] == TargrtSN:
						SendFlag=1
						TargetNumberCode=i
						print("TargetNumberCode:%d" %TargetNumberCode)
			if SendFlag == 0:
				print("Target Not found! maybe she is off-line !")
			#print("Tread%d SendFlag:%d" %(NumberCode,SendFlag))
			print("ProductSN L:[%d][0]:" %(NumberCode) + str(L[NumberCode][0]))
			print(self.data)
			if self.data == string_led:
				print("相等")
				#self.feedback_data =("Open LED\n").encode("utf8")
				#self.request.sendall(self.feedback_data)
			self.feedback_data =("回复\""+self.data+"\":\n\t你好，我是Server端").encode("utf8")
			self.request.sendall(self.feedback_data)
			print('运行中的列表：',L)

	def finish(self):
		print("client is disconnect!")
		# client_addr.remove(self.client_address)
		# client_socket.remove(self.request)
		for i in range(len(L)):
			print(i)
			if L[i][1] == self.request:
				print("start.remove")
				L[i][0] = 0
				L[i][1] = 0
		print('退出删除列表元素：',L)

def main_loop():
	global SendFlag,TargetNumberCode,TargrtSN
	message = ("clientTest\n").encode("utf8")
	while True:
		time.sleep(5)
		#print("Tread1 SendFlag:%d" %(SendFlag))
		if SendFlag==1:
			#print('原始列表_mainloop：',L)
			L[TargetNumberCode][1].sendall(message)
			SendFlag=0
	
def main_loop2():
	while True:
		time.sleep(1)
		#print("hello2222222222")
		
if __name__ == '__main__':
	host = ''
	port = 10087
	L=[[0 for p in range(M)] for q in range(N)]  #创建二维列表
	print('原始列表：',L)
	server = socketserver.ThreadingTCPServer((host,port),myTCPhandler) # 实现多线程通话
	t1=threading.Thread(target=main_loop)
	t2=threading.Thread(target=main_loop2)
	t1.start()
	t2.start()
	t3=threading.Thread(target=server.serve_forever())
	t3.start()

