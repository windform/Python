# _*_ coding:utf-8 _*_

import urllib
import urllib2
import re
import mysql.connector
from bs4 import BeautifulSoup
import html5lib

soup = BeautifulSoup(open("index.html"),'html5lib')
#提取文件信息
content = soup.find(id="column-center").find_all('section')
#file = open('filter.html','w+')

config = {
  'host': 'localhost',
  'user': 'root',
  'password': '',
  'database': 'wiki',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
add_data = ("INSERT INTO article "
               "(author, title, create_time, scan_num, commentNum, desc, type) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")

for list in content:
	author = list.find('a', class_='author_link').get_text()
	title = list.find('a', class_='author_link').find_next_sibling("a").get_text()
	pubDate = list.find('div', class_='media-info').find('span',class_='hide')
	scanNum = list.find('div', class_='media-info').find_all("span")[1]
	commentNum = list.find('div', class_='media-info').find_all("span")[2]
	desc = list.find('p', class_='media-body').get_text()
	category = list.find('div', class_='media-info').find_all("span")[3].find('a')

	#data_employee = (str(author), str(title), str(pubDate), str(scanNum), str(commentNum), str(desc), str(category))
	data_employee = ('12','12','12','12','12','12','12')
	cursor.execute(add_data, data_employee)

cnx.commit()
cnx.close()