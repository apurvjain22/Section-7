import inspect

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from codes.models.item import ItemModel


"""
If anything changes we are changing the API
"""

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank.')
    parser.add_argument('store_id', type=float, required=True, help='Every item needs a store id.')

    @jwt_required() # we are using the decorator in front of the get method.
    # we will be authenticating before using the get method.
    def get(self, name):  # Retrieve item

        item = ItemModel.find_by_name(name) # now returns an itemModel object as opposed to a dict.
        print(item)
        if item:
            return item.json() # so now we will be returning itemModel object
        return {'message': 'Item not found'}, 404 # returning if the item is None

    def post(self, name):  # creating item

        # print(inspect.getmembers(ItemModel.find_by_name(name)))
        # print(ItemModel.find_by_name(name).__dict__)

        # checking if the name is already present or not.
        if ItemModel.find_by_name(name):
            return {'message': 'An item with the name "{}" already exists'.format(name)}, 400 # Bad Request

        data = Item.parser.parse_args() # accessing the JSON response.
        item = ItemModel(name, data['price'], data['store_id'])
        print(item)
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred while inserting'}, 500 # 500-Internal Server Error(Not users mistake)
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}

# Note:
    # In put(), we are updating and creating a new item.
    # creating a new item, is being done in post(), but to call post would be a task for us.
    # so we have created an insert() method, which can insert items as well call from post() as well as put()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id']) # creating a new item
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()

class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}
        # return {'item': list(map(lambda x: x.json(), ItemModelquery.all()))} - can be another way



class Student(Resource):
    def get(self, name):
        return {'student': name}