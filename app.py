from flask import Flask, redirect, url_for
from CRUD import db_read

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return redirect(url_for('api'))


@app.route("/api/v1", methods=['GET'])
def api():
    api_urls = {
    'Main Api Manipulation':'/analytics',
    'List of Stores':'/stores',
    'List of products':'/products',
    'List of products + limit + offset':'/products?limit=&offset=',
    'Product by EAN':'/products/<ean>'
    }
    return api_urls



@app.route('/api/v1/stores/', methods=['GET'])
def stores():
    return db_read.all_stores()


@app.route('/api/v1/products/<ean>', methods=['GET'])
def get_products_by_ean(ean):
    return db_read.get_products_by_ean(ean)


@app.route('/api/v1/products', strict_slashes=False, methods=['GET'])
def get_products():
    return db_read.get_products()


@app.route('/api/v1/analytics', strict_slashes=False, methods=['GET'])
def get_header():
    return db_read.get_header()


if __name__ == '__main__':
    app.run(debug=True)