from flask import render_template, redirect, url_for
from flask_login import logout_user, login_required
from app.user import user


@user.route('/profile')
@login_required
def profile():
    return render_template('user/profile.html')


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.start'))
