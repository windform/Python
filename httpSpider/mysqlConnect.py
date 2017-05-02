# -*- coding: utf-8 -*-
import mysql.connector

class MysqlConnect():
	#构造函数
	def __int__(self,path):
		self.path = path

	#连接数据库
	def connectDataBase():
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
		for value in values:
			print 'id:' + str(value[0]) + ', username: ' + value[1] + ',password: ' + value[2]
		cnx.close()

info = MysqlConnect('hello')
info.connectDataBase()



