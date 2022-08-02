from exception.invalid_param_error import InvalParam

class User:
    def __init__(self, usn, pwd, joined):
        self.id = None
        self.usn = usn
        self.pwd = pwd
        self.fav_genre = None
        self.joined = joined
        self.reviews = []
        self.admin = False
        self.want_to_read = []

    def set_id(self, id):
        self.id = id

    def edit_pw(self, old_pw, new_pw):
        if old_pw == self.pwd:
            self.pwd = new_pw
        else:
            raise InvalParam("password does not match")

    def set_review(self, rev):
        self.reviews.append(rev)

    def set_admin(self, admin):
        self.admin = admin

    def set_fav_genre(self, fg):
        self.fav_genre = fg

    def get_fav_genre(self):
        return self.fav_genre

    def get_admin(self):
        return self.admin

    def __str__(self):
        return f"{self.usn} joined on {self.joined}. Their favorite genre is {self.fav_genre}."

    def set_want_to_read(self, isbn):
        self.want_to_read.append(isbn)

    def get_want_to_read(self):
        return self.want_to_read