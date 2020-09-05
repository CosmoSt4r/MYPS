from app import app
from database import db
from account.account import account
from homepage.homepage import homepage
from flask import redirect, session, url_for

app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(homepage, url_prefix='/home')


@app.route("/", methods=['GET', 'POST'])
def index():
    if 'user' in session:
        return redirect(url_for('homepage.home'))
    else:
        return redirect(url_for('account.login'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
