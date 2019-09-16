import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'DiDacsCookBook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipe.html",
                           recipe=mongo.db.recipe.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           categories=mongo.db.recipe.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe =  mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipe'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe,
                           categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
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






if__name__== '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)