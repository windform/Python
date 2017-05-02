# -*- coding: utf-8 -*-
import mysql.connector

username = ''

def application(environ, start_response):
	start_response('200 ok', [('Content-Type','text/html')])
	username = (environ['PATH_INFO'][1:])
	return mysqlConnect()

def pathHandle(val):
	#query = ("SELECT * FROM node WHERE username = val")
	#return mysqlConnect(query)
	return val

def mysqlConnect():
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
	return values

def returnResult(data):
	return data 

