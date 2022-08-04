from flask import Blueprint, request, session, current_app
import json
from service.review_service import ReviewService
from model.review import Review
from exception.invalid_param_error import InvalParam

rc = Blueprint('review_controller', __name__)
rs = ReviewService()


# Create
@rc.route('/book/review', methods=['POST'])
def new_review():
    if "user" in session:
        isbn = request.form.get('isbn')
        user = request.form.get('user')
        review = request.form.get('review')
        rating = request.form.get('rating')
        rev = Review(isbn, user, review, rating)
        try:
            return rs.new_review(rev)
        except InvalParam as e:
            return {
                       "message": f"{e}"
                   }, 400

# Read


# Update


# Delete
@rc.route('/book/<review>')
def delete_review():
    pass
