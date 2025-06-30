# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import logging

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.exceptions import DropItem
from pymongo import logger
from MongoDB import MongoDB


class FirstscrapyPipeline:
    def process_item(self, item, spider):
        return item

class PricePipeline():
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price'):
            adapter['price'] = float(adapter['price'])
            return item
        else:
            raise DropItem(f"Price is missing on item {item}")

class RemoveDuplicatesPipeline:

    def __init__(self):
        self.items_seen = set()


    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['name'] in self.items_seen:
            raise DropItem(f"Duplicate item {adapter['name']} found")
        else:
            self.items_seen.add(adapter['name'])
            return item

class FillDbPipeline:

    def __init__(self):
        self.mongo = MongoDB()
        self.mongo.getDB()['Snus'].drop()

    def process_item(self, item, spider):
        self.mongo.insertDB('Snuzone', 'Snus', item)
        return item