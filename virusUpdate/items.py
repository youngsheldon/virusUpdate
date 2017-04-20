# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VirusupdateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    md5 = scrapy.Field()
    url = scrapy.Field()
    add_time = scrapy.Field()
    cn_vname = scrapy.Field()
    mal_type = scrapy.Field()
    first_time = scrapy.Field()
    market_name = scrapy.Field()
    market_id = scrapy.Field()
    app_name = scrapy.Field()
    state = scrapy.Field()
