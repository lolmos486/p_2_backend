class Review:
    def __init__(self, isbn, user, review, rating):
        self.isbn = isbn
        self.user = user
        self.review = review
        self.rating = rating

    def to_dict(self):
        return {
            'isbn': self.isbn,
            'author': self.user,
            'rating': self.rating,
            'review': self.review
        }