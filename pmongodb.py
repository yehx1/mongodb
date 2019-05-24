# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:02:11 2019

@author: yehx
"""

from pymongo import MongoClient
from gridfs import *
from bson import binary

#插入记录
def insert_record(collection):
    #插入一条记录
    collection.insert({"name":"zhangsan","age":18})
    #插入多条记录
    users=[{"name":"zhangsan","age":18},{"name":"lisi","age":20}]  
    collection.insert(users)
    
#查询记录
def find_record(collection):
    #查询多条记录
    for i in collection.find({"name":"zhangsan"}):
        print(i)
    #查询单条记录
    find_result = (collection.find_one({"name":"lisi"}))
    print(find_result["_id"])
    print(find_result["age"])

#修改记录
def update_record(collection):
    collection.update_one({"name":"lisi"},{'$set':{"age":22}})
    collection.update_many({"name":"zhangsan"},{'$set':{"age":25}})
    
#删除记录
def delete_recoord(collection):
    #删除name=zhangsan的全部记录
    collection.remove({'name': 'zhangsan'})
    #删除name=lisi的某个id的记录
    id = collection.find_one({"name":"lisi"})["_id"]
    collection.remove(id)
    #删除集合里的所有记录
    #db.CollectionName.remove()

############################################################################## 
##############################################################################
# 大文件上传
def insert_large_file(collection):
    image_path = "./test.jpg" 
    dic = {
           "Name" : "Wangwu",
           "Age" : 30,
           }
    with open(image_path, 'rb') as f2:
        data = f2.read() 
    fs = GridFS(db, collection=collection) #连接collection
    fs.put(data, **dic)
    
#大文件查询
def find_large_file(collection):
    fs = GridFS(db, collection=collection) #连接collection
    grid_out = fs.find({"Age":30})[0]
    image = grid_out.read()
    name  = grid_out.Name
    age   = grid_out.Age

       
if __name__ == "__main__":
    conn = MongoClient('localhost', 27017)     #创建连接
    db = conn.DatabaseName                     #选择数据库，没有则自动创建
    collection = db.CollectionName
    #print(collection)
    
    #1. 插入记录
    #insert_record(collection)
    
    #2. 查询记录
    #find_record(collection)
    
    #3. 修改记录
    #update_record(collection)









