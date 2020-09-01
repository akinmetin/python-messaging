from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import datetime


class Message(db.Document):
    receiver = db.StringField(required=True)
    message = db.StringField(required=True)
    sent_by = db.StringField(required=True)
    created_at = db.DateTimeField(required=True, default=datetime.utcnow())
    read = db.IntField(default=0)


class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Logs(db.Document):
    err_type = db.StringField(required=True)
    username = db.StringField(required=True)
    occured_at = db.DateTimeField(required=True, default=datetime.utcnow())