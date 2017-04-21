# -*- coding:utf-8 -*-
import scrapy
import json 
from virusUpdate.items import VirusupdateItem
seq = 0
base = 'https://appstore.anva.org.cn/Login/getBlackList?starttime=&endtime=&type=all&md5=&limit=20'
url_base = 'https://appstore.anva.org.cn/Login/getUrlList?md5='
elem = VirusupdateItem()

class VirusUpdateSpider(scrapy.Spider):
    name = 'virus'
    start_urls = ['https://appstore.anva.org.cn/Login/getBlackList?starttime=&endtime=&type=all&md5=&limit=20']

    def parse(self, response):
        jsons = json.loads(response.body)
        for item in jsons['list']:
            deliver_dict = {}
            md5 = item['md5']
            seq = int(item['seq']) 
            url = url_base + md5 
            deliver_dict['md5'] = item['md5']
            deliver_dict['add_time'] = item['add_time']
            deliver_dict['cn_vname'] = item['cn_vname']
            deliver_dict['mal_type'] = item['type'].encode('utf-8')
            deliver_dict['first_time'] = item['firsttime']
            deliver_dict['market_name'] = item['market_name'].encode('utf-8')
            callback_elem=lambda arg1=response, arg2=deliver_dict:self.extract_url_info(arg1, arg2)
            yield scrapy.Request(url, callback=callback_elem)
        page = jsons['page_now']
        total = int(jsons['total'])
        if seq < total:
            next_page = base + '&page='+str(int(page)+1)
            yield scrapy.Request(next_page, callback=self.parse)

    def extract_url_info(self,response,deliver_dict):
        url_info = json.loads(response.body)[0]
        elem['app_name'] = url_info['app_name']
        elem['url'] = url_info['url'] 
        elem['market_id'] = url_info['market_id']
        elem['state'] = url_info['state'] 
        elem['md5'] = deliver_dict['md5']
        elem['add_time'] = deliver_dict['add_time']
        elem['cn_vname'] = deliver_dict['cn_vname']
        elem['mal_type'] = deliver_dict['mal_type']
        elem['first_time'] = deliver_dict['first_time']
        elem['market_name'] = deliver_dict['market_name']
        yield elem 