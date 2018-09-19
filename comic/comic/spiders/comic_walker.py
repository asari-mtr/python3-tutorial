# -*- coding: utf-8 -*-
import scrapy


class ComicWalkerSpider(scrapy.Spider):
    name = 'comic-walker'
    allowed_domains = ['comic-walker.com', 'cdn.comic-walker.com', 'lohas.nicoseiga.jp']
    start_urls = ['https://comic-walker.com/contents/list/']

    def parse(self, response):
        for data in response.css("#mainContent > div > dl > dd > ul > li > a"):
            yield {
                    "title": data.css("h2 > span::text").extract_first(),
                    "link": data.css("a::attr(href)").extract_first(),
                    "image_urls": [data.css("div > img::attr(src)").extract_first()]
            }
