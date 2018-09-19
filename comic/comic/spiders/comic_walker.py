# -*- coding: utf-8 -*-
import scrapy


class ComicWalkerSpider(scrapy.Spider):
    name = 'comic-walker'
    allowed_domains = ['comic-walker.com']
    start_urls = ['http://comic-walker.com/']

    def parse(self, response):
        pass
