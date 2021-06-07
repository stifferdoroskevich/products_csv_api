from flask import Flask
from connect import Connect

app = Flask(__name__)
app.config.from_object('rest_api.config')

client = Connect.get_connection()

import rest_api.routes  