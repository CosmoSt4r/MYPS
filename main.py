from app import app
from database import db, User, Password
from utils import check_inputs
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
    else:
        if request.method == 'POST':
            # POST

            username = request.form['username']
            password = request.form['password']

            invalid = check_inputs(username, password)
            if invalid:
                flash(invalid)
                return render_template('login.html', username=username)

            found_user = User.query.filter_by(username=username).first()
            if found_user:
                if password == found_user.password:
                    session['user'] = username
                    return 'Home'
                else:
                    flash('Wrong password')
                    return render_template('login.html', username=username)
            else:
                flash('User not found')
                return render_template('login.html', username=username)
        else:
            # GET

            return render_template('login.html')


@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    db.create_all()
    app.run()
