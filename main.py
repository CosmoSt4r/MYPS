from app import app
from database import db, User, Password
from pypasswords import *
from utils import *
from flask import render_template, request, redirect, session, url_for, flash


@app.route("/", methods=['GET', 'POST'])
def index():
    if 'user' in session:
        return 'Home'
    else:
        return redirect(url_for('login'))


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return 'Home'

    if request.method == 'POST':
        # POST

        username = request.form['username']
        password = request.form['password']

        invalid = check_inputs_login(username, password)
        if invalid:
            flash(invalid)
            return render_template('login.html', username=username)

        found_user = User.query.filter_by(username=username).first()
        if found_user:
            if hash_it(password) == found_user.password:
                session['user'] = username
                return 'Home'

        flash('Wrong username or password')
        return render_template('login.html', username=username)

    else:
        # GET

        return render_template('login.html')


@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    if 'user' in session:
        return 'Home'

    if request.method == 'POST':
        # POST

        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        invalid = check_inputs_signup(username, password, confirm_password)
        if invalid:
            flash(invalid)
            return render_template('signup.html', username=username)
        else:
            new_user = User(username, hash_it(password))
            db.session.add(new_user)
            db.session.commit()

            session['user'] = username
            return 'Home'
    else:
        # GET

        return render_template('signup.html')


if __name__ == '__main__':
    db.create_all()
    app.run()
