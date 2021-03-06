from pymongo import MongoClient
import os

MONGODB_CONNECTION = os.getenv('MONGODB_CONNECTION')

class DatabaseAtlas(object):

    client = MongoClient(MONGODB_CONNECTION, serverSelectionTimeoutMS = 2000)
    db = client["test"]

    @staticmethod
    def insertOne(col, data):
        return DatabaseAtlas.db[col].insert_one(data)

    @staticmethod
    def insertMany(col, data):
        return DatabaseAtlas.db[col].insert_many(data)

    @staticmethod
    def find(col, query):
        return DatabaseAtlas.db[col].find_one(query, {"_id":0})

    @staticmethod
    def findAll(col, query):
        findlist = [i for i in DatabaseAtlas.db[col].find(query, {"_id":0})]
        return findlist

    @staticmethod
    def dropCol(col):
        c = DatabaseAtlas.db[col].drop()
        return c



