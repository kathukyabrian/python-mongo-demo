from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/mongotut")

db = mongodb_client.db