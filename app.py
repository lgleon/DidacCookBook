import os
import pymongo
from flask import Flask, render_template, redirect, url_for, request, session, g, flash
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
from functools import wraps

app = Flask(__name__)

#uri = "mongodb://127.0.0.1:27017"
#client = pymongo.MongoClient(uri)
#database = client["didaccookbook"]
#collection = database["recipe"]
#recipes = collection.find({})


##################################################################

#app.config["MONGO_DBNAME"] = 'DiDacsCookBook'
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
# This part is for the connection to atlas MondoDB (remote DB)
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Admin:plomez13@myfirstcluster-mfuzc.mongodb.net/DiDacsCookBook?retryWrites=true&w=majority')

#client = pymongo.MongoClient(os.getenv('MONGO_URI'))
#db = client.didaccookbook

#mongo = PyMongo(app)

#########################################################################
#Connecting to the local MondoDB

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
db = client.didaccookbook
#database = client["el_luis"]
#collection = database["new"]
#recipes = collection.find({})

'''
To test if the connection with our local mongpdb is working, we can use this for loop

for recipe in recipes:
    print(recipe)
    
    si se cambia a local:
    
    cambiar: <collection> por <mongo.db.recipe>
    
'''

# Render the home page
@app.route('/')
def home_site():
    return render_template("home.html")


######## Render recipes


#render recipe
@app.route('/get_recipe')
def get_recipe():
    cursor = db.recipe.find()
    print( "Numero de documentos en la colecttion: ", cursor.count())
    #results = database.new.find({})
    return render_template("recipe.html",
                           recipes = cursor)


# Get all recipes
#Recipe Menu, recipe search big subgroups
#@app.route('/get_recipes')
#def get_recipes():
#    return render_template("recipes.html",
#                           recipes=mongo.db.recipes.find())
@app.route('/recipes')
def recipes():
    recipes = list(db.recipe.find())
    for arg in request.args:
        if 'recipe_search' in arg:
            new_recipe_list = []
            query = request.args['recipe_search']
            for recipe in recipes:
                if recipe['recipe_name'].lower().find(query.lower()) != -1:
                    new_recipe_list.append(recipe)
            return render_template('recipes.html', recipes=new_recipe_list, cuisines=cuisines, user=g.user)

        elif 'sort' in arg:
            if request.args['sort'] == 'asc':
                new_recipe_list = list(db.recipes.find().sort('recipe_name', pymongo.ASCENDING))
                return render_template('recipes.html', recipes=new_recipe_list, cuisines=cuisines, user=g.user)
            elif request.args['sort'] == 'dsc':
                new_recipe_list = list(db.recipes.find().sort('recipe_name', pymongo.DESCENDING))
                return render_template('recipes.html', recipes=new_recipe_list, cuisines=cuisines, user=g.user)

    return render_template('recipes.html', recipes=recipes, )




#Get Recipes by Menu
@app.route('/menu_recipes')
def menu_recipes():
    return render_template("menu_recipes.html",
                           recipes=db.recipe.find())

#Get Recipes by main course
@app.route('/main_course')
def main_course():
    return render_template("main_course.html",
                           recipes=db.recipe.find())

#Get Recipes by Cuisine type
@app.route('/cusine')
def cusine():
        cuisines = list(db.cuisines.find().sort('cuisine', pymongo.ASCENDING))
        recipes = list(db.recipe.find())
        for arg in request.args:
            if 'recipe_search' in arg:
                new_recipe_list = []
                query = request.args['recipe_search']
                for recipe in recipes:
                    if recipe['recipe_name'].lower().find(query.lower()) != -1:
                        new_recipe_list.append(recipe)
                return render_template('cusine.html', cuisines=cuisines)

            elif 'sort' in arg:
                if request.args['sort'] == 'asc':
                    new_recipe_list = list(db.recipes.find().sort('name', pymongo.ASCENDING))
                    return render_template('cusine.html', cuisines=cuisines)
                elif request.args['sort'] == 'dsc':
                    new_recipe_list = list(db.recipes.find().sort('name', pymongo.DESCENDING))
                    return render_template('cusine.html', cuisines=cuisines)

        return render_template('cusine.html', cuisines=cuisines )



########## Log in and Add recipe(only if you are sign in)

# Manage session user
#@app.before_request
#def before_request():
#    g.user = None
#    if 'username' in session:
#        g.user = session['username']
#        return 'You are logged in as ' + session['username']

@app.route('/home')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('home_site.html')

# To log in in case user is already resgister
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = db.users
        login_user = users.find_one({'name': request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('home_site'))

        #return 'Invalid username/password combination'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('login'))

        return 'That username already exists!'

    return render_template('signup.html')




#Add recipe, only if a member or resgister user
@app.route('/addrecipe')
def addrecipe():
    return render_template("addrecipe.html")


# Submit add recipe form
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = db.recipe

    recipe_name = request.form['name']
    recipe_description = request.form['description']
    recipe_serving = request.form['n_service']
    recipe_prep_time = request.form['prep_time']
    recipe_cook_time = request.form['cooking_time']
    recipe_cuisine = request.form['cuisine']
    recipe_level = request.form('level')
    recipe_main_course = request.form('m_course')
    recipe_ingredient = request.form('ingredient')
    recipe_preparation = request.form['preparation']
    recipe_user = request.form['user']

    recipe_form = {
        "name": recipe_name,
        "description": recipe_description,
        "n_service": recipe_serving,
        "cooking-time": recipe_cook_time,
        "prep-time": recipe_prep_time,
        "cuisine": recipe_cuisine,
        "level": recipe_level,
        "m_course": recipe_main_course,
        "ingredients": recipe_ingredient,
        "preparation": recipe_preparation,
        "user": recipe_user,
    }

    recipes.insert_one(recipe_form)
    return redirect(url_for('get_recipe'))







if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

