from flask import  render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from appflexi.forms import LoginForm, RegisterForm
from appflexi import app, database, bcrypt
from appflexi.models import User, Photo


@app.route('/', methods=['GET', 'POST'])
def homepage():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            return redirect(url_for('profile', user_id=user.id))
    return render_template('homepage.html', form=login_form)

@app.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    register_Form = RegisterForm()
    if register_Form.validate_on_submit():
        password = bcrypt.generate_password_hash(register_Form.password.data)
        user = User(username = register_Form.username.data, password = password, email = register_Form.email.data)
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('profile', user_id=user.id))
    return render_template('createaccount.html', form=register_Form)

@app.route('/profile/<user_id>')
@login_required
def profile(user_id):
    if int(user_id) == int(current_user.id):
        return render_template('profile.html', user=current_user)
    else:
        user = User.query.get(int(user_id))
        return render_template('profile.html', user=user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))
