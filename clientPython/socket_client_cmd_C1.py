#!/usr/bin/env python
# coding=utf8

import socket
import threading

host = 'gavin.science'
port = 10087
ProductSN="A120181002A01"
TagetSN="A120181002A02"
flag = True

def main_loop():
	while True:
		# 接收数据
		data = client.recv(1024)
		# 打印接收到的数据
		print(data.decode('UTF-8', 'ignore'))

if __name__ == '__main__':
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # 生成socket对象
	client.connect((host,port)) # 链接要链接的ip和port（端口）
	t1=threading.Thread(target=main_loop)
	t1.start()
	# while循环
	while flag:
		# 获得用户输入
		msg = input("Enter your message('q' for quit):").strip() 
		# 判断是否为空
		if len(msg) == 0:  
			print("Message can't be empty")
			continue
		# 发送数据
		msg=ProductSN+"_"+TagetSN+"_"+msg
		client.send(msg.encode())
		# 判断是否为'q'
		if msg != 'q':
			#data = client.recv(1024)
			#print(data.decode('UTF-8', 'ignore'))
			print("------------------")
		else:
			# 条件为False
			flag = False

	# 关闭socket链接
	client.close()
	print('Connection is broken')

