from flask import Flask, jsonify
from CRUD import db_read

app = Flask(__name__)


@app.route("/", methods=['GET'])
def root():
    return 'API ROOT'


@app.route("/databases", methods=['GET'])
def database_list():
    result = db_read.databases()
    return str(result)


@app.route("/stores", methods=['GET'])
def stores():
    return db_read.all_stores()


if __name__ == '__main__':
    app.run(debug=True)