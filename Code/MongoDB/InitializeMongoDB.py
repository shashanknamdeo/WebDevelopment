
# mongodb://localhost:27017

from pymongo import MongoClient 
client = MongoClient() 

client = MongoClient('mongodb://localhost:27017/') 

mydatabase = client['DummyDB']

mycollection = mydatabase['TestConnection'] 


# get data of mycollection

cursor = mycollection.find() 
for record in cursor: 
    print(record) 


# insert data in mycollection

mycollection.insert_one({"name":"Shree","value":"17335"})
