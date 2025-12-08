from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from appflexi.models import User

class PhotoForm(FlaskForm):
    photo = FileField("Foto",validators=[DataRequired()])
    submit = SubmitField("Postar")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("Usuário não encontrado!")
        return None

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuario", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6, max=60)])
    confirm_password = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Criar conta")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Esse e-mail já esta cadastrado!")
        return None

    def validade_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Usuário já cdastrado")