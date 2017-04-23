# -*- coding:utf-8 -*-
import scrapy
import json 
from scrapy.loader import ItemLoader
from virusUpdate.items import VirusupdateItem
seq = 0
base = 'https://appstore.anva.org.cn/Login/getBlackList?starttime=&endtime=&type=all&md5=&limit=20'
url_base = 'https://appstore.anva.org.cn/Login/getUrlList?md5='

class VirusUpdateSpider(scrapy.Spider):
    name = 'virus'
    start_urls = ['https://appstore.anva.org.cn/Login/getBlackList?starttime=&endtime=&type=all&md5=&limit=20']

    def parse(self, response):
        jsons = json.loads(response.body)
        run_state = self.get_setting('first_run')
        local_total = self.get_setting('total')
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
            if self.check_md5(md5) == False:
                self.add_md5(md5)
                yield scrapy.Request(url, callback=callback_elem)
        page = jsons['page_now']
        total = int(jsons['total'])
        if run_state == 1: 
            if seq < total:
                next_page = base + '&page='+str(int(page)+1)
                yield scrapy.Request(next_page, callback=self.parse)
        else:
            dev = total - local_total
            v = dev/20
            for index in (1,v + 2):
                next_page = base + '&page='+str(index)
                yield scrapy.Request(next_page, callback=self.parse)

    def extract_url_info(self,response,deliver_dict):
        load = ItemLoader(item=VirusupdateItem())
        url_info = json.loads(response.body)[0]
        load.add_value('app_name',url_info['app_name'])
        load.add_value('url',url_info['url'])
        load.add_value('market_id',url_info['market_id'])
        load.add_value('state',url_info['state'])
        load.add_value('md5',deliver_dict['md5'])
        load.add_value('add_time',deliver_dict['add_time'])
        load.add_value('cn_vname',deliver_dict['cn_vname'])
        load.add_value('mal_type',deliver_dict['mal_type'])
        load.add_value('first_time',deliver_dict['first_time'])
        load.add_value('market_name',deliver_dict['market_name'])
        yield load.load_item()

    def check_md5(self,md5):
        with open('md5_his.txt','r') as f:
            if md5 in f.read():
                return True
            else:
                return False

    def add_md5(self,md5):
        with open('md5_his.txt','a+') as f:
            f.write(md5 + '\n')

    def get_setting(self,arg):
        with open('scrapy.cfg','r') as f:
            for line in f:
                v = line.strip()
                tar = '%s='%(arg)
                if tar in line:
                    return int(line.split('=')[1])
