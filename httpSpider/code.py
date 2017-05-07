# -*- coding:utf-8 -*-  

#__author__ = 'xiaolong'  
import urllib  
import re  
import sys  
import chardet  
  
def GetHtml( url):  
    page = urllib.urlopen(url)  
    contex = page.read()  
    return contex  
  
  
def GetLink(html):  
    reg = r' <a href="(.+)">(.+)</a>'  
    imgre = re.compile(reg)  
    imglist = re.findall(imgre,html)  
    return imglist  
  
url = "http://www.qdfuns.com"  
get =  GetLink(GetHtml(url).decode('utf-8'))
file = open('links.html','w+')
#在创建的文件中写入数据
file.write(str(get))
#关闭文件
file.close() 
#print get
print ('文件写入成功').decode('utf-8')