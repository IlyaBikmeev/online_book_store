from flask import Blueprint, render_template, flash, redirect
from online_store import db, login_manager
from online_store.books_store.models import Client
from online_store.auth.models import RegistrationForm, AuthForm 
from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return Client.query.filter_by(id=user_id).first()

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.data.get('email')
        password = form.data.get('password')
        first_name = form.data.get('first_name')
        last_name = form.data.get('last_name')
        login = form.data.get('login')
        city_name = form.data.get('city_name')

        #Проверяем, чтобы не было пользователя в бд с таким email
        existing_user = Client.query.filter_by(email=email).first()
        if existing_user:
            flash('Такой пользователь уже существует', 'danger')

        else:
            user = Client(first_name, last_name, email, login, password, None)
            db.session.add(user)
            db.session.commit()
            flash('Вы успешно зарегистрированы!', 'success')
            return redirect('/login')

    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = AuthForm()
    if form.validate_on_submit():
        email = form.data.get('email')
        password = form.data.get('password')

        existing_user = Client.query.filter_by(email=email).first()

        if not existing_user or not existing_user.check_password(password):
            flash('Неверный логин или пароль!', 'danger')
        else:
            login_user(existing_user)
            flash('Вы успешно авторизовались', 'success')
            return redirect('/')

    return render_template('auth.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/')