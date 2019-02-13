from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange
#from wtforms.widgets import NumberInput


#: Form for adding user to user database.
class AddUserForm(FlaskForm):
    username = StringField(
        'Username', validators=[
            DataRequired(), Length(
                min=2, max=50)])
    password = PasswordField(
        'Password', validators=[
            DataRequired(), Length(
                min=3, max=50)])
    confirm_password = PasswordField(
        'Confirm Password', validators=[
            DataRequired(), EqualTo('password')])
    submit = SubmitField('Save')


#: Form for adding user to user database.
class LoginForm(FlaskForm):
    username = StringField(
        'Username', validators=[
            DataRequired(), Length(
                min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


#: Form to create/add Student to student application.
class CreateStudentForm(FlaskForm):
    name = StringField(
        'Username', validators=[
            DataRequired(), Length(
                min=2, max=50)])
    age = IntegerField(
        'Age',
        validators=[
            DataRequired(),
            NumberRange(
                min=0,
                max=99,
                message='age')])
    gender = SelectField(
        'Gender', choices=[
            ('Male', 'Male'), ('Female', 'Female')])
    add = SubmitField('Add')


#: Form to update the student details - similar to create form.
class UpdateStudentForm(FlaskForm):
    roll_number = StringField('Roll Number', validators=[DataRequired()])
    name = StringField(
        'Username', validators=[
            DataRequired(), Length(
                min=2, max=50)])
    age = IntegerField(
        'Age',
        validators=[
            DataRequired(),
            NumberRange(
                min=0,
                max=99,
                message='age')])
    gender = SelectField(
        'Gender', choices=[
            ('Male', 'Male'), ('Female', 'Female')])
    save = SubmitField('Save')
    delete = SubmitField('Delete')
