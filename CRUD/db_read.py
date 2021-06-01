from flask import Response, request
from pymongo import ASCENDING
from connect import Connect
from bson.json_util import dumps, loads


client = Connect.get_connection()


def all_stores():
    collection = client['price_analytics']['stores']
    col_results = collection.find()
    result = dumps(col_results)
    return Response(result, mimetype="application/json")


def get_products_by_ean(ean):
    collection = client['price_analytics']['products']
    products = collection.find({'ean': ean})
    result = dumps(products)

    return Response(result, mimetype="application/json")


def get_products():
    collection = client['price_analytics']['products']
    
    limit = int(request.args.get('limit', 0))
    offset = int(request.args.get('offset', 0))

    #offset preparation 
    first_product = collection.find().sort('_id', ASCENDING)[offset]
    starting_id = first_product['_id']

    products = collection.find({'_id' : {'$gte' : starting_id}}).sort('_id', ASCENDING).limit(limit)
    result = dumps(products)
    return Response(result, mimetype="application/json")


def get_header():
    collection = client['price_analytics']['products']
    
    total_products = collection.count_documents({})
    total_promotions = collection.count_documents({'$expr':{'$gt':["$discount", 0]}})
    total_categories = len(collection.distinct('category'))
    products = list(collection.find({},{'_id':0}))

    header = {"total_products": total_products, "total_promotions":total_promotions, "total_categories": total_categories, "products":products}
    return header

