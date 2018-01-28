# -*- coding: utf-8 -*-
import scrapy
from film.items import FilmItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        movies = response.xpath('//table[@class="tbspan"]')
        #print(len(movies))
        for each_movie in movies:
            #print(88)
            item = FilmItem()
            item['name'] = each_movie.xpath('.//a[@class="ulink"]/text()').extract_first()
            #item['name']="4"
            #print(item['name'])
            yield item

