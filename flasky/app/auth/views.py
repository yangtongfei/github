from . import auth
from flask import render_template, request, redirect, url_for, session, flash
from flask_login import logout_user, login_required, login_user
from .forms import loginform, registerform
from ..models import User
from .. import db



@auth.route('/register', methods=['GET', 'POST'])
def register():
	form =registerform()
	if request.method == 'POST':
		user = User.query.filter_by(name=form.name.data).first()
		if user:
			flash('该用户名已注册')
			return render_template('auth/register.html', form=form)
		elif form.password.data != form.two_password.data:
			flash('密码不一致')
			return render_template('auth/register.html', form=form)
		user = User(name=form.name.data, password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('注册成功')
		return redirect(url_for('auth.login'))
		
	return render_template('auth/register.html', form=form)



@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = loginform()
	if request.method == 'POST' :
		user = User.query.filter_by(name=form.name.data).first()
		if user is None or user.query.filter_by(password=form.password.data).first() is None:
			flash('用户或密码无效')
			return render_template('auth/login.html', form=form)
		login_user(user)
		flash('登录成功')
		return redirect(url_for('main.index'))
	return render_template('auth/login.html', form=form)



@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('退出登录')
	return redirect(url_for('main.base'))
