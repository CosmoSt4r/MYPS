from app import app
from database import db, User, Password
from account.account import account
from flask import render_template, request, redirect, session, url_for, flash

app.register_blueprint(account, url_prefix='/account')


@app.route("/", methods=['GET', 'POST'])
def index():
    if 'user' in session:
        return 'Home'
    else:
        return redirect(url_for('account.login'))


if __name__ == '__main__':
    db.create_all()
    app.run()
