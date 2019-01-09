uri="mongodb://admin:admin1@ds053300.mlab.com:53300/c4e25"

#1.connect to mlab server
from pymongo import MongoClient
client=MongoClient(uri)

#2.get a database
db= client.get_database()

# #3. get  a CONNECTION
# collection = db.test_collection

# #4.CREATE A DOCUMENT
# import datetime
# post={
#     "author": "Mike",
#     "text": "My first blog post!",
#     "tags": ["mongodb", "python", "pymongo"],
#     "date": datetime.datetime.utcnow()
# }

# #5.inseert document

# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# post_id





#3. get  a CONNECTION
post_collection = db["post"]

#4.CREATE A DOCUMENT
new_post={
    "title":"sunny day", #field title
    "content":"hello",
}
#5.inseert document
post_collection.insert_one(new_post)

# for post in post_collection.find():
#     print(post_collection)
# # close connection
# client.close()


# # lazyloading
# post_list=post_collection.find()
# # first_post=post_list[0]
# # print(first_post)
# for p in post_list:
#     print(p)
