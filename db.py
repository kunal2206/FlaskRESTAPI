from pymongo import MongoClient
import os


Mongo_URI = os.environ.get("URI")


cluster = MongoClient(Mongo_URI)

db = cluster["nursery"]
collection = db["seed"]
