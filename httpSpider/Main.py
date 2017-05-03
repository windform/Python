# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
import mysql.connector
from Application import *
from Spider import *

class Main:

	def __init__(self):
		#,self.handle.application
		self.data = []
		httpd = make_server('',1234,self.handle)
		print('Server HTTP on port 1234...')
		#Application类的实例化
		self.app = Application()
		#Spider类的实例化
		self.spider = Spider()
		httpd.serve_forever()

	def handle(self,environ, start_response):
		start_response('200 ok', [('Content-Type','text/html')])
		info = (environ['PATH_INFO'][1:])
		if info == 'a':
			responseInfo = 'aaaaa'
		elif info == 'b':
			responseInfo = 'bbbbb'
		elif info == 'c':
			self.data = self.connectDataBase()
			responseInfo = self.data
		elif info == 'e':
			value = self.app.printData()
			responseInfo = value
		elif info == 'spider':
			spiderData = self.spider.start()
			#打开文件，如果不存在，则创建
			file = open('baidu.html','w+')
			#在创建的文件中写入数据
			file.write(spiderData)
			#关闭文件
			file.close()
			responseInfo = '文件写入成功'
		else:
			responseInfo = '什么鬼'
		return responseInfo

	def connectDataBase(self):
		config = {
		  'user': '',
		  'password': '',
		  'host': '127.0.0.1',
		  'database': 'test',
		  'raise_on_warnings': True,
		}
		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()
		name = 'lily'
		cursor.execute("select * from node")
		values = cursor.fetchall()
		return str(values)
		'''
		for value in values:
			print 'id:' + str(value[0]) + ', username: ' + value[1] + ',password: ' + value[2]
		'''
		cnx.close()

main = Main()