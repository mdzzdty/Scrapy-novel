# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MinuItem(scrapy.Item):
    novelClass = scrapy.Field()
    novelClassUrl = scrapy.Field()

class NameItem(scrapy.Item):
    novelName = scrapy.Field()
    novelUrl = scrapy.Field()

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
