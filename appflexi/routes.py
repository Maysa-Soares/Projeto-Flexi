from flask import  render_template, url_for
from appflexi import app

@app.route('/')
def HomePage():
    return render_template('homepage.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)
