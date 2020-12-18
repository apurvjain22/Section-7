from flask_restful import Resource, reqparse
from codes.models.user import UserModel

class UserRegister(Resource):
    # parser will parse through the JSON of the request
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
    parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")

    def post(self):
        # parse the arguments using the parser
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']): # if not none which means the username is already exists.
            return {'message': 'A user with that username already exists'}, 400

        user = UserModel(data['username'], data['password']) # UserModel(**data) - unpack
        user.save_to_db()

        return {'message': 'User created successfully.'}, 201
