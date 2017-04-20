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
    start_urls = [
        'https://appstore.anva.org.cn/Login/getBlackList?starttime=&endtime=&type=all&md5=&limit=20&page=450',
    ]

    def parse(self, response):
        jsons = json.loads(response.body)
        for item in jsons['list']:
            md5 = item['md5']
            seq = int(item['seq']) 
            url = url_base + md5 
            # yield {
            # 'md5':item['md5'],'add_time':item['add_time'],
            # 'cn_vname':item['cn_vname'],'type':item['type'].encode('utf-8'),
            # 'firsttime':item['firsttime'],'market_name':item['market_name'].encode('utf-8')
            # }
            elem['md5'] = item['md5']
            elem['add_time'] = item['add_time']
            elem['cn_vname'] = item['cn_vname']
            elem['mal_type'] = item['type'].encode('utf-8')
            elem['first_time'] = item['firsttime']
            elem['market_name'] = item['market_name'].encode('utf-8')
            yield scrapy.Request(url, callback=self.extract_url_info)
        page = jsons['page_now']
        total = int(jsons['total'])
        if seq < total:
            next_page = base + '&page='+str(int(page)+1)
            yield scrapy.Request(next_page, callback=self.parse)

    def extract_url_info(self,response):
        url_info = json.loads(response.body)[0]
        # yield {
        # 'app_name':url_info['app_name'],'url':url_info['url'],
        # 'market_id':url_info['market_id'],'state':url_info['state'].encode('utf-8'),
        # 'market_name':url_info['market_name'].encode('utf-8'),'add_time':url_info['add_time']
        # }
        elem['app_name'] = url_info['app_name']
        elem['url'] = url_info['url'] 
        elem['market_id'] = url_info['market_id']
        elem['state'] = url_info['state'] 
        yield elem 
