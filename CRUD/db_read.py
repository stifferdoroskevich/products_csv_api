from pymongo import collection
from connect import Connect
import json
from bson.json_util import dumps


client = Connect.get_connection()


'''print('Printing first 10 documents...')
for doc in documents[:10]:
    country = doc['address']['country']
    name = doc['name']
    print(f'Country: {country}, Name: {name}')'''

#10006546 - 10009999
'''def print_by_id(id):
    document = col.find_one({'_id':str(id)})
    doc_basic_info = document.get('name'), document.get('room_type'), document.get('price')
    print(doc_basic_info)
'''

def all_stores():
    collection = client['price_analytics']['stores']
    col_results = json.loads(dumps(collection.find().limit(0).sort("time", -1)))
    result = json.dumps(col_results, indent=2)
    return result


def databases():
    names = client.list_database_names()
    db_names = []

    # iterate over the list of database names
    for db in names:
        db_names.append(db)

    
    return ('databases names: ', db_names)
