# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class CoinSpiderSpider(scrapy.Spider):
    name = 'coin_spider'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ['http://www.livecoin.net/en/']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriverr")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.get("https://www.livecoin.net/en")

        rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        rur_tab[4].click()

        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        pass
