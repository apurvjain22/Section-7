from flask_restful import Resource
from codes.models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()  # will also return items as well.
        return {'message': 'Store not found'}, 404  # passing as a tuple

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' is already exists".format(name)},
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating the store'}, 500  # 500- Internal Server Error

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
