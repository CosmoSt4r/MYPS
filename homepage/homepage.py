from flask import (
    Blueprint, render_template, request,
    redirect, url_for, session, flash)
from pypasswords import *
from database import db, User, Password
from .utils import *


homepage = Blueprint('homepage', __name__, static_folder='static', template_folder='templates')


@homepage.route("/", methods=['POST', 'GET'])
def home():
    if 'user' not in session:
        return redirect(url_for('account.login'))

    if request.method == 'POST':
        # POST

        session.pop('user')
        flash("You've been logged out")
        return redirect(url_for('account.login'))
    else:
        # GET

        username = session.get('user')
        key = generate_key(username)

        user_id = User.query.filter_by(username=hash_it(username)).first().user_id
        passwords = Password.query.filter_by(owner_id=user_id).all()

        displayed_passwords = []
        for password in passwords:
            data = decrypt_data(key, [password.url, password.login, password.password])
            data.append(get_strength(data[2]))
            data.append(password.pass_id)

            displayed_passwords.append(data)

        return render_template('home.html', passwords=displayed_passwords)


@homepage.route("/new", methods=['POST', 'GET'])
def new():
    if 'user' not in session:
        return redirect(url_for('account.login'))

    if request.method == 'POST':
        # POST

        url = request.form['url']
        login = request.form['login']
        password = request.form['password']

        invalid = check_inputs(url, login, password)
        if invalid:
            flash(invalid)
            return render_template('new.html', url=url, login=login, password=password)
        else:
            username = session.get('user')
            key = generate_key(username)

            inputs = encrypt_data(key, [url, login, password])
            owner_id = User.query.filter_by(username=hash_it(username)).first().user_id

            new_password = Password(*inputs, owner_id)
            db.session.add(new_password)
            db.session.commit()

            return redirect(url_for('homepage.home'))
    else:
        # GET

        return render_template('new.html')


@homepage.route('/delete/<int:pass_id>')
def delete(pass_id):
    if 'user' not in session:
        return redirect(url_for('account.login'))

    pass_to_delete = Password.query.get_or_404(pass_id)

    db.session.delete(pass_to_delete)
    db.session.commit()

    return redirect(url_for('homepage.home'))


@homepage.route('/update/<int:pass_id>', methods=['GET', 'POST'])
def update(pass_id):
    if 'user' not in session:
        return redirect(url_for('account.login'))

    password_to_update = Password.query.get_or_404(pass_id)
    username = session.get('user')
    key = generate_key(username)

    if request.method == 'POST':
        # POST

        url = request.form['url']
        login = request.form['login']
        password = request.form['password']

        invalid = check_inputs(url, login, password)
        if invalid:
            flash(invalid)
            return render_template('new.html', url=url, login=login, password=password)
        else:
            inputs = encrypt_data(key, [url, login, password])

            password_to_update.url = inputs[0]
            password_to_update.login = inputs[1]
            password_to_update.password = inputs[2]

            db.session.commit()

            return redirect(url_for('homepage.home'))

    else:
        # GET
        password = Password.query.filter_by(pass_id=pass_id).first()

        data = decrypt_data(key, [password.url, password.login, password.password])

        return render_template('update.html', password=data)
