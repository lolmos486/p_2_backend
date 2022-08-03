import psycopg
from model.user import User

from dao.review_dao import ReviewDao


class UserDao:
    def __init__(self):
        self.rd = ReviewDao()

class UserDao:
    def __init__(self):
        pass
# Create
    def create_user(self, user_obj):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:

                cur.execute(f"INSERT INTO project_2.users (username, password, fav_genre, date_joined) "
                            f"VALUES ('{user_obj.usn}', crypt('{user_obj.pwd}', gen_salt('bf')), "
                            f"'{user_obj.fav_genre}', '{user_obj.joined}');")

# Read
    def get_user(self, usn):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_2.users WHERE username = {usn};")
                for line in cur:
                    user = User(line[1], line[2], line[4])
                    user.set_id(line[0])
                    user.set_fav_genre(line[3])
                    user.set_admin(line[5])
                    revs = self.rd.get_reviews(user.usn, None)
                    for rev in revs:
                        user.set_review(rev)
                    return user


    def get_all_users(self):
        users = []
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_2.users;")
                for line in cur:
                    user = User(line[1], line[2], line[4])
                    user.set_id(line[0])
                    user.set_fav_genre(line[3])
                    user.set_admin(line[5])
                    users.append(user)
                return users


# Update
    def update_fav_genre(self, usn, fav_genre):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE project_2.users SET fav_genre = '{fav_genre}' WHERE username = '{usn}';")
                conn.commit()

    def update_admin(self, usn, admin):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE project_2.users SET is_admin = '{admin}' WHERE username = '{usn}';")
                conn.commit()

# Delete

    def delete_user(self, usn):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM project_2.users WHERE username = '{usn}';")
                conn.commit()