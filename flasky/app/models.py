from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from flask_login import UserMixin
from sqlalchemy import Text



class User(UserMixin, db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True, nullable=False)
	password = db.Column(db.String(128))

	roles = db.relationship('Role', backref='user', lazy='dynamic')
	

#	def password(self, password):
#		self.password_hash = generate_password_hash(password)
#	
#	def get_password(self, password):
#		return check_password_hash(self.password_hash, password)	
	


class Role(UserMixin, db.Model):
	
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	txt = db.Column(Text)
	date = db.Column(db.Date, nullable=False)
	image = db.Column(db.String(255), unique=True)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))




@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
