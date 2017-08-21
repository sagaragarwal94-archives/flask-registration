from flask import render_template, redirect, url_for
from flask_login import current_user, logout_user, login_required
from app.user import user
from app import mongo


@user.route('/profile')
@login_required
def profile():
    return render_template('user/profile.html')


@user.route('/logout')
@login_required
def logout():
    mongo.db.users.update({'email': current_user.email}, {'$set': {'authenticated': False}})
    logout_user(current_user)
    return redirect(url_for('home.start'))
