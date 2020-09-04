from flask import (
    Blueprint, render_template, request,
    redirect, url_for, session, flash)
from app import app
from pypasswords import *
from database import db, User, Password

homepage = Blueprint('homepage', __name__, static_folder='static', template_folder='templates')


@homepage.route("/")
def home():
    if request.method == 'POST':
        pass
    else:
        return render_template('home.html')
