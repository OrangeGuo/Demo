# -*- coding: utf-8 -*-
import scrapy
from demo.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    next_url = 'https://movie.douban.com/top250?start='
    offset = 0

    def parse(self, response):
        # with open("top250.html","w",encoding='utf-8') as f:
         #   f.write(response.text)
        items = []
        head = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for item in head:
            movie = MovieItem()
            movie['name'] = item.xpath(
                'div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            movie['rate'] = item.xpath(
                'div/div[2]/div[2]/div/span[2]/text()').extract()[0]
            movie['comment'] = item.xpath(
                'div/div[2]/div[2]/div/span[4]/text()').extract()[0]
            movie['img'] = item.xpath('div/div[1]/a/img/@src').extract()[0]
            items.append(movie)
            yield movie
        self.offset += 25
        if(self.offset == 250):
            return

        yield scrapy.Request(self.next_url+str(self.offset)+'&filter=', callback=self.parse)
        # pass
