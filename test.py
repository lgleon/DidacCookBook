import os
import pymongo
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

#uri = "mongodb://127.0.0.1:27017"
#client = pymongo.MongoClient(uri)
#database = client["didaccookbook"]
#collection = database["recipe"]
#recipes = collection.find({})

app.config["MONGO_DBNAME"] = 'DiDacsCookBook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Admin:plomez13@myfirstcluster-mfuzc.mongodb.net/DiDacsCookBook?retryWrites=true&w=majority')

mongo = PyMongo(app)


#################################################


import os
from pymongo import MongoClient

#to create a mongo client, which connet with the default host and port
client = MongoClient()

#we can specief the host and port
client = MongoClient('localhost, 27017')