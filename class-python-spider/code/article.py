#_*_coding:utf-8_*_

import urllib as u
from bs4 import BeautifulSoup as bbs
import re
import time
#import pymysql.cursors

resp = u.urlopen('http://www1.qdfuns.com/fearticle.php').read()
soup = bbs(resp,'html.parser')
link = soup.find('div',class_ = "p_r")

detailLink = link.find('a')['href']
detailContent = u.urlopen('http://www1.qdfuns.com/' + detailLink)
soup1 = bbs(detailContent,'html.parser')
detailMain = soup1.find('table', id="article_content")
print detailMain.find('tbody').get_text()

'''
print 'post_author: 1'
print 'post_data:' +  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print 'post_data_gmt:' +  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print 'post_content:' + detailMain.find('tbody').get_text()
print 'post_title:' + link.find('h2').get_text()
print 'post_excerpt:' + ' '
print 'post_status:' + 'publish'
print 'comment_status:' + 'closed'
print 'ping_status:' + 'closed'
print 'post_password:' + ' '
print 'post_name:' + '1-revision-v2'
print 'to_ping:' + ''
print 'pinged:' + ''
print 'post_modified:' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print 'post_modified_gmt:' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print 'post_content_filtered:' + ''
print 'post_parent:' + '252'
print 'guid' + 'url'
print 'menu_order:' + '0'
print 'post_type:' + 'revision'
print 'post_mine_type:' + ' '
print 'comment_count:' + '0'
'''


# 连接数据库
connection = pymysql.connect(host='localhost',user='root',password='',db='wordpress',charset='utf8')
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `wp_posts`(`post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) VALUES ([value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8],[value-9],[value-10],[value-11],[value-12],[value-13],[value-14],[value-15],[value-16],[value-17],[value-18],[value-19],[value-20],[value-21],[value-22],[value-23])"
        cursor.execute(sql, (urllink.string , urllink['href']))
    connection.commit()
finally:
    connection.close()

'''
for link in listUrl:
	print 'post_title:' + link.find('h2').get_text()
	print 'post_content:' + link.find('p').get_text()
'''