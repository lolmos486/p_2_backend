class Book:
    def __init__(self, isbn, title, author, edition, genre, type):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.edition = edition
        self.reviews = []
        self.genre = genre
        self.type = type

    def set_review(self, rev):
        self.reviews.append(rev)