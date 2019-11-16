import os
from bson.objectid import ObjectId
import bcrypt
import pymongo
from flask import Flask, render_template, redirect, url_for, request, session, g
from config import Config


app = Flask(__name__)
app.secret_key = os.urandom(24)
#uri = "mongodb://127.0.0.1:27017"
#client = pymongo.MongoClient(uri)
#database = client["didaccookbook"]
#collection = database["recipe"]
#recipes = collection.find({})

#app.config['MONGO_URI'] = os.environ.get("MONGODB_URI")
#app.config.from_object(Config)

##################################################################

#app.config["MONGO_DBNAME"] = 'DiDacsCookBook'
#app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
# This part is for the connection to atlas MondoDB (remote DB)
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Admin:plomez13@myfirstcluster-mfuzc.mongodb.net/DiDacsCookBook?retryWrites=true&w=majority')

#client = pymongo.MongoClient(os.getenv('MONGO_URI'))
#db = client.didaccookbook

#mongo = PyMongo(app)

#########################################################################
#Connecting to the local MondoDB

#uri = "mongodb://127.0.0.1:27017"
#client = pymongo.MongoClient(uri)
#db = client.didaccookbook
#mongodb+srv://Admin:plomez13@myfirstcluster-mfuzc.mongodb.net/didaccookbook?retryWrites=true&w=majority
uri = "mongodb+srv://Admin:plomez13@myfirstcluster-mfuzc.mongodb.net/didaccookbook?retryWrites=true&w=majority"
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
def home():
    return render_template("home.html")


######## Render recipes


#render recipe
#@app.route('/get_recipe/')
#def get_recipe():
#    cursor = db.recipe.find()
#    print( "Numero de documentos en la collection: ", cursor.count())
#    return render_template("recipe.html",
#                          recipes = cursor)

@app.route('/recipe/<recipe_id>/')
def recipe(recipe_id):
    one_recipe = db.recipe.find_one({'_id': ObjectId(recipe_id)})
    #recipe_id = str(one_recipe['recipe_id'])
    return render_template('recipe.html', recipe=one_recipe )


# Get all recipes
@app.route('/recipes')
def recipes():
    recipes = list(db.recipe.find())
    if 'recipe_search' in request.args:
        query = request.args['recipe_search']
        new_recipe_list = []
        for recipe in recipes:
            if recipe['name'].lower().find(query.lower()) != -1:
                new_recipe_list.append(recipe)
        return render_template('recipes.html', recipes=new_recipe_list)

    elif 'sort' in request.args:
        if request.args['sort'] == 'asc':
            new_recipe_list = list(db.recipes.find().sort('recipe_name', pymongo.ASCENDING))
            return render_template('recipes.html', recipes=new_recipe_list, cuisines=cuisines)
        elif request.args['sort'] == 'dsc':
            new_recipe_list = list(db.recipes.find().sort('recipe_name', pymongo.DESCENDING))
            return render_template('recipes.html', recipes=new_recipe_list, cuisines=cuisines)

    return render_template('recipes.html', recipes=recipes, )


#Get Recipes by Menu
@app.route('/menu_recipes')
def menu_recipes():
    dish_types = set()
    recipes = list(db.recipe.find())
    for recipe in recipes:
        dish_types.add(recipe['dish_type'])
    return render_template("menu_recipes.html", dish_types=dish_types, recipes=recipes)

#Get Recipes by main course
@app.route('/main_course')
def main_course():
    courses = set()
    recipes = list(db.recipe.find())
    for recipe in db.recipe.find():
        courses.add(recipe['main_course'])
    return render_template("main_course.html", courses=courses, recipes=recipes)

#Get Recipes by Cuisine type
@app.route('/cusine')
def cusine():
    cuisines = set()
    recipes = list(db.recipe.find())
    for recipe in db.recipe.find():
        cuisines.add(recipe['cusine'])
    return render_template('cusine.html', cuisines=cuisines, recipes=recipes)



########## Log in and Add recipe(only if you are sign in)

# Manage session user
@app.before_request
def before_request():
    if 'username' in session:
        g.user = session['username']

@app.route('/home')
def index():
    if 'username' in session:
        return 'You are logged in as' + session['username']

    return render_template('home.html')

# To log in in case user is already resgister
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = db.users
        login_user = users.find_one({'username': request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('home'))

        #return 'Invalid username/password combination'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('login'))

        return 'That username already exists!'

    return render_template('signup.html')

@app.route('/logout')
def logout():
    del session["username"]
    return redirect(url_for('home'))


#Add recipe, only if a member or resgister user
@app.route('/addrecipe')
def addrecipe():
    dish_types=["Startes", "Soup", "Salad", "Main", "Dessert"]
    courses=["Meat Lovers", "Vegeterian", "Vegan"]
    levels=["easy", "medium", "medium-expert", "expert", "5stars michellin"]
    """for recipe in db.recipe.find():
        dish_types.add(recipe['dish_type'])"""
    return render_template("addrecipe.html", courses=courses, dish_types=dish_types, levels=levels, users=db.users.find())


# Submit add recipe form
@app.route('/insert_recipe', methods=['POST', 'GET'])
def insert_recipe():
    recipes = db.recipe

    recipe_name = request.form['name']
    recipe_description = request.form['description']
    recipe_serving = request.form['serves']
    recipe_dish = request.form['dish_type']
    recipe_prep_time = request.form['prep_time']
    recipe_cook_time = request.form['cook_time']
    recipe_cusine = request.form['cusine']
    recipe_level = request.form['level']
    recipe_main_course = request.form['main_course']
    recipe_ingredient_name = request.form.getlist('name[]')
    recipe_ingredient_quantity = request.form.getlist('quantity[]')
    recipe_ingredient_unit = request.form.getlist('unit[]')
    recipe_preparation = request.form['preparation']
    ingredients = []

    for i, name in enumerate(recipe_ingredient_name):
        ingredients.append({
            'name': recipe_ingredient_name[i],
            'quantity' : recipe_ingredient_quantity[i],
            'unit': recipe_ingredient_unit[i]
        })
    recipe_form = {
        "name": recipe_name,
        "description": recipe_description,
        "serves": recipe_serving,
        "dish_type": recipe_dish,
        "prep_time": recipe_prep_time,
        "cook_time": recipe_cook_time,
        "cusine": recipe_cusine,
        "level": recipe_level,
        "main_course": recipe_main_course,
        "ingredients": ingredients,
        "preparation": recipe_preparation,
    }

    recipes.insert_one(recipe_form)
    return redirect(url_for('recipes'))







if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

