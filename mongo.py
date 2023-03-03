from pymongo import MongoClient
import numpy as np

cluster = MongoClient("localhost:27017")
db = cluster['black_coffer']
collection = db['data']
result =  collection.find()

def charachter_count(arr, i):
    x = np.char.count(arr, i)
    temp = 0
    for i in x:
        temp = temp + i
    return temp

def show_sector():
    sector = []
    for i in result:
        sector.append(str(i["sector"]))
    # print(sector)
    temp = sector
    sector = np.array(sector)
    sector = np.unique(sector)
    # print(sector)
    no_sector = []
    s_sector = []
    for i in range(1, len(sector)-1):
        # print(i, charachter_count(temp, i))
        s_sector.append(sector[i])
        no_sector.append(charachter_count(temp, sector[i]))
    # print(s_sector)
    return s_sector, no_sector

def var_graph(var, fil):
    result =  collection.find()
    sector = []
    for i in result:
        sector.append(str(i[var]))
    
    temp = sector
    sector = np.array(sector)
    sector = np.unique(sector)
    # print(sector)
    # print(len(sector))
    no_sector = []
    s_sector = []
    for i in range(1, len(sector)-1):
        # print(i, charachter_count(temp, i))
        s_sector.append(sector[i])
        no_sector.append(charachter_count(temp, sector[i]))
    # print(s_sector)
    return s_sector, no_sector

def sumofAll(var):
    x,y = [],[]
    result =  collection.find().distinct(var)
    for i in result:
        result =  collection.count_documents({var: i}) 
        x.append(i)
        y.append(result)
    return x, y