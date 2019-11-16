
<h3 align="center">
Didacs Collaborative Cook Book
</h3>

<h3 align="center">
https://images.unsplash.com/photo-1556761223-4c4282c73f77?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60
</h3>

<div align="center">
[DidacCookBook](https://github.com/lgleon/DidacCookBook.git) This repository contains the 
code for an online Cookbook application. It is primarily built using Python (back-end) and the 
Flask framework and uses MongoDB for the database. It also uses the Materialize framework on 
the front-end.
That application was built for forth Milestone Project at Code Institute.
The live project can be viewed [here](https://didacscookbook.herokuapp.com/).

</div>


## Contents Table

1. [**UX**](#ux)
    - [**user storires**](#how you experience it as user)
    - [**Design Ideas**](#design-ideas)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
    - [**Challenges**](#learning challenges)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Contents**](#contents)
    - [**Media**](#media)
    - [**Acknowledgements and Inspiration**](#acknowledgements)

7. [**Disclaimer**](#disclaimer)


## UX
 
This application is built with a mobile first, responsive design in mind.

### User stories

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


### Design ideas

The design of this cook book is base of the needs of a Chef (Didac Verdager) who is 
working in a restaurant and wanted a place where he can store and visualize his recipes 
and share with other collaborators. 
 
 ### Wireframes

There are no computer, mobile or any digital wireframes or mockups. 
There is a paper wireframe, picture included in the folder (readme_info/)




## Features
 
### Existing Features

- The **User Registration and User Login** feature hashes user passwords so user's passwords are not stored in the application database as simple text strings as they are entered by the user when registering. This means that even by viewing the database documents you will not be able to see a user's password. The Registration form and Login forms use a lot of HTML validation including Regex pattern detection to ensure that usernames and password etc are all entered in the correct format. 

- The feature for **Adding Recipes** will be available for users who are logged in and is accessed by the 'Add recipe' button in the narbar right-hand corner, next to the user name when is logged. This will take the user to a full page form that will allow them to submit detailed information about a new recipe.

- When **Browsing Recipes** in the application a user can search recipe names by entering a search string in the provided text field and this will then search for recipes whose name includes the query string. There is a drop-down menu of cuisine types so a user can filter the recipe list by recipes only matching the selected cuisins. In addition to that there are sorting buttons to sort all recipes in the application by ascending and descending alphabetical order.

- Changing **serves** number will automaticly change the amounts of ingredientes for the recipe, in case you wan to prepare for more or less people.


### Features Left to implement

- A Menu prepararion is an idea that I have to allow users who are logged in to the application to preapre a whole menu, combinng i.e. starters, main and desserts etc.  

- Unique list of ingredients; The previous feature will be acompained to an implementation for the ingredients, to create a unique list of ingredients with the amounts to prepare the entire menu.

- Ingredients search, if the user want to search recipies by main ingredient provide a feature where recipes could be filtered by the ingredients they contain. For example, a user may want to only see recipes containing Chicken. This feature could be added to the search/filter/sort menu options.


### Challenges

- Learning how to integrate Flask and MongoDB was a great learning experience. I learned much from how to manage and interact with a NoSQL data store.

- Managing routes and URL's with Flask was also very interesting and I learned a great deal from reading the documentation around Flask and MongoDB.




## Technologies Used

Languages, frameworks, libraries, and any other tools used to construct this project. 


- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - **HTML5** HyperText Markup Language.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - **CSS3** Cascading Style Sheets.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - **Javasript** is a high-level, interpreted programming language.
- [PyCharm](https://www.jetbrains.com/pycharm/)
    - **PyCharm** Is the IDE used to develop the website.
- [GitHub](https://github.com/)
    - **Github** is used: 
    1. As a remote backup of code used in the project.
    2. As a remote server for another user to see the code used in the project.
    3. For users to view the deployed version of the website. The deployed version can be viewed [here!](https://lgleon.github.io/genomic_data/).
- [Bootstrap](https://www.bootstrapcdn.com/)
    - **Bootstrap** is used to create easier & cleaner responsiveness in addition with helping maintain padding and margins.
    - It's also used to include modal features to the website to give it a professional look.
- [JQuery](https://jquery.com)
    - **JQuery** has been used to simplify DOM manipulation.
- [Materialize](https://materializecss.com/)
    - **Materialize** to provide the front-end grid framework and support responsive behaviour.
- [Python](https://www.python.org/)
    - **Python** as the server-side programming language to provide back-end logic and serve dynamic web pages to the browser.
- [Flask](http://flask.pocoo.org/)
    - **Flask** as the back-end framework to simplify configuration of the application and routing, to render HTML templates, work with client requests  and to assist with user session management.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - **Flask-PyMongo** to connect the application to MongoDB and for retrieving, inserting, updating and deleting data to and from the database.
- [MongoDB](https://www.mongodb.com/)
    - **MongoDB**, and more specifically MongoDB Atlas, as it's database system used to store data about users and recipes.
- [Heroku](https://www.heroku.com/) 
    - **Heroku**, Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.



## Testing

The javascript functionality were tested using, many times  `console.log` function and similarly using `print()` in the python part, app.py, to be sure that function and routes where working as expected.   
The api was build using Google Chrome  and then later tested in other browsers; FireFox and Safary.

This project was tested for responsiveness using the Chrome Developer Tools.



## Deployment

The project was built using [PyCharm](https://www.jetbrains.com/pycharm/), through a built-in function called 'Git', I could commit
the project & push it up to [GitHub](https://github.com/).

- To view the deployed version of [Genomic Data](https://lgleon.github.io/DidacCookBook/) I needed to take the following steps:
    - Log in to [GitHub](https://github.com/).
    - Select **lgleon/genomic_data** from the list of repositories.
    - Select **Settings** from the navbar near the top of the page.
    - Scroll down to where it says **Github Pages**, there is a subtitle labelled **Source**, click that and change the source to be **master branch**.
    - The page is automatically refreshed and ready for deployment, it can take up to 5-10 minutes for it to be viewable.

- To add this repository to your local workspace:
    - Click on the [Genomic Data repository on GitHub!](https://lgleon.github.io/DidacCookBook) link.
    - Select the green button on the right-hand side named **Clone or download** and copy the clone URL.
    - Go into your local workspace and open up a new terminal (git bash).
    - You will need to be inside of the directory that you want to add the cloning to.
    - Type `git clone ` and paste the URL you copied from GitHub and press enter. It should look like this: 
```console
git clone https://github.com/*username*/*repository*
```
The process of cloning will now be completed. For further information on cloning,
visit [How to clone from GitHub](https://help.github.com/en/articles/cloning-a-repository).

This project was then deployed to Heroku to host the live application, following the steps below:

1. Log in to [Heroku](https://www.heroku.com/) and create a new app called 'didaccookbook'
2. Log in to Heroku in the CLI
3. Add the remote Heroku repo
4. Create the requirements.txt file by running `pip3 freeze --local > requirements.txt` in the CLI
5. Create a Procfile by running `echo web: python run.py > Procfile` in the CLI
6. Start a web process on Heroku by running `heroku ps:scale web=1` in the CLI
7. Set environment variables in Heroku for IP, PORT and MONGO_URI
8. Restart all dynos on Heroku

The live project can be viewed [here](https://didacscookbook.herokuapp.com/).


## Databse schema:
- The main MongoDB collection `didaccookbook.recipe` takes he following schema.

```json
{
    "_id": {
        "$oid": "5d8c81eefbfb79a5bfd27f90"
    },
    "name": "Gazpacho",
    "description": "Traditional Spanish cold soup perfect for summer and super tasty",
    "image_url": "https://images.unsplash.com/photo-1529566186297-155c18f9a434?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
    "n_service": 20,
    "dish_type": "Soup",
    "prep_time": [{
        "p_time": 45,
        "tm_unit": "min"
    }],
    "cook_time": [{
        "c_time": "1",
        "time_unit": "min"
    }],
    "cusine": "mediterranean",
    "level": "easy",
    "main_course": "Vegetarian",
    "ingredients": [{
            "name": "tomatoes",
            "quantity": 5,
            "unit": "kg"
        },
        {
            "name": "pepinos",
            "quantity": 2,
            "unit": "enteros"
        },
        {
            "name": "garlic",
            "quantity": 1,
            "unit": "tps"
        },
        {
            "name": "sherry vinegar",
            "quantity": {
                "$numberDecimal": "0.25"
            },
            "unit": "litro"
        },
        {
            "name": "aceite de oliva virgen",
            "quantity": {
                "$numberDecimal": "0.5"
            },
            "unit": "litro"
        }
    ],
    "preparation": "Wash the vegetables, Chop the tomatoes in medium size cubes, peel the cucumbers and chop them in the size of the tomatoes deseed the pepper and cut it small. Add the garlic and some salt and leave for 15 min to rest. Blend all the ingredients, when smooth add  the oil slowly to allow to emulsionate, add the vinegar, salt to taste. If is too thick add some water "
}
```


## Credits

### Content
- All Content has been thought of and written by the Developer. 
- The content of the project is original from Didac personal recipe list.

### Media
- The images for the recipes and home page are taken from:
 [Unsplash](https://unsplash.com/s/photos/cuisine)


## Acknowledgements and Inspiration

- I got Inspiration for this project looking into other cookbooks or applications in the web.
A huge thank you to:

- Spencer Barriball (Super_Spence_mentor) - For discussing ideas, providing help wherever needed also
coaching and "dont give up you are doing great" moments.

- Luis Rodil and David van Zessen for share ideas, show me where lo look and their patience.


## Disclaimer

All content on the website, including images, are used for educational purposes only.
