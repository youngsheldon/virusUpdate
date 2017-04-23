# -*- coding:utf-8 -*-
import urllib2
import json
import commands

def get_online_total():
	target_website = r'https://appstore.anva.org.cn/Login/getBlackList?starttime=&endtime=&type=all&md5=&limit=20'
	try:
		html = urllib2.urlopen(target_website)
	except Exception, e:
		html = urllib2.urlopen(target_website)
	hjson = json.loads(html.read())
	return int(hjson['total'])

def modify_total(total):
	with open('scrapy.cfg','r') as f:
		lines = f.readlines()
	with open('scrapy.cfg','w') as f:
		for line in lines:
			if 'total=' in line:
				continue
			f.write(line)
		f.write('total=' + str(total) + '\n')

def get_local_total():
	with open('scrapy.cfg','r') as f:
		for line in f:
			v = line.strip()
			if 'total=' in line:
				return int(line.split('=')[1])

def check_update():
	online_total = get_online_total()
	local_total = get_local_total()
	if online_total != local_total:
		commands.getoutput('scrapy crawl virus')
		modify_total(online_total)

check_update()

