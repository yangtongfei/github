from . import db
from werkzeug.security import generate_password_hash, check_password_hash




class Permission:
	r = 4
	w = 2
	x = 1	


class User(db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True, nullable=False)
	password_hash = db.Column(db.String(128))
	

	def password(self, password):
		self.password_hash = generate_password_hash(password)
	
	def get_password(self, password):
		return check_password_hash(self.password_hash, password)	
	


class Role(db.Model):
	
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	title = db.Column(db.String(64))
	body = db.Column(db.String(256))



