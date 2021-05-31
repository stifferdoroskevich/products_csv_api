from connect import Connect
import csv
import os


#get connection
client = Connect.get_connection()

def drop_db():
    client.drop_database('price_analytics')

curr_dir = os.getcwd()
#CSV to JSON Conversion
def insert_csv_data(collection, filename):
    with open(curr_dir + '/samples/' + filename , 'r') as csvfile:
        reader = csv.DictReader( csvfile )
        header = reader.fieldnames

        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]

            collection.insert(row)


#create a dabase + collection
def create_db():
    db = client['price_analytics']
    
    collection = db['stores']
    insert_csv_data(collection, 'store_v1(small).csv')

    collection = db['products']
    insert_csv_data(collection, 'products_v1(small).csv')