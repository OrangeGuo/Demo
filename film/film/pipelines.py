# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FilmPipeline(object):
    def process_item(self, item, spider):
        with open("films.txt",'a') as fp:
            fp.write(item['name'] + '\n')
            fp.close()
