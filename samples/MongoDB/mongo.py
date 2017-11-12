import pymongo
import sys


if __name__ == "__main__":
    connect = pymongo.MongoClient('localhost',27017)

    db = connect.hoge
    co = db.my_collection

    co.insert_one({"test":"fugafuga",
                   "num":1})
    print ("db name: %s" % str(db.name))
    connect.close()
