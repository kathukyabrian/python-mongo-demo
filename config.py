from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

mongodb_client = MongoClient("mongodb://localhost:27017/")

db = mongodb_client["mongotut"]