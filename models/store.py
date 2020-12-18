from codes.db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True) # our item doesn't use id, but having an id for each entity is useful.
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') # many-to-one- it can have many items with the same store id

    def __init__(self, name):  # defining an object
        self.name = name

    def json(self):  # representation of an object
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    # retrieve a store by name
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM stores where name=name LIMIT BY 1

    # saving the model to db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # delete from database
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
