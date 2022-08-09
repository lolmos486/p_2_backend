from dao.user_dao import UserDao
from dao.review_dao import ReviewDao
from dao.book_dao import BookDao
from model.user import User
from model.book import Book
from model.review import Review
from service.user_serivce import UserService
import datetime
import psycopg
import os


ud = UserDao()
rd = ReviewDao()
bd = BookDao()
us = UserService()

today = datetime.date.today()
print(today)

# u1 = User('Bren', 'tabaxi', today)
# b1 = Book(9780786966912, "Explorer's Guide to Wildemount", "Matthew Mercer", "1", "TTRPG", "book")

# ud.create_user(u1)
# bd.new_book(b1)
# rev = "I really liked EGtM! It builds a framework that I can then use to break my players."
# r1 = Review(9780786966912, 'Bren', rev, 5)
# rd.new_review(r1)

# print(ud.get_all_usernames())
# print(us.check_password('Bren', 'tabaxi'))
#
# with psycopg.connect(host="database-1.ccqnc6akbbbx.us-west-1.rds.amazonaws.com", port="5432", dbname="",
#                      user="postgres", password="Demig0rg0n") as conn:
#     print("connection successful")

print(os.environ['P2HOST'])
print(os.environ['P2PORT'])
print(os.environ['P2USER'])
print(os.environ['P2PW'])
