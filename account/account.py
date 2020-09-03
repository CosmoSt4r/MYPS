from flask import (
    Blueprint, render_template, request,
    redirect, url_for, session, flash)
from app import app
from pypasswords import *
from database import db, User, Password
from .utils import check_inputs_login, check_inputs_signup

account = Blueprint('account', __name__, static_folder='static', template_folder='templates')


@app.route("/")
def start_page():
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
