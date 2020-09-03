from app import app
from database import db, User, Password
from flask import render_template, request, redirect


@app.route("/", methods=['GET', 'POST'])
def index():
        return 'Hello, World!'


if __name__ == '__main__':
    db.create_all()
    app.run()
