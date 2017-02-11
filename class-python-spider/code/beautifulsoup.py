#_*_coding:utf-8_*_

#引入库
from bs4 import BeautifulSoup as bbs

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister1" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#建立对象
soup = bbs(html_doc, 'html.parser')
#格式化
soup.prettify()

#print soup.title
print soup.find_all('a', class_="sister1")

for link in soup.find_all('a'):
	print link['href']
