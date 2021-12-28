from pymongo import MongoClient

class Database(object):

    MONGODBPORT = "mongodb://localhost:27017/"
    client = MongoClient(MONGODBPORT, serverSelectionTimeoutMS = 2000)
    db = client["test"]

    @staticmethod
    def insertOne(col, data):
        return Database.db[col].insert_one(data)

    @staticmethod
    def insertMany(col, data):
        return Database.db[col].insert_many(data)

    @staticmethod
    def find(col, query):
        return Database.db[col].find_one(query, {"_id":0})

    @staticmethod
    def findAll(col, query):
        findlist = [i for i in Database.db[col].find(query, {"_id":0})]
        return findlist

    @staticmethod
    def dropCol(col):
        c = Database.db[col].drop()
        return c