from flask_login import UserMixin, login_manager

class User(UserMixin):
    def __init__(self):
        super()
        self.cart = []

    def get_user(self,):
        if User != None:
            return self
        return User()
