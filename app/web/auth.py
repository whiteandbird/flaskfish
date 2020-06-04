from flask import render_template, request, redirect, url_for, flash, current_app

from . import web

__author__ = '七月'

from ..email import send_message

from ..forms.auth import RegisterForm, LoginForm
from ..forms.emailform import Emailform, ResetForm
from ..models import db
from ..models.user import User,reset_password

from flask_login import login_user, logout_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method.lower() == "post" and form.validate():
        user = User()
        user.set_attr(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method.lower() == 'post' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('web.index'))
        else:
            flash("用户不存在或者密错误")
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    if request.method.lower() == 'post':
        form = Emailform(request.form)
        if form.validate():
            u_email = User.query.filter_by(email=form.email.data).first()
            if not u_email:
                return redirect(url_for('web.forget_password_request'))
            else:
                return 'http://127.0.0.1:5000/reset/password/{}'.format(u_email.generate_token())
    return render_template('auth/forget_password_request.html')


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    newpass = request.args.get('password')
    ifmod = reset_password(token,newpass)
    if ifmod:
        return 'success'

    return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    print(current_app.config.get('MAIL_PASSWORD'))
    send_message()
    return 'llllll'


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
