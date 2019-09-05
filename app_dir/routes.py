# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app_dir import app, db
from app_dir.models import User, BaseDecor, SecondDecor
from app_dir.forms import LoginForm, RegistrationForm, \
    BaseDecorForm, SecondDecorForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/laminate', methods=['get', 'post'])
@login_required
def laminate():
    form = BaseDecorForm()
    if form.validate_on_submit():
        basedecor = BaseDecor(
            indexname=form.indexname.data,
            decorname=form.decorname.data
        )
        db.session.add(basedecor)
        db.session.commit()
        flash('Поздравляю, Вы добавили новую пленку.')
        return redirect(url_for('laminate'))
    laminates = BaseDecor.query.all()
    if not laminates:
        flash('В базе еще нет пленок')
    return render_template('laminate.html', laminates=laminates, form=form)


@app.route('/glass', methods=['get', 'post'])
@login_required
def glass():
    form = SecondDecorForm()
    if form.validate_on_submit():
        seconddecor = SecondDecor(
            indexname=form.indexname.data,
            decorname=form.decorname.data
        )
        db.session.add(seconddecor)
        db.session.commit()
        flash('Поздравляю, Вы добавили новое стекло.')
        return redirect(url_for('glass'))
    glasses = SecondDecor.query.all()
    print("glass === ", glasses)
    if not glasses:
        flash('В базе еще нет стекла')
    # glasses = [
    #     {
    #         'imdexname': '1',
    #         'decorname': 'Крашеное Черное'
    #     },
    #     {
    #         'imdexname': '2',
    #         'decorname': 'Крашеное Белое'
    #     }
    # ]
    return render_template('glass.html', glasses=glasses, form=form)
