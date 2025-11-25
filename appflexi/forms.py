from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from appflexi.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuario", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6, max=60)])
    confirm_password = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Criar conta")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return ValidationError("Esse e-mail ja esta cadastrado!")
        return None