from rest_api import app, core
from flask import redirect, url_for


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
    return core.all_stores()


@app.route('/api/v1/products/<ean>', methods=['GET'])
def get_products_by_ean(ean):
    return core.get_products_by_ean(ean)


@app.route('/api/v1/products', strict_slashes=False, methods=['GET'])
def get_products():
    return core.get_products()


@app.route('/api/v1/analytics', strict_slashes=False, methods=['GET'])
def get_header():
    return core.get_header()


