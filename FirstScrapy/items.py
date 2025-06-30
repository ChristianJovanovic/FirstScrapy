# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    strong = scrapy.Field()
    url = scrapy.Field()
    details = scrapy.Field()

class ProductDetailsItem(scrapy.Item):
    marke = scrapy.Field()
    niko_per_gram = scrapy.Field()
    niko_per_piece = scrapy.Field()
    aroma = scrapy.Field()
    format = scrapy.Field()
    pieces_per_pack = scrapy.Field()
    summary = scrapy.Field()
    review_score = scrapy.Field()