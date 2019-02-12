'''
 created by : Ajay Singh Parmar
 Date : Febuary 12, 2019
 Description : COntaines all the database functinality for Student_NODB app can be found here.
 - Thus module is written from scratch to simulate the behavior of any database query language.

 - The methods wriiten here will be imported used inside the views to read or update the file database.
'''


import os
'''
    importing neccessary objects for database these special objects are:
    current_app = this handles the flask related requests
    g - speacial object which is unique to each request 
'''
import click


from flask import current_app, g, flash
from flask.cli import with_appcontext



from .database.user_data import add_user, login_authenticator
from .database.student_data import (list_data_student, add_data_student, update_student_detail, delete_student, search_student)


# main file to load data for user.
# cwd = os.getcwd()
# FILE_USERS = os.path.join(cwd, 'student_nodb/database/user_data_file.txt')

# #:Target file where all users added or can be read to authenticate users
# TARGET_USER_FILE = os.path.join(cwd, 'student_nodb/database/temp/user/temp_user_data_file.txt')


# # main file to load data for Student.
# FILE_STUDENTS = os.path.join(cwd, 'student_nodb/database/student_data_file.txt')

# #:Target file where all students are added or CRUD operation will be performed.
# TARGET_STUDENT_FILE = os.path.join(cwd, 'student_nodb/database/temp/student/temp_student_data_file.txt')


# def load_user_data():
# 	load_data_user(FILE_USERS, TARGET_USER_FILE)

# def load_student_data():
# 	load_data_student(FILE_STUDENTS, TARGET_STUDENT_FILE)

# def init_db():

# 	#: load data for user authentications
# 	load_user_data()

# 	#: load student data for CRUD operations.
# 	load_student_data()


def validate_login(username='', password=''):
	return login_authenticator(username, password)

def add_user_data(username='test', password='pass'):
	add_user(username, password)

def add_student_data(name='Test Student', age=18, gender='Male'):
	add_data_student(name, age, gender)

def list_student_data():
	return list_data_student()

def update_student(name='', age=0, gender='', id=0):
	update_student_detail(name, age, gender, id)

def delete_student_data(id=0):
	delete_student(id)

def search_student_record(search_string=''):
	return search_student(search_string)



# # : We will be creating a command for initializing the database for the application.
# # : before loading the app, it should be called inorder to configure all data.
# # : Here we are adding command into flask for initializing app database.
# @click.command('init_db')
# @with_appcontext
# def init_db_command():
#     #: clear the existing data and make fresh tables using the command.'''
#     init_db()
#     click.echo('Initialized Student Database')

# def init_app(app):
#     #: makes flask to call function while clean up 
#     # add the command into flask <command> in this case : flask init_db
#     app.cli.add_command(init_db_command) 


def main_boiler_plate():
	# methods to be exported
	#init_db()
	add_user_data()
	add_student_data()
	update_student(name='Student1',roll_number='S00001')
	delete_student_data(roll_number='S000010')
	list_result = search_student_record('Stu')

	if validate_login(username='admin', password='password'):
		for student in list_result:
			print('\n', student)
	else:
		print('login failed')
