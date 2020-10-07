# Flask proyect starter

Hi and welcome to my proyect! :D

## Why did i decided to do this?

Have you notice it is really hard to start with a new technology specially when it is a Interpreted language?. That's what a lived with flask because I have used Java most of my programming life and when I wanted to start with flask was very difficult to find information about how to.

Sure, there are many courses and web pages where they explain and teach how to programming with python and flask but, what about TDD?...Dependency Injection?...No many places find info about it.

This Flask proyect starter has the main goal to give a skeleton to start a Flask app giving you some tools like a TestBase class to create tests which was a tried to copy from Djago's method of mocking data bases and focusing on Dependency Injection separeting all python modules in many folders.

## So...how does this works?.

### Project structure

_NOTE: This app use Flask Blueprints to organize code._

In the main folder we found the next components:
* An _app_ folder.
    
    Here is conteined all "apps" of our proyect where you can put any folder with any name focusing on what that part of code will do.

    Every folder contains the following folder structure:

    * **controllers**: If your "app" will have endpoint, here you can put all logic of each of them. This is to separate the routes from logic allowing an dependency injection.

    * **models**: Here you can put all your entities that use the ORM configurated in this proyect (Flask-SQLAlchemy) or ODM (Flask-mongoengine)

    * **services**: Here you can create the logic that each entity could have.

    * **utils**: Here you can put any code that is not a service, but is usefull to make any task

    * **templates & static**: Here you put all HTML templates and static resources your app will need

    Currently, this folder contains the next "apps":
    * **admin**

        As the name tell us, here you can put all your administrator logic.

    * **cli_manage**

        If your projects needs any CLI commands, you can put it in here

    * **config**

        This is not an app, but contains modules of configurations for each enviroment which are use to instanciate Flask object using its Flask.config.from_object method. By example:

        A local enviroment will use these configurations:
        ```
            SQLALCHEMY_DATABASE_URI = "sqlite:///local_db.db"
            SQLALCHEMY_TRACK_MODIFICATIONS = False
            MONGODB_DB = 'local_db'
            MONGODB_HOST = 'localhost'
            MONGODB_PORT = 27017
        ```

        For watch how it works the correspondent code is in app.app_factory.py

    * **testing**

        This is not an app too. Here is the test_base python module with the class TestBase to write your own tests. It initialize a MongoDB an selected SQL database. 

        It provides some usefull methods to handle databases.

    * **web**

        Here is conteined all logic for your main page.

    In the same way, this folder contains some python modules used to many task:

    * **app_factory.py**

        Here you can register your blueprints from your apps created and has the main function used in autoapp.py to instanciate the flask app

    * **dbs.py**

        Here are instanciate all databases handlers. This project has a mongo and sqlite databases configurated

    * **migrate.py**

        Here is instanciate the Flask-Migrate object to handle all SQL database changes

* A _requirement.txt_ file

    This file contains all python dependencies which you can install in your enviroment with a ```python install -r requirements.txt``` command

* A _env.sh_ file

    It contains all enviroment variables to a local deploying. These are based on the flask documentation to support custom cli commands

* An _autoapp.py_ file

    It is the python module to start the flask app with ```flask run``` command


### Did I forget something?.

I will put examples to use the project, but I was to anxious to share this in GitHub and if you find somenthig that I got wrong or you'd like to improve something in the code, please make your merge request explaining the changes you like to make and I'll check it.

If in some case you need it to use, please feel free to do it. I hope this help you to beging your proyect.

Nice!