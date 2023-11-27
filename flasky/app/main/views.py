from . import main
from flask import render_template, flash, request, redirect, url_for, session, abort
from flask_login import current_user, login_required
from .forms import addform, editform, rmform
from ..models import User, Role
from .. import db
from datetime import datetime


@main.route('/')
def base():
	return render_template('base.html')



@main.route('/index')
def index():
	user = User.query.filter_by(id=current_user.id).first()
	if user is None:
		return 0
	role = user.roles.order_by().all()
	
	p = Role.query.all()
	s = []
	n = datetime.now()
	date_y = n.month
	date_r = n.day

	date1 = datetime(n.year, date_y, date_r)

	for i in p:	
		x = datetime.strftime(i.date, "%Y-%m-%d")
		if int(date_y) > int(x[-5:-3]):
			date2 = datetime(n.year + 1, int(x[-5:-3]), int(x[-2:]))
		elif int(date_y) < int(x[-5:-3]):
			date2 = datetime(n.year, int(x[-5:-3]), int(x[-2:]))
		else:
			if int(date_r) > int(x[-2:]):
				date2 = datetime(n.year + 1, int(x[-5:-3]), int(x[-2:]))
			else:
				date2 = datetime(n.year, int(x[-5:-3]), int(x[-2:])) 
				
					
		d = date2 - date1
		
		s.append(d.days)	
		
	return render_template('main/index.html', role=zip(role, s))



@main.route('/my', methods=['GET', 'POST'])
def my():
	return render_template('main/my.html')		



@main.route('/add', methods=['GET', 'POST'])
def add():
	form = addform()
	if request.method == 'POST':
		role = Role(name = form.name.data, txt = form.txt.data, date = form.date.data, user = current_user._get_current_object())
		db.session.add(role)
		db.session.commit()
		flash('添加成功')
		return redirect(url_for('main.index'))	
	return render_template('main/add.html', form=form)




@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
	role = Role.query.get_or_404(id)
	if current_user.id != role.user_id:
		abort(403)
	form = editform()
	if request.method == 'POST':
		role.name = form.name.data
		role.txt = form.txt.data
		role.date = form.date.data
		db.session.add(role)
		db.session.commit()
		flash('修改成功')
		return redirect(url_for('.index'))
	form.name.data = role.name
	form.date.data = role.date
	form.txt.data = role.txt
	return render_template('main/edit.html', form=form, id=id)

	


@main.route('/rm/<int:id>', methods=['GET', 'POST'])
def rm(id):
	role = Role.query.get_or_404(id)
	form = rmform()
	if request.method == 'POST':
		db.session.delete(role)
		db.session.commit()
		flash('删除成功')
		return redirect(url_for('.index'))
	return render_template('main/rm.html', form=form, id=id)

