from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)

app.config.from_object('settings')
app.permanent_session_lifetime = timedelta(days=30)

db = SQLAlchemy(app)
