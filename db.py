from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # this is an SQLAlchemy object and it is going to link to our app.py
# It is going to allow us to map column objects present in our model class to rows in a database.