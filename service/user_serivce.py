from dao.user_dao import UserDao

class UserService():
    def __init__(self):
        self.ud = UserDao()

# Create
    def create_user(self, user_obj):
        return self.ud.create_user(user_obj)

# Read
    def get_user(self, usn):
        return self.ud.get_user(usn)

    def get_all_users(self):
        return self.ud.get_all_users()

# Update
    def update_fav_genre(self, usn, fav_genre):
        return self.ud.update_fav_genre(usn, fav_genre)

    def update_admin(self, usn, admin):
        return self.ud.update_admin(usn, admin)

# Delete
    def delete_user(self, usn):
        return self.ud.delete_user(usn)

