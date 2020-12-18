from codes.db import db


"""
Models:
This class is not a resource becoz the API cannot receive data into this class or sends this class as a JSON represenation. 
API deals with resources such as Users, items, stores, students.
This class is essentially a helper, which stores some data about the User and methods to retrieve user data from db.

Model is an internal representation of an entity (which are linked with resources to produce some data) whereas 
Resource is an external representation of an entity.(which are called directly by an API)

Our API clients, like a website or a mobile app,think they're interacting with resources,that's what they see.
And when our API responds it responds with resources and that's what the client sees.
When we deal internally in our code with a User,for ex in our security.py file,we are using find_by_Username for example
We're not using the resource, we're using the model becoz that's what has the code that allows our programme to do.
So model is basically a helper which gives the flexibility without polluting the resource.
Models and resources are separate although they can be linked .
Ex: In UserRegister, we are using find_by_username(), which means resource is using the model, to get the data out.
Resource is use to map the endpoints such as HTTP verbs like get, post, put, delete.
"""


class UserModel(db.Model): # extending to db.Model, which means we are mapping the objects(userModel & iteModel) with db
    # and becoz of which operations like creating and retrieving can be ease from a database.

    # Now we will define a table for these objects.
    __tablename__ = 'users' # table name where UserModel object will get store
    __table_args__ = {'extend_existing': True}

    # Below are the columns which UserModel will going to have
    id = db.Column(db.Integer, primary_key=True) # id with Integer type and it would be primary key(unique & make index)
    username = db.Column(db.String(80)) # username with String type limiting to 80 characters only
    password = db.Column(db.String(80)) # password with String type limiting to 80 characters only.

    # So the below db columns should match with the name of below created properties.
    def __init__(self, username, password):
        # self.id = _id  # using this because 'id' is a keyword in python
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # as we are not using self anywhere in the below method,
    # so we will be making the below method as a classmethod
    @classmethod
    def find_by_username(cls, username):
        """ searching by username"""
        return cls.query.filter_by(username=username).first() # fetching the first row returned

    @classmethod
    def find_by_id(cls, _id):
        """ searching by userid """
        return cls.query.filter_by(id=_id).first()

# The find_by_username method, & the find_by_id method are API which acts as an interface for other parts of the prog to
# interact with the user thing. And that includes writing it to a database and retrieving it from a database.


# -----------------id----------------
# Whenever we insert a new row into the database, the SQL engine we use, SQLite in our case,
# but it could be Postgres, or MySQL, will automatically assign an id for us.
# So, we don't have to do it ourselves. And when we create the object through SQLAlchemy,the id is given to us as well.
# So SQLAlchemy would give us self.id, but when we create the object, we don't have to specify an id,
# because it is automatically generated.