from pymongo import MongoClient
import numpy as np

cluster = MongoClient("localhost:27017")
db = cluster['black_coffer']
collection = db['data']
result =  collection.find()


def sumofAll(var):
    x,y = [],[]
    result =  collection.find().distinct(var)
    for i in result:
        result =  collection.count_documents({var: i}) 
        x.append(i)
        y.append(result)
    return x, y

def sumofFilter(search, filter):
    x =  collection.find().distinct(filter)
    y = []
    for i in x:
        result =  collection.find({filter: i})
        sum_all = 0
        for j in result:
            try:
                sum_all+= int(j[search])
            except Exception:
                pass
        y.append(sum_all)
    return x, y