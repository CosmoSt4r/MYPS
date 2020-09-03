from app import db
from datetime import datetime


class User(db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    user_pass = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)

    passwords = db.relationship('Password', backref='user', lazy=True)


class Password(db.Model):

    pass_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    url = db.Column(db.String, nullable=False)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)
