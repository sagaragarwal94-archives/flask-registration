from app import bcrypt
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, email):
        self.email = email

    @staticmethod
    def is_authenticated(self):
        self.authenticated = True

    def get_id(self):
        return self.email

    @staticmethod
    def validate_login(password_hash, password):
        return bcrypt.check_password_hash(password_hash, password)