from pymongo import MongoClient


class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient(username='eiprice', password='contratado')
