from flask import  render_template, url_for
from flask_login import login_required
from appflexi.forms import LoginForm, RegisterForm
from appflexi import app, login_manager


@app.route('/', methods=['GET', 'POST'])
def homePage():
    login_form = LoginForm()
    return render_template('homepage.html', form=login_form)

@app.route("/createaccount", methods=['GET', 'POST'])
def createAccount():
    register_Form = RegisterForm()
    return render_template('createaccount.html', form=register_Form)

@app.route('/profile/<username>')
@login_required
def profile(username):
    return render_template('profile.html', username=username)
