# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieItem(scrapy.Item):
    name = scrapy.Field()
    rate = scrapy.Field()
    comment = scrapy.Field()
    img = scrapy.Field()
    url = scrapy.Field()

class BookItem(scrapy.Item):
    name = scrapy.Field()
    rate = scrapy.Field()
    comment = scrapy.Field()
    img = scrapy.Field()