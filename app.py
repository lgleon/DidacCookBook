import os
import pymongo
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client["didaccookbook"]
collection = database["recipe"]

recipes = collection.find({})

'''
To test if the connection with our local mongpdb is working, we can use this for loop

for recipe in recipes:
    print(recipe)
    
'''
@app.route("/")
def hello():
    return "Hello world"

#@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipe.html",
                           recipes=collection.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           recipie=collection.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = collection
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipe'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = collection.find_one({"_id": ObjectId(recipe_id)})
    all_recipies = collection.find()
    return render_template('edit_recipe.html', recipe=the_recipe,
                           recipie=all_recipies)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = collection
    recipe.update({'_id': ObjectId(recipe_id)},
                  {
                      'recipe_name': request.form.get('recipe_name'),
                      'number_of_service': request.form.get('number_of_service'),
                      'time': request.form.get('time'),
                      'level': request.form.get('level'),
                      'type': request.form.get('type'),
                      'origin': request.form.get('origin'),
                      'ingredients': request.form.get('ingredients'),
                      'amounts': request.form.get('amounts'),
                      'preparation': request.form.get('preparation')
                  })
    return redirect(url_for('get_recipe'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
