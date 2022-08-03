from flask import Blueprint, request, session, current_app
import json
from service.book_service import BookService
from model.book import Book
from exception.invalid_param_error import InvalParam

bc = Blueprint('book_controller', __name__)
bs = BookService()

# Create
@bc.route('/book', methods = ['POST'])
def new_book():
    isbn = request.form.get('isbn')
    title = request.form.get('title')
    author = request.form.get('author')
    edition = request.form.get('edition')
    genre = request.form.get('genre')
    book = Book(isbn, title, author, edition, genre)
    try:
        bs.new_book(book)
        return f"{title} added to database"
    except InvalParam as e:
        return {
                   "message": f"{e}"
               }, 400
    pass

# Read
@bc.route('/books/<isbn>')
def get_book(isbn):
    try:
        return bs.get_book(isbn)
    except InvalParam as e:
        return {
                   "message": f"{e}"
               }, 400

# Update
@bc.route('/books/<isbn>', methods = ['PUT'])
def edit_book_attributes(isbn):
    pass

@bc.route('/books/<oldisbn>', methods = ['PUT'])
def edit_isbn(oldisbn):
    pass


# Delete
@bc.route('/books/<isbn>', methods = ['DELETE'])
def delete_book(isbn):
    return "No"
