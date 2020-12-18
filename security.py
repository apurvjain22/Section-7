from models.user import UserModel
"""
Instead of storing the data in memory database,
now we are storing in sqlite database
"""


# when passing a username and password in the authenticate method, it will authenticate and pass the userid as JWT token
# That token has an identity which consist of user-id.
# After having a correct JWT token, it will return a user information

# authenticate a username
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


# identifying a username
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


