# drive python to connect with a mongodb

from pymongo import MongoClient
import datetime

# instantiate a client
client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

# creating a test database
db = client.test_database
db = client['test-database']
print(db)

# creating a collection
collection = db.test_collection
collection = db['test-collection']
print(collection)


post = {'autor': 'Mike',
'text': 'my first blog post!',
'tags': ['mongodb', 'python', 'pymongo'],
'date': datetime.datetime.utcnow()
}

inserting a document
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.list_collection_names())