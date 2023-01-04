from flask import Flask
from flask_pymongo import pymongo
from app import app
#CONNECTION_STRING = "mongodb+srv://test:test@flask-mongodb-atlas-1g8po.mongodb.net/test?retryWrites=true&w=majority"
CONNECTION_STRING = "mongodb+srv://wainaina:1234@cluster0.dcztjre.mongodb.net/flask-mongo-db?serverSelectionTryOnce=false&serverSelectionTimeoutMS=150000&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
users = pymongo.collection.Collection(db, 'user_collection')