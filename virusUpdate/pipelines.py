# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import os 

logger = logging.getLogger('SQL')

class VirusupdatePipeline(object):
    def __init__(self):
        self.sql_count = 0 

    def process_item(self, item, spider):
        self.sql_count += 1 
        # logger.info('insert into virus_black_list(md5,url) values (\'%s\',\'%s\');',item['md5'][0],item['url'][0])
        logger.info('sql_count=%d',self.sql_count)
        sql = self.make_sql(item['url'][0],item['md5'][0])
        self.sql_exec(sql)
        return item

    def make_sql(self,url,md5):
        remark = '由病毒库自动更新程序添加'
        sql = 'call sp_add_virus_list(20,0,0,\'%s\',\'%s\',\'%s\',\'%s\');' % (url,' ',md5,remark)
        return sql 

    def sql_exec(self,sql):
        sql_exe = ''
        if isinstance(sql,list):
            for v in sql:
                sql_exe += v + '\n'
            out = 'sqlplus smmchunan/A1234567@SMMC <<!\n' + sql_exe + 'exit;\n' + '!\n'
        else:
            out = 'sqlplus smmchunan/A1234567@SMMC <<!\n' + sql + '\n' + 'exit;\n' + '!\n'
        os.system(out)

    def get_setting(self,arg):
        with open('scrapy.cfg','r') as f:
            for line in f:
                v = line.strip()
                tar = '%s='%(arg)
                if tar in line:
                    return int(line.split('=')[1])