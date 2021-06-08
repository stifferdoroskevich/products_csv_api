import os
from pymongo import MongoClient


class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient(host=os.environ['MONGO_HOST'], username=os.environ['MONGO_USER'], password=os.environ['MONGO_PASSWORD'])
