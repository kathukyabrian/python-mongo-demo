from config import db

def save_one(user):
    db.mongotut.insert_one(user)