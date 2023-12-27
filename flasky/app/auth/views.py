from . import auth
from flask import render_template, request, redirect, url_for, session, flash
from flask_login import logout_user, login_required, login_user, current_user
from .forms import loginform, registerform, editform
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
		if user is None or user.get_password(form.password.data) is False:
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





@auth.route('/my', methods=['GET', 'POST'])
def my():
	return render_template('auth/my.html')		





@auth.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
	form = editform()
	user = User.query.filter_by(id=current_user.id).first()
	if request.method == 'POST':
		if form.name.data == user.name or form.password.data == user.password:
			flash('不能与之前的用户名或密码一样')
			return render_template('auth/edit_user.html', form=form)
		user = User.query.filter_by().first()
		if user.query.filter_by(name=form.name.data).first() is not None:
			print(user.query.filter_by(name=form.name.data).first())
			flash('用户名冲突')
			return render_template('auth/edit_user.html', form=form)
		
		user.name = form.name.data
		user.password = form.password.data
		db.session.add(user)
		db.session.commit()
		flash('修改成功')
		return render_template('auth/my.html')
	return render_template('auth/edit_user.html', form=form)
