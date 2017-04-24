# -*- coding:utf-8 -*-
import urllib2
import json

class Crawler(object):
	"""docstring for Crawler"""
	def __init__(self):
		self.start_url = 'https://appstore.anva.org.cn/Login/getBlackList?starttime=&endtime=&type=all&md5=&limit=20'
		self.url_base = 'https://appstore.anva.org.cn/Login/getUrlList?md5='
		self.page_base = 'https://appstore.anva.org.cn/Login/getBlackList?starttime=&endtime=&type=all&md5=&limit=20'
		self.elem = {}

	def total_elem(self):
		jsons = self.load_page(self.start_url)
		return int(jsons['total'])

	def load_page(self,url):
		try:
			html = urllib2.urlopen(url)
		except Exception, e:
			html = urllib2.urlopen(url)
		return json.loads(html.read())

	def crawl_manager(self):
		totalElem = self.total_elem()
		if totalElem % 20 == 0:
			pages = totalElem/20
		else:
			pages = totalElem/20 + 1
		for page in range(1,pages + 1):
			print page 
			page_link = self.page_base + '&page='+str(page)
			self.get_item(page_link)

	def get_item(self,page_link):
		jsons = self.load_page(page_link)
		page = int(jsons['page_now'])
		for item in jsons['list']:
			seq = int(item['seq'])
			self.elem['md5'] = item['md5']
			self.elem['add_time'] = item['add_time']
			self.elem['cn_vname'] = item['cn_vname']
			self.elem['type'] = item['type'].encode('utf-8')
			self.elem['firsttime'] = item['firsttime']
			self.elem['market_name'] = item['market_name'].encode('utf-8')
			url_info = self.url_base + item['md5']
			self.get_url_info(url_info)
		return page,seq

	def get_url_info(self,link):
		jsons = self.load_page(link)[0]
		self.elem['app_name'] = jsons['app_name'].encode('utf-8')
		self.elem['url'] = jsons['url']
		self.elem['market_id'] = jsons['market_id']
		self.elem['state'] = jsons['state'].encode('utf-8')
		self.handle_elem()
		self.elem = {}

	def handle_elem(self):
		for k,v in self.elem.items():
			print k + '=' + v 

	def run(self):
		self.crawl_manager()

obj = Crawler()
obj.run()


