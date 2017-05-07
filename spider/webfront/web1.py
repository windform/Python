import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import html5lib
import sys
import chardet

url='http://www.toutiao.com/search_content/?offset=0&format=json&keyword=python&autoload=true&count=20&cur_tab=1'
request = urllib2.Request(url)
response=urllib2.urlopen(request)
content=response.read()
typeEncode = sys.getfilesystemencoding()
infoencode = chardet.detect(content).get('encoding','utf-8')
html = content.decode(infoencode,'ignore').encode(typeEncode)
print html


# file = open('data.json','w+')
# file.write(html)
# file.close()

'''
import gzip
import StringIO
import urllib2

ur1='http://www.toutiao.com/search_content/?offset=0&format=json&keyword=python&autoload=true&count=20&cur_tab=1'
reponse=urllib2.urlopen(ur1)
r=reponse.read()
data = StringIO.StringIO(r)
gzipper = gzip.GzipFile(fileobj=data)
html = gzipper.read()
print html
'''
'''
import urllib2
import sys
import chardet

req = urllib2.Request("http://www.163.com/")
content = urllib2.urlopen(req).read()
typeEncode = sys.getfilesystemencoding()
infoencode = chardet.detect(content).get('encoding','utf-8')
html = content.decode(infoencode,'ignore').encode(typeEncode)
print html
'''

