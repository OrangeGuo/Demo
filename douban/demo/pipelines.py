# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class DemoPipeline(object):
    def __init__(self, *args, **kwargs):
        self.file = open("movie.json", "wb+")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)+",\n"
        self.file.write(content.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.file.close()

#TODO: save img with movie name
class DoubanImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img'])
