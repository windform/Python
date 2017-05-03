# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

class Spider:

	#构造函数
	def __init__(self):
		pass

	def start(self):
		url = 'http://www.baidu.com'
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = { 'User-Agent' : user_agent }
		try:
			request = urllib2.Request(url,headers = headers)
			response = urllib2.urlopen(request)
			val = response.read()
		except urllib2.URLError, e:
			if hasattr(e,"code"):
				val = e.code
			if hasattr(e,"reason"):
				val = e.reason
		return val
'''
spider = Spider()
spider.start()
'''