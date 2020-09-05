from flask import (
    Blueprint, render_template, request,
    redirect, url_for, session, flash)
from pypasswords import *
from database import db, User, Password
from .utils import *


homepage = Blueprint('homepage', __name__, static_folder='static', template_folder='templates')


@homepage.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for('homepage.new'))
    else:
        username = session.get('user')
        key = generate_key(username)

        user_id = User.query.filter_by(username=hash_it(username)).first().user_id
        passwords = Password.query.filter_by(owner_id=user_id).all()

        displayed_passwords = []
        for password in passwords:
            data = decrypt_data(key, [password.url, password.login, password.password])
            data.append(get_strength(data[2]))

            displayed_passwords.append(data)

        return render_template('home.html', passwords=displayed_passwords)


@homepage.route("/new", methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        url = request.form['url']
        login = request.form['login']
        password = request.form['password']

        username = session.get('user')
        key = generate_key(username)

        inputs = encrypt_data(key, [url, login, password])
        owner_id = User.query.filter_by(username=hash_it(username)).first().user_id

        new_password = Password(*inputs, owner_id)
        db.session.add(new_password)
        db.session.commit()

        return redirect(url_for('homepage.home'))
    else:
        return render_template('new.html')
