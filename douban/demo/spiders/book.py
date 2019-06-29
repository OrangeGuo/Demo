# -*- coding: utf-8 -*-
import scrapy
from demo.items import BookItem
class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/tag/Top250','https://book.douban.com/tag/Top250?start=20&type=T']

    def parse(self, response):
        items = []
        head = response.xpath('//*[@id="subject_list"]/ul/li')
        for item in head:
            book = BookItem()
            book['name'] = item.xpath(
                'normalize-space(div[2]/h2/a/text())').extract_first()
            book['rate'] = item.xpath(
                'div[2]/div[2]/span[2]/text()').extract()[0]
            book['comment'] = item.xpath(
                'normalize-space(div[2]/div[2]/span[3]/text())').extract()[0][1:-1]
            book['img'] = item.xpath('div[1]/a/img/@src').extract()[0]
            items.append(book)
            yield book
        return

