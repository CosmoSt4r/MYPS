from flask import (
    Blueprint, render_template, request,
    redirect, url_for, session, flash)
from app import app
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

        return render_template('home.html')


@homepage.route("/new", methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        url = request.form['url']
        login = request.form['login']
        password = request.form['password']

        username = session.get('user')
        key = generate_key(username)
        inputs = encrypt_data(key, [url, login, password])

        return render_template('new.html')  # # #
    else:
        return render_template('new.html')
