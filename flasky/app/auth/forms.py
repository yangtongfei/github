from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class loginform(FlaskForm):
	name = StringField('用户名', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名只能是大小写字母或下划线')])
	password = PasswordField('密码', validators=[DataRequired()])
	submit = SubmitField('登陆')


	
class registerform(FlaskForm):
	name = StringField('用户名', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名只能是大小写字母或下划线')])
	password = PasswordField('密码', validators=[DataRequired()])
	two_password = PasswordField('确认密码', validators=[DataRequired()])
	submit = SubmitField('注册')

