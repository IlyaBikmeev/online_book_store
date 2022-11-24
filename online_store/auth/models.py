from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from online_store.books_store.models import City

class RegistrationForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    first_name = StringField('Имя: ', validators=[DataRequired()])
    last_name = StringField('Фамилия: ', validators=[DataRequired()])
    login = StringField('Логин: ', validators=[DataRequired()])

    password = PasswordField('Пароль: ', validators=[DataRequired()])
    repeat_password = PasswordField('Повторите пароль: ', validators=[EqualTo('password')])


class AuthForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
