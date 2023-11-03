from . import auth
from flask import render_template
from .forms import loginform
from ..models import User
from flask import flash
from flask import request

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = loginform()
	if request.method == 'POST' :
		user = User.query.filter_by(name=form.name.data).first()
		if user is None or user.get_password(form.password.data):
			flash('用户或密码无效')
			return render_template('auth/login.html', form=form)
		return render_template('index.html')
	return render_template('auth/login.html', form=form)
