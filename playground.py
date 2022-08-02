from dao.user_dao import UserDao
from dao.review_dao import ReviewDao
from dao.book_dao import BookDao
from model.user import User
from model.book import Book
from model.review import Review
import datetime


ud = UserDao()
rd = ReviewDao()
bd = BookDao()

today = datetime.date.today()
print(today)

# u1 = User('Bren', 'tabaxi', today)
# b1 = Book(9780786966912, "Explorer's Guide to Wildemount", "Matthew Mercer", "1", "TTRPG")

# ud.create_user(u1)
# bd.new_book(b1)