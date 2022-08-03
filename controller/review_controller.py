from flask import Blueprint, request, session, current_app
import json
from service.review_service import ReviewService

rc = Blueprint('review_controller', __name__)
rs = ReviewService()


# Create
@rc.route('/book/review', methods=['POST'])
def new_review():
    pass

# Read
@rc.route('/book')
def get_reviews():
    pass

# Update

# Delete
@rc.route('/book/<review>')
def delete_review():
    pass
