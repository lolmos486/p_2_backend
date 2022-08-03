from flask import Blueprint, request, session, current_app
import json
from service.book_service import BookService

bc = Blueprint('book_controller', __name__)
bs = BookService()

# Create
@bc.route('/book', methods = ['PUT'])
def new_book():
    pass

# Read
@bc.route('/books/<isbn>')
def get_book(isbn):
    pass

# Update
@bc.route('/books/<isbn>', methods = ['POST'])
def edit_book_attributes(isbn):
    pass

@bc.route('/books/<oldisbn>', methods = ['POST'])
def edit_isbn(oldisbn):
    pass


# Delete

