from flask import Blueprint, request, session, current_app
import json
from service.user_serivce import UserService

uc = Blueprint('user_controller', __name__)
us = UserService()

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
