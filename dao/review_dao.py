import psycopg
from model.review import Review

class ReviewDao:
    def __init__(self):
        pass


# Create
    def new_review(self, rev_obj):
        with psycopg.connect(host="database-1.ccqnc6akbbbx.us-west-1.rds.amazonaws.com", port="5432", dbname="",
                             user="postgres", password="Demig0rg0n") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO reviews (isbn, review, usr, rating) VALUES "
                            f"(%s, %s, %s, %s);", (rev_obj.isbn, rev_obj.review, rev_obj.user, rev_obj.rating))

# Read
    def get_reviews(self, usn, isbn):
        call = "SELECT * FROM reviews"
        if usn:
            call = call + f" where usr = '{usn}'"
        if isbn:
            call = call + f" where isbn = '{isbn}'"
        call = call + ";"
        reviews = []
        with psycopg.connect(host="database-1.ccqnc6akbbbx.us-west-1.rds.amazonaws.com", port="5432", dbname="",
                             user="postgres", password="Demig0rg0n") as conn:
            with conn.cursor() as cur:
                cur.execute(call)
                for line in cur:
                    rev = Review(line[0], line[2], line[1], line[3])
                    reviews.append(rev)
                return reviews

# Update

# Delete
    def delete_review(self, isbn, user):
        return f"Did you really think you could delete something from the internet, {user}?"
