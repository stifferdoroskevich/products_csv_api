from rest_api import client
import csv
import os


#get connection
#client = Connect.get_connection()

def drop_db():
    client.drop_database('price_analytics')

curr_dir = os.getcwd()
#CSV to JSON Conversion
def insert_csv_data(collection, filename):
    with open(curr_dir + '/samples/' + filename , 'r') as csvfile:
        reader = csv.DictReader( csvfile )
        header = reader.fieldnames

        for each in reader:
            row = {}
            discount = 0.0
            
            # if is a product, creat a discount field
            if 'product' in filename:
                real_price = float(each['real_price'].replace(',', '.'))
                price = float(each['price'].replace(',', '.'))

                discount =  real_price - price
                row['discount'] = round(discount, 2)

            for field in header:
                row[field]=each[field]

            collection.insert_one(row)


#create a dabase + collection
def init_db():
    db = client['price_analytics']
    
    collection = db['stores']
    insert_csv_data(collection, 'store_v1.csv')

    collection = db['products']
    insert_csv_data(collection, 'products_v1.csv')
