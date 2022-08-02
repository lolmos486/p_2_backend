import psycopg
from dao.review_dao import ReviewDao
from model.book import Book

class BookDao:
    def __init__(self):
        self.rd = ReviewDao()

# Create
    def new_book(self, book_obj):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO project_2.books (isbn, title, author, edition) VALUES "
                            f"(%s, %s, %s, %s);", (book_obj.isbn, book_obj.title, book_obj.author, book_obj.edition))
                conn.commit()


# Read
    def get_book(self, isbn):
        book = None
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_2.books WHERE isbn = '{isbn}';")
                for line in cur:
                    book = Book(line[0], line[1], line[2], line[3], line[4])
                revs = self.rd.get_reviews(None, isbn)
                for rev in revs:
                    book.set_review(rev)
                return book

    def get_genre_list(self):
        genres = []
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT DISTINCT genre FROM project_2.books")
                for line in cur:
                    genres.append(line)
                return genres

# Update
    def edit_book_attributes(self, book_obj):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE project_2.books SET title = '{book_obj.title}', author = '{book_obj.author}',"
                            f"edition = '{book_obj.edition}', genre = '{book_obj.genre}' "
                            f"WHERE isbn = '{book_obj.isbn}';")
                conn.commit()


    def edit_isbn(self, old_isbn, new_book_obj):
        self.new_book(new_book_obj)
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE project_2.reviews SET isbn = '{new_book_obj.isbn}' WHERE isbn = '{old_isbn}';")
                cur.execute(f"DELETE FROM project_2.books WHERE isbn = '{old_isbn}';")
                conn.commit()


# Delete
