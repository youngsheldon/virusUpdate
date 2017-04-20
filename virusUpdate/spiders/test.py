# -*- coding:utf-8 -*-
import urllib2
import json

html = urllib2.urlopen(r'https://appstore.anva.org.cn/Login/getUrlList?md5=7f0564a57fd78b8faa4a8b3648ca3651')
 
hjson = json.loads(html.read())
url_info = hjson[0]
print url_info['app_name']
print url_info['url']
print url_info['market_id']
print url_info['state'].encode('utf-8')
print url_info['market_name'].encode('utf-8')
print url_info['add_time']