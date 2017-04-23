# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
logger = logging.getLogger('SQL')

class VirusupdatePipeline(object):

	def process_item(self, item, spider):
		logger.info('insert into virus_black_list(md5,url) values (\'%s\',\'%s\');',item['md5'][0],item['url'][0])
		# self.w2f('md5_his.txt',item['md5'][0])
		return item

	def w2f(self,path,content):
		with open(path,'a+') as f:
			f.write(content + '\n')
