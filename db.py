from pymongo import MongoClient
import os

settings = {
    'host': os.environ('host'),
    'username': os.environ('username'),
    'password': os.environ('password'),
    'database': os.environ('database'),
    'options': os.environ('options')
}
Mongo_URI = os.environ.get("mongodb://{username}:{password}@{host}/{database}?{options}".format(**settings))


cluster = MongoClient(Mongo_URI)

db = cluster["nursery"]
collection = db["seed"]
