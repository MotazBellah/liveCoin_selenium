# -*- coding: utf-8 -*-
import scrapy


class CoinSpiderSpider(scrapy.Spider):
    name = 'coin_spider'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ['http://www.livecoin.net/en/']

    def parse(self, response):
        pass
