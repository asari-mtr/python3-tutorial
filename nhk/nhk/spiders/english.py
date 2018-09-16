# -*- coding: utf-8 -*-
import scrapy


class EnglishSpider(scrapy.Spider):
    name = 'english'
    allowed_domains = ['https://www2.nhk.or.jp/gogaku/english/']
    start_urls = ['https://www2.nhk.or.jp/gogaku/english/']

    def parse(self, response):
        for program in response.css("div.programListBox"):
            link = program.css('a[href*=stream]').xpath("@href").extract_first()
            if link == None:
                continue

            yield {
                    'title': ''.join(program.css('.title>a *::text').extract()),
                    'link': link
            }

