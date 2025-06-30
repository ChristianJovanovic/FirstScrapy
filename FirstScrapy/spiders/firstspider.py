import urllib
from typing import AsyncIterator, Any
from urllib.parse import urlencode, urljoin

import scrapy
from scrapingbee import ScrapingBeeClient
from bs4 import BeautifulSoup
from FirstScrapy.items import FirstscrapyItem, ProductDetailsItem
from FirstScrapy.itemloaders import FirstScrapyItemLoader, ProductDetailsLoader

### returns a proxy url
def getProxy(url: str):
    params = {'api_key': 'e051a594-2b3e-41d0-97f2-5dbd58880c0e', 'url': url}
    return 'https://proxy.scrapeops.io/v1/?' + urlencode(params)

class FirstspiderSpider(scrapy.Spider):
    name = "firstspider"
    allowed_domains = ["snuzone.com", "proxy.scrapeops.io"]
    #start_urls = [url]

    async def start(self):
        url = 'https://snuzone.com/collections/snus-und-nicotine-pouches/'
        yield scrapy.Request(getProxy(url), callback=self.parse)

    def parse(self, response):
        products = response.css('div.custom-grid-product')

        for product in products:
            item = FirstScrapyItemLoader(item=FirstscrapyItem(), selector=product)
            if product.css('span.grid-regular-price'):
                item.add_css("name", 'a.grid-product__title')
                item.add_css("price", 'span.grid-regular-price')
                item.add_css("strong", 'div.grid-product__vendor')
                item.add_css("url", 'a.grid-product__link::attr(href)')
                yield item.load_item()
            else:
                item.add_css("name", 'a.grid-product__title')
                item.add_css("price", 'div.product-price')
                item.add_css("strong", 'div.grid-product__vendor')
                item.add_css("url", 'a.grid-product__link::attr(href)')
                yield item.load_item()

        next_page = response.css('span.next a::attr(href)').get()
        
        if next_page is not None:
            absolute_url = urljoin("https://snuzone.com", next_page)
            print(absolute_url)
            yield response.follow(getProxy(absolute_url), callback=self.parse)
        else:
            print('No next page')