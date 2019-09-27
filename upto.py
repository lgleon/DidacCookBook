import pymongo



## This is the way to connect with the local mongodb
uri="mongodb://127.0.0.1:27017"
client=pymongo.MongoClient(uri)
database=client["didaccookbook"]
collection=database["recipe"]

recipes = collection.find({})

#This is for testing the connection
for recipe in recipes:
    print(recipe)




# This is the way to connect with the external (Atlas) mondodb
app.config["MONGO_DBNAME"] = 'DiDacsCookBook'
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Admin:plomez13@myfirstcluster-mfuzc.mongodb.net/DiDacsCookBook?retryWrites=true&w=majority')
#app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

#Never forget to go to mongoDB copy the url and put the password to connect with our python-flask app
#After we should remember to put a variable and not show our password (monDB password)