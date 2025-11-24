from flask import  render_template, url_for
from flask_login import login_required

from appflexi import app, login_manager


@app.route('/')
def HomePage():
    return render_template('homepage.html')

@app.route('/profile/<username>')
@login_required
def profile(username):
    return render_template('profile.html', username=username)
