from pymongo import MongoClient


class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient(host='mongo_composed', username='eiprice', password='contratado')
