from pymongo import MongoClient


cluster = MongoClient("mongodb://kunal:kunal22061994@e-commerce-app-shard-00-00.ysjtb.mongodb.net:27017,e-commerce-app-shard-00-01.ysjtb.mongodb.net:27017,e-commerce-app-shard-00-02.ysjtb.mongodb.net:27017/PymongoFlaskAppOne?ssl=true&replicaSet=atlas-r3qvd9-shard-0&authSource=admin&retryWrites=true&w=majority")

db = cluster["nursery"]
collection = db["seed"]
