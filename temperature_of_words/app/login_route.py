from flask import request, render_template, redirect, url_for, Blueprint
from app.models.user_model import User
from app import db

bp = Blueprint('login', __name__)

@bp.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')


@bp.route('/register/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        new_user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')


@bp.route('/logout')
def logout():
    db.session['logged_in'] = False
    return redirect(url_for('home'))
