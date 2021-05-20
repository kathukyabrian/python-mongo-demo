from flask import  request
from models.user import User
from repository.user_repository import save_one
from config import app, db

@app.route("/add-one", methods=["POST"])
def add_one():
    if request.method == "POST":

        # get the request data as json
        request_data = request.json

        # create a User with the provided data
        user = User(request_data["name"],request_data["age"])

        # insert into mongo db the dictionary representation
        save_one(user.__dict__)

        return "User created"


if(__name__=="__main__"):
    app.run(debug=True)