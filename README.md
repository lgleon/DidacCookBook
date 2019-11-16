
<h3 align="center">
Didacs Collaborative Cook Book
</h3>

<h3 align="center">
https://images.unsplash.com/photo-1556761223-4c4282c73f77?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60
</h3>

<h3 align="center">
This repository contains the code for an online Cookbook application. 
It is primarily built using Python (back-end) and the Flask framework and uses 
MongoDB for the database. It also uses the Materialize framework on the front-end.
That application was built for forth Milestone Project at Code Institute.
The live project can be viewed [here](https://didacscookbook.herokuapp.com/).

</h3>

## UX
 
This application is built with a mobile first, responsive design in mind.

#### User stories

- As a new user, I should:
    - see a homepage with a cover image with a tag line.
    - see a main navigation with links to main recipe categories.
    - see a signup tap to register as user.

- As a register user who wishes to create a recipe (authentication is required for this part), I should:
    - see a form allowing me to add the following fields:
        - title, description, preparation.
        - main ingredient, with the option to add/remove more ingredients as necessary.
        - choose a meal time i.e. starters/main/soup/salad/dessert etc.
        - servings per recipe.
        - cooking and preparation time.
        - cuisine i.e. Spanish, Mediterranean etc.
    - see a submit to send the form

- As a user who wants to view all recipes, I should see a link to "Recipes" where I can see preview cards of each of the stored recipes, each displaying the following:
    - thumbnail image.
    - preview icon, to view basic recipe details i.e. name and description.
    - link to the full recipe listing.

- As a user who wants to view a certain category of recipes, I should:
    - click on the category name from a link and be taken to a page only returning recipes contained within those recipes

- A a user who wants to view a full recipe, I should:
    - click on a recipe card from the recipes page and be taken to a page where I should:
        - see a page detailing the recipe:
            - Name, description.
            - servings per recipe.
            - cooking time.
            - preparation time.
            - cuisine.
            - ingredients.
            - preparation.

- As a user who wants to view all cuisines, I should see a link to "cuisines" where I can see a list of all cuisines, each displaying the following:
    - cuisine name.

- As a user who wants to view which type of Food, I should see a link to "Menu" where I can see a list of all types of food meatlovers/Vegan/Vegetarian, each displaying the following:
    - food type.

- As a user who wants to view all courses, I should see a link to "Course" where I can see a list of all options for a menu starters/salad/soup/main/dessert, each displaying the following:
    - course type.



This site was built on the basis of ideas from initial wireframes created manually in collaboration with a chef **I NEED TO MAKE PICUTRES OF TEH WIRFEIRES AND RECIPE RENDER** 


## Features
 
##### Existing Features
- The **User Registration and User Login** feature hashes user passwords so user's passwords are not stored in the application database as simple text strings as they are entered by the user when registering. This means that even by viewing the database documents you will not be able to see a user's password. The Registration form and Login forms use a lot of HTML validation including Regex pattern detection to ensure that usernames and password etc are all entered in the correct format. 

- The feature for **Adding Recipes** will be available for users who are logged in and is accessed by the 'Add recipe' button in the narbar right-hand corner, next to the user name when is logged. This will take the user to a full page form that will allow them to submit detailed information about a new recipe.

- When **Browsing Recipes** in the application a user can search recipe names by entering a search string in the provided text field and this will then search for recipes whose name includes the query string. There is a drop-down menu of cuisine types so a user can filter the recipe list by recipes only matching the selected cuisins. In addition to that there are sorting buttons to sort all recipes in the application by ascending and descending alphabetical order.

- Changing **serves** number will automaticly change the amounts of ingredientes for the recipe, in case you wan to prepare for more or less people.

##### Future Features
- A Menu prepararion is an idea that I have to allow users who are logged in to the application to preapre a whole menu, combinng i.e. starters, main and desserts etc.  

- Unique list of ingredients; The previous feature will be acompained to an implementation for the ingredients, to create a unique list of ingredients with the amounts to prepare the entire menu.

- Ingredients search, if the user want to search recipies by main ingredient provide a feature where recipes could be filtered by the ingredients they contain. For example, a user may want to only see recipes containing Chicken. This feature could be added to the search/filter/sort menu options.

## Challenges
- Learning how to integrate Flask and MongoDB was a great learning experience. I learned much from how to manage and interact with a NoSQL data store.

- Managing routes and URL's with Flask was also very interesting and I learned a great deal from reading the documentation around Flask and MongoDB.


## Technologies Used

Languages, frameworks, libraries, and any other tools used to construct this project. 

- [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
    - This project uses **HTML** to structure the content of the website.
 - [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - The project uses **CSS** to add additional styling to the site and refine responsive beahviour using media queries.
- [Bootstrap](https://getbpptstrap.com) 
    - Bootstrap is used as the primary CSS framework.
- [Materialize](https://materializecss.com/)
    - This project uses **Materialize** to provide the front-end grid framework and support responsive behaviour.
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
    - The project uses **JavaScript** to add and remove content dynamically and to initialise Materialize components.
- [jQuery](https://jquery.com/)
    - This project uses **jQuery** to assist in making asynchronous requests for and also to simplify DOM node selection and manipulation.
- [Python](https://www.python.org/)
    - This project uses **Python** as the server-side programming language to provide back-end logic and serve dynamic web pages to the browser.
- [Flask](http://flask.pocoo.org/)
    - This project uses **Flask** as the back-end framework to simplify configuration of the application and routing, to render HTML templates, work with client requests  and to assist with user session management.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - This project uses **Flask-PyMongo** to connect the application to MongoDB and for retrieving, inserting, updating and deleting data to and from the database.
- [MongoDB](https://www.mongodb.com/)
    - This project uses **MongoDB**, and more specifically MongoDB Atlas, as it's database system used to store data about users and recipes.
- [Heroku](https://www.heroku.com/) 
    - Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.




## Testing

The javascript functionality were tested using, many times  `console.log` function and similarly using `print()` in the python part, app.py, to be sure that function and routes where working as expected.   
The api was build using Google Chrome  and then later tested in other browsers; FireFox and Safary.

This project was tested for responsiveness using the Chrome Developer Tools.

All of the following routes were checked using the W3C Validation Tool [here](http://validator.w3.org), and both HTML and CSS files passed without error:
- /
- /login
- /add_recipe
- /edit_recipe/<recipe_id>/
- /recipe/<recipe_id>/
- /signup

There are a number of forms used on this application to accept user input including the login form, signup form, and search forms on the recipe list page and on the add and edit recipe pages. Various forms and levels of HTML validation has been used on form inputs to verify inputs to each form field. These forms were tested while being developed to ensure that the validation was having the desired effect and providing the desired outcome.

The site was also audited with Chrome Dev Tools' Lighthouse, with no throttling, and the results were good and were as follows on the audit report:

| Performance | Accessibility | Best Practices | SEO |
| :---------: | :------------:|:--------------:|:---:|
| 100         | 78            | 64             | 75  |

(_Progressive Web App audit scoring has been removed as the site was not intended to operate as a PWA_.)





## Deployment

GitHub was used for version control throught the development of the application and to host the code by pushing all code to the repo on GitHub.

This project was then deployed to Heroku to host the live application, following the steps below:

1. Log in to [Heroku](https://www.heroku.com/) and create a new app called 'didaccookbook'
2. Log in to Heroku in the CLI
3. Add the remote Heroku repo
4. Create the requirements.txt file by running `pip3 freeze --local > requirements.txt` in the CLI
5. Create a Procfile by running `echo web: python run.py > Procfile` in the CLI
6. Start a web process on Heroku by running `heroku ps:scale web=1` in the CLI
7. Set environment variables in Heroku for IP, PORT and MONGO_URI
8. Restart all dynos on Heroku

The live project can be viewed [here](http://didaccookbook.herokuapp.com/).



## Production Deployment

- A live version of this app is available [here](https://glacial-brook-98593.herokuapp.com/).

- The Flask application is deployed to a Heroku instance.

- The MongoDB is deployed to an mLab instance.

- Testing is triggered via TravisCI upon PR's to the GitHub repository.

- Once TravisCI builds successfully, deployment is carried out on Heroku.

##### The process I took was as follows:
- Set up a new instance of a Heroku app, along with a mLab instance.
- Store the necessary config variables in the Heroku app settings.
- Set the necessary  variables in the Flask app settings.
- Set up Travis-CI to trigger when pushes are made to the repository, set up with a yml config file.
- Set up a automatic deployment hook on Heroku to trigger once Travis-CI has completed.
- Deploy by pushing to GitHub

- If you wish to deploy - ensure you have set the following config vars set in Heroku app settings:
```
    - 'IP'
    - 'MONGO_URI'
    - 'PORT'
```


## Databse schema:
- The main MongoDB collection `recipes` takes he following schema.

```json
{
    "_id": {
        "$oid": "5c78652fe64d1e68d7eba7a6"
    },
    "name": "Chocolate cake",
    "description": "Dark chocolate sponge cake",
    "method": "Mix all ingredients. Bake for 35 mins at 180C",
    "ingredients": [
        "Chocolate",
      "6 Eggs",
      "125ml millke",
      "200g Flour"
    ],
    "meal": "dessert",
    "serves": "4",
    "cooking-time": "30",
    "prep-time": "10",
    "cuisine": "French",
    "user": "Dave",
    "last_modified": "Thu Feb 28 22:48:15 2019"
  }
```















## Credits

##### Acknowledgements

- The Authorisation function used on routes requiring user log in was based on code from a Flask Snippet written by Alex Abbott which can be found [here](http://flask.pocoo.org/snippets/98/)
- The pagination feature used on the recipe list in this application was based on a coding tutorial by David Acosta which can be found [here](https://www.youtube.com/watch?v=Xznn-ggD0GU) on YouTube
- All initial recipes (of which there are ten), including their images, were recipes taken from the BBC GoodFood website which can be found [here](https://www.bbcgoodfood.com/recipes)
