from flask import Flask, jsonify
from CRUD import db_read

app = Flask(__name__)


@app.route("/", methods=['GET'])
def root():
    return 'API ROOT'


@app.route('/stores/', methods=['GET'])
def stores():
    return db_read.all_stores()


@app.route('/products/<ean>', methods=['GET'])
def get_products_by_ean(ean):
    return db_read.get_products_by_ean(ean)


@app.route('/products', strict_slashes=False, methods=['GET'])
def get_products():
    return db_read.get_products()


@app.route('/analytics', strict_slashes=False, methods=['GET'])
def get_header():
    return db_read.get_header()



if __name__ == '__main__':
    app.run(debug=True)