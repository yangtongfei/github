import os
from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import session
from flask import redirect
from flask import url_for
from . import db

def create_app():
	app = Flask(__name__)
	
	app.config['SECRET_KEY'] = '1'

	@app.route('/hello', methods=['GET','POST'])
	def hello():
		return render_template('hello.html')	

	@app.route('/', methods=['GET', 'POST'])
	def index():
		dp = db.Mysql()
		results = dp.get_data()
		return render_template('index.html', results=results)


	@app.route('/zhuce', methods=['GET','POST']) #注册
	def zhuce():
		if request.method == 'POST':
			name = request.form['uname']
			passwd = request.form['upasswd']
			dp = db.Mysql()
			error = None
			
			if name == "":
				error = '必须填写用户名'
			elif passwd == "":
				error = '必须填写密码'
			elif dp.youbiao.execute('SELECT name FROM user WHERE name = %s', (name)) !=0:
				error = '该用户已存在'
		
			if error is None:
				dp.youbiao.execute('INSERT INTO user (name, passwd) VALUES (%s, %s)',(name, passwd))
				dp.youbiao.connection.commit()
				dp.close_db()

				return redirect(url_for('login'))

			flash(error)
 
		return render_template('auth/zhuce.html')
	
 
	@app.route('/login', methods=['GET', 'POST']) #登陆
	def login():
		if request.method == 'POST':
			username = request.form['username']
			password = request.form['userpasswd']
			dp = db.Mysql()
			error = None
			
			if dp.youbiao.execute('SELECT name FROM user WHERE name = %s', (username)) ==  0:
				error = '用户名不正确'
			elif dp.youbiao.execute('SELECT passwd FROM user WHERE passwd = %s', (password)) ==  0 or dp.youbiao.execute('SELECT id,name FROM user WHERE name = %s AND passwd = %s', (username, password)) != dp.youbiao.execute('SELECT id,name FROM user WHERE name = %s AND passwd = %s',(username, password)):
				error = '密码错误'
			if error is None:
				return redirect(url_for('hello'))
	
			flash(error)			
		return render_template('auth/login.html')

	@app.route('/zhuxiao') #注销
	def zhuxiao():
			session.clear()
			return redirect(url_for('index'))
	
	
	@app.route('/add', methods=['GET', 'POST']) #添加数据
	def add():
		if request.method == 'POST':
			ming = request.form['userming']
			val = request.form['userval']
			dp = db.Mysql()
			error = None

			if ming == "" or val == "":
				error = '数据名和数据值不能为空'
			
			if error == None:
				dp.add_data(ming, val)
				error = '添加成功'	

			flash(error)

		return render_template('database/add_data.html')			

	@app.route('/del_db', methods=['GET', 'POST']) #删除数据
	def del_db():
		if request.method == 'POST':
			uid = request.form['nid']
			dp = db.Mysql()
			error = None
		
			if dp.youbiao.execute('SELECT id FROM biao WHERE id = %s', (uid)) == 0:
				error = '该数据id不存在'
			
			if error == None:	
				dp.del_data(uid)
				error = '删除成功'

			flash(error)

		return render_template('database/del_data.html')			
	

	return app 
