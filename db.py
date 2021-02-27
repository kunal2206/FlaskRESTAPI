from pymongo import MongoClient
from info import Mongo_URI


cluster = MongoClient(Mongo_URI)

db = cluster["nursery"]
collection = db["seed"]
