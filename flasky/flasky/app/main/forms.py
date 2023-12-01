from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Regexp


class addform(FlaskForm):
	date = DateField('日期', validators=[DataRequired()], format='%Y-%m-%d')
	name = StringField('名字', validators=[DataRequired(), Length(1, 64)])
	txt = TextAreaField('计划', validators=[DataRequired(), Length(0, 256)])
	submit = SubmitField('确定')


class editform(FlaskForm):
	date = DateField('日期', format='%Y-%m-%d')
	name = StringField('名字', validators=[DataRequired(), Length(1, 64)])
	txt = TextAreaField('计划', validators=[DataRequired(), Length(0, 256)])
	submit = SubmitField('确定')
	

class rmform(FlaskForm):
	submit = SubmitField('确定')
