from pymongo import MongoClient
import os

settings = {
    'host': os.environ.get('host'),
    'username': os.environ.get('username'),
    'password': os.environ.get('password'),
    'database': os.environ.get('database'),
    'options': os.environ.get('options')
}
Mongo_URI = os.environ.get("mongodb://{username}:{password}@{host}/{database}?{options}".format(**settings))


cluster = MongoClient(Mongo_URI)

db = cluster["nursery"]
collection = db["seed"]
