# -*- coding: utf-8 -*-
import scrapy


class EnglishSpider(scrapy.Spider):
    name = 'english'
    allowed_domains = ['www2.nhk.or.jp']
    start_urls = ['https://www2.nhk.or.jp/gogaku/english/']

    def parse(self, response):
        for data in response.xpath("//musicdata/music"):
            yield {
                'title': data.xpath("@title").extract_first(),
                'hdate': data.xpath("@hdate").extract_first(),
                'kouza': data.xpath("@kouza").extract_first(),
                'code': data.xpath("@code").extract_first(),
                'file': data.xpath("@file").extract_first(),
                'nendo': data.xpath("@nendo").extract_first(),
                'pgcode': data.xpath("@pgcode").extract_first()
            }

        for program in response.css("div.programListBox"):
            link = program.css('a[href*=stream]::attr(href)').extract_first()
            if link is None:
                continue

            lesson = program.css(
                '.title>a::attr(href)').extract_first().rsplit("/", 2)[-2]

            if lesson is None:
                continue

            url = f"https://www2.nhk.or.jp/gogaku/st/xml/english/{lesson}/listdataflv.xml"

            yield scrapy.Request(url, callback=self.parse)
