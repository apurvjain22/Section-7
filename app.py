from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from codes.security import authenticate, identity
from codes.resources.user import UserRegister
from codes.resources.item import Item, ItemList
from codes.resources.store import Store, StoreList


app = Flask(__name__)
# telling SQLAlchemy, that where to find data.db file.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # SQLAlchemy db is gonna live at the root folder of our proj
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# If the above operation is ON, it will notify before and after changes are committed to the database.
# So we are turning off the Flask SQLAlchemy modification but SQLAlchemy modification is still on.

app.secret_key = 'apurv' # this key should be secured and also kept in private, so that it is not visible to all.
api = Api(app)

@app.before_first_request
def create_tables():
    # with app.app_context():
    #     db.init_app(app)
    db.create_all() # it only creates a table that it sees, becoz it goes through all imports.
    # so if any one is not present then the table for that won't get created.

jwt = JWT(app, authenticate, identity) # JWT creates an endpoint /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from codes.db import db
    db.init_app(app)
    app.run(debug=True)
