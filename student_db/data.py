import os
import click
from flask import current_app, g, flash
from flask.cli import with_appcontext
from .database.user_data import add_user, login_authenticator
from .database.student_data import (
    list_data_student,
    add_data_student,
    update_student_detail,
    delete_student,
    search_student)

'''
 created by : Ajay Singh Parmar
 Date : Febuary 12, 2019
 Description : COntaines all the database functinality for Student_NODB app can be found here.
 - The methods wriiten here will be imported used inside the views to read or update the file database.
'''


#: validate user's credential.
def validate_login(username='', password=''):
    return login_authenticator(username, password)


#: add user to the users table
def add_user_data(username='test', password='pass'):
    add_user(username, password)

#: add student for students table


def add_student_data(name='Test Student', age=18, gender='Male'):
    add_data_student(name, age, gender)

#: list all student from the databse.


def list_student_data():
    return list_data_student()

#: update the student details inside the student table


def update_student(name='', age=0, gender='', id=0):
    update_student_detail(name, age, gender, id)

#: delete the student record for specific id


def delete_student_data(id=0):
    delete_student(id)

#: search for pattern in the database.


def search_student_record(search_string=''):
    return search_student(search_string)


# def main_boiler_plate():
# 	# methods to be exported
# 	#init_db()
# 	add_user_data()
# 	add_student_data()
# 	update_student(name='Student1',roll_number='S00001')
# 	delete_student_data(roll_number='S000010')
# 	list_result = search_student_record('Stu')

# 	if validate_login(username='admin', password='password'):
# 		for student in list_result:
# 			print('\n', student)
# 	else:
# 		print('login failed')
#: end of module
