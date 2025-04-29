from flask_login import login_required, logout_user
from flask import flash, redirect, url_for
from app.auth import bp

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.home'))

@bp.route('/login')
def login():
    return redirect(url_for('google.login'))