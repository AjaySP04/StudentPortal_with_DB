from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange
#from wtforms.widgets import NumberInput

class AddUserForm(FlaskForm):
	username = StringField('Username', validators=[ DataRequired(), Length(min=2, max=50)])
	password = PasswordField('Password', validators= [ DataRequired(), Length(min=3, max=50)])
	confirm_password = PasswordField('Confirm Password', validators=[ DataRequired(), EqualTo('password')])
	submit = SubmitField('Save')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[ DataRequired(), Length(min=2, max=50)])
	password = PasswordField('Password', validators= [ DataRequired() ])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class CreateStudentForm(FlaskForm):
	name = StringField('Username', validators=[ DataRequired(), Length(min=2, max=50)])
	age = IntegerField('Age', validators= [ DataRequired(), NumberRange(min=0, max=99, message='age') ])
	gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
	add = SubmitField('Add')

class UpdateStudentForm(FlaskForm):
	roll_number = StringField('Roll Number', validators= [DataRequired()] )
	name = StringField('Username', validators=[ DataRequired(), Length(min=2, max=50)])
	age = IntegerField('Age', validators= [ DataRequired(), NumberRange(min=0, max=99, message='age') ])
	gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
	save = SubmitField('Save')
	delete = SubmitField('Delete')
