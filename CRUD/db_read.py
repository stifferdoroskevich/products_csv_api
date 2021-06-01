from flask import Response
from pymongo import collection
from connect import Connect
import json
from bson.json_util import dumps


client = Connect.get_connection()


def all_stores():
    collection = client['price_analytics']['stores']
    col_results = json.loads(dumps(collection.find().limit(0).sort("time", -1)))
    result = json.dumps(col_results, indent=2)
    return result


def get_products_by_ean(ean):
    collection = client['price_analytics']['products']
    if ean:
        products = collection.find({'ean': ean})
    else:
        products = collection.find({})
    response = dumps(products)
    return Response(response, mimetype="application/json")


def get_products():
    return get_products_by_ean({})


def databases():
    names = client.list_database_names()
    db_names = []

    # iterate over the list of database names
    for db in names:
        db_names.append(db)

    
    return ('databases names: ', db_names)
