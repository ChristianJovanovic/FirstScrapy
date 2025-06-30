from pymongo import MongoClient
import logging
class MongoDB:

    def __init__(self):
        self.client = MongoClient('localhost',
                          username='root',
                          password='example',
                          authSource='admin',
                          port=27017)
        logging.disable(logging.DEBUG)

    def insertDB(self, db: str, collection: str, item):
        db  = self.client.get_database(db)
        collection = db[collection]
        collection.drop()
        collection.insert_one(dict(item))
