from flask import Flask, redirect
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
coll = client.bitly.database

app = Flask(__name__)

for i in coll.find():
    _id = i["_id"]
    query = i["query"]

    @app.route(f"/{_id}")
    def red():
        return redirect(query)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
