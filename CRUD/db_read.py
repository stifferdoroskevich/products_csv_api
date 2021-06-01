from flask import Response
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
    if ean:
        products = collection.find({'ean': ean})
    else:
        products = collection.find({})
    result = dumps(products)
    return Response(result, mimetype="application/json")


def get_products():
    return get_products_by_ean({})

#"total_products":50,
#"total_promotions":30,
#"total_categories":20,
def get_header():
    collection = client['price_analytics']['products']
    total_products = collection.count_documents({})
    #products list(cursor) in promotion 
    total_promotions = collection.find({'$expr':{'$gt':["$real_price", "$price"]}})
    total_categories = len(collection.distinct('category'))
    products = list(collection.find({},{'_id':0}))
    c = 0
    for n in total_promotions:
        c += 1
    header = {"total_products": total_products, "total_promotions":c, "total_categories": total_categories, "products":products}
    return header

