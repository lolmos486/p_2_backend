class Book:
    def __init__(self, isbn, title, author, edition, genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.edition = edition
        self.reviews = []
        self.genre = genre

    def set_review(self, rev):
        self.reviews.append(rev)