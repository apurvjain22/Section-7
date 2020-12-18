from codes.db import db

class ItemModel(db.Model):  # extending to db.Model, which means we are mapping the objects(userModel & itemModel) with db
    # it is creating a link b/w database and the objects.
    __tablename__ = 'items' # telling sqlalchemy the table name for the ItemModel object

    # creating columns which ItemModel object will hold.
    id = db.Column(db.Integer, primary_key=True) # our item doesn't use id, but having an id for each entity is useful.
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) # precision- numbers after a decimal point

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) # store_id should be same as store.py 'id' column.
    store = db.relationship('StoreModel') # joining with store.py

    def __init__(self, name, price, store_id):  # defining an object
        self.name = name
        self.price = price
        self.store_id = store_id # store_id which we will define will get store in db

    def json(self):  # representation of an object
        return {'store_id': self.store_id,'name': self.name, 'price': self.price}

    # it should remain classmethod becoz, it will return an object of ItemModel as opposed to a dict.
    # So instead of returning a dict, we will be return an object of type ItemModel.
    @classmethod
    def find_by_name(cls, name):
        # If we use SQLAlchemy to find a data, it doesn't find a row, it will automatically convert a row to an object,
        # if it can!
        return cls.query.filter_by(name=name).first() # SELECT * FROM items where name=name LIMIT BY 1

    """ 
    Below in insert and update methods we don't need a classmethod becoz in both the methods we are accessing item
    and we have a class ItemModel which is dealing with the item having same properties.
    And by creating a classmethod we will be making an another object which makes no sense. 
    So to access the class items property we will be removing classmethod.
    """

    # saving the model to db
    def save_to_db(self):
        # SQLAlchemy can directly translate from an object to row in a db.
        # We don't have to tell, what row data to insert, we just have to tell it to insert this object into the db.
        db.session.add(self)
        db.session.commit()
        # The session in this instance is a collection in of objects that we are going to write in a db.

        # when any name or price is updated we have to update the items in the db.
        # So SQLAlchemy will update instead of an insert.
        # So save_to_db() method is useful for both inserting and updating the items into db.


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
