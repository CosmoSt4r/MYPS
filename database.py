from app import db
from datetime import datetime


class User(db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)

    passwords = db.relationship('Password', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}({self.user_id})>'


class Password(db.Model):

    pass_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password

    def __repr__(self):
        return f'<{self.url} - {self.login}>'

