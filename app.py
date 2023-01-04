
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
import json
from bson import json_util

app = Flask(__name__)
CORS(app)

## Setting database
import pymongo

# Production Environment
#database = pymongo.MongoClient();

# Development Environment
#database = pymongo.MongoClient("mongodb://localhost:27017/")

# Mongo Atlas Environment. (online db)
#database = pymongo.MongoClient('mongodb+srv://wainaina:1234@cluster0.dcztjre.mongodb.net/flask-mongo-db?serverSelectionTryOnce=false&serverSelectionTimeoutMS=150000&w=majority')

#users = database["users"]["customers"]

#Get all users from 
'''
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message":"ok"})
'''


import db
from db import users

#test to insert data to the data base
@app.route("/test")
def test():
    db.db.collection.insert_one({"name": "John"})
    return "Connected to the data base!"

#Create new user
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    obj = {
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "age": data["age"],
        "role": data["role"],    
        "games": data["games"],
        "contacts": data["contacts"]
    }

    print(obj)

    res = users.insert_one(obj)

    return jsonify({
        "message": 'User added on ${}'.format(res),
        "user": str(obj)
    })


#Get all users from DB
@app.route('/api/users', methods=['GET'])
def get_users():
    response = []
    for i in users.find():
        response.append(i)
        
    #return json.dumps(response, default=json_util.default)
    return jsonify(str(response))

#GET unique user
@app.route('/api/user/<first_name>', methods=["GET"])
def get_user(first_name):
    
    response = users.find_one({"first_name":first_name})

    #return json.dumps(response, default=json_util.default)
    return jsonify(str(response))