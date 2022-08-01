import psycopg
from model.user import User


class UserDao:
    def __init__(self):
        pass
# Create
    def create_user(self, user_obj):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO project_2.users (username, password, fav_genre, date_joined VALUES"
                            f"('{user_obj.usn}', crypt('{user_obj.pwd}', gen_salt('bf')), '{user_obj.fav_genre}', "
                            f"'{user_obj.joined}';")


# Read
    def get_user(self, username):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="password") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM project_2.users WHERE username = '{username}';")
                for line in cur:
                    user = User(line[1], line[2], line[3], line[4])
                    user.set_id(line[0])
                    if line[5]:
                        user.set_admin_true()
                    return user



# Update

# Delete