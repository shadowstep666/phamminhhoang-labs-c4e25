uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1.connect to mlab server
from pymongo import MongoClient
client=MongoClient(uri)

#2.get a database
db= client.get_database()
#3. get  a CONNECTION
post_collection = db["post"]


#4.CREATE A DOCUMENT
new_post={
    "title" : "pham hoang" ,
    "author": "nhìn lại cuộc đời" ,
    "text" : "lại một ngày trôi qua bỗng thấy mình già đi thêm một ngày . Nhìn lại quá khứ mà thấy luyến tiếc nhiều điều đã trôi qua",
}
#5.insert document
post_collection.insert_one(new_post)
