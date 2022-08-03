from flask import Blueprint, request, session, current_app
import json
from service.user_serivce import UserService
from exception.invalid_param_error import InvalParam

uc = Blueprint('user_controller', __name__)
us = UserService()

@uc.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and "user" not in session:
        print("method = POST")
        json_input = request.get_json()
        usn = json_input['username']
        pwd = json_input['password']
        try:
            key = us.check_password(usn, pwd)
            session["user"] = key
            return session["user"], 200
        except InvalParam as e:
            return{
                "message": f"{e}"
            }, 400
    elif "user" in session:
         return session["user"], 200
    else:
        return "something went wrong"


@uc.route('/logout', methods=['POST'])
def logout():

    [session.pop(key) for key in list(session.keys())]
    print(session)
    return {
        'message': 'logout successful'
    }, 201


# Create
@uc.route('/users/new-user')
def create_user():
    pass

# Read
@uc.route('/users/<usn>')
def get_user(usn):
    pass

@uc.route('/users')
def get_all_users():
    pass

# Update
@uc.route('/users/<usn>', methods = ['POST'])
def update_fav_genre(usn):
    pass

@uc.route('/admin/<usn>', methods = ['POST'])
def update_admin(usn):
    pass

# Delete
@uc.route('/users/<usn>',  methods = ['DELETE'])
def delete_user(usn):
    pass
