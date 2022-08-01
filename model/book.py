class Book:
    def __init__(self, isbn, title, author, edition):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.edition = edition
        self.reviews = {}