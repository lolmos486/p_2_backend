from exception.invalid_param_error import InvalParam

class User:
    def __init__(self, usn, pwd, fav_genre, joined):
        self.id = None
        self.usn = usn
        self.pwd = pwd
        self.fav_genre = fav_genre
        self.joined = joined
        self.reviews = []
        self.admin = False

    def set_id(self, id):
        self.id = id

    def edit_pw(self, old_pw, new_pw):
        if old_pw == self.pwd:
            self.pwd = new_pw
        else:
            raise InvalParam("password does not match")

    def set_review(self, rev):
        self.reviews.append(rev)

    def set_admin_true(self):
        self.admin = True
