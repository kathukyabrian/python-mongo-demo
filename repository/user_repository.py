from config import db, mongodb_client

doc = db["mongotut"]

def save_one(user):
    db.mongotut.insert_one(user)

def find_one():
    return doc.find_one()