# _*_coding:utf8_*_

import urllib2
import re
import itertools
import urlparse

def download(url, num_retries=2):
	print 'Downloading:',url
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print 'Download error:',e.reason
		html = None
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				return download(url, num_retries - 1)
	return html

def crawl_sitemap(url):
	sitemap = download(url)
	links = re.findall('<loc>(.*?)</loc>', sitemap)
	for link in links:
		html = download(link)

#download('http://httpstat.us/500')
#crawl_sitemap('http://example.webscraping.com/sitemap.xml')
'''
max_errors = 5
num_errors = 0
for page in itertools.count(1):
	url = 'http://example.webscraping.com/view/-%d' % page
	html = download(url)
	if html is None:
		num_errors +=1
		if num_errors == max_errors:
			break
		else:
			num_errors = 0
'''
def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

link_crawler('http://baike.baidu.com/item/Python','/(view)/')