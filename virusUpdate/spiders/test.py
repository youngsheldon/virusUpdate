# -*- coding:utf-8 -*-
import urllib2
import json

def get_total():
	target_website = r'https://appstore.anva.org.cn/Login/getBlackList?starttime=&endtime=&type=all&md5=&limit=20'
	try:
		html = urllib2.urlopen(target_website)
	except Exception, e:
		html = urllib2.urlopen(target_website)
	hjson = json.loads(html.read())
	return hjson['total']

dev = 1
for i in range(1,dev + 2):
	print i