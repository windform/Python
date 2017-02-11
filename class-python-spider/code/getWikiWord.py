#_*_coding:utf-8_*_

import urllib as u
from bs4 import BeautifulSoup as bbs
import re
import pymysql.cursors

resp = u.urlopen('http://www.ldyna.com/').read()
soup = bbs(resp,'html.parser')
listUrl = soup.find_all('a',rel = "bookmark")
#print soup.prettify()
'''
for urllink in listUrl:
	if (urllink.string != None):
		# print 'title:' + urllink.string + ',link:' + urllink['href']
		# 连接数据库
		connection = pymysql.connect(host='localhost',user='root',password='',db='wiki',charset='utf8')
		try:
		    with connection.cursor() as cursor:
		        # Create a new record
		        sql = "INSERT INTO `urls` (`urlname`, `urlhref`) VALUES (%s, %s)"
		        cursor.execute(sql, (urllink.string , urllink['href']))
		    connection.commit()
		finally:
		    connection.close()
'''
connection = pymysql.connect(host='localhost',user='root',password='',db='wordpress',charset='utf8')
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "SELECT * FROM `wp_posts`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print result
    #connection.commit()
finally:
    connection.close()