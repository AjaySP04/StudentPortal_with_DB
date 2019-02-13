'''
 created by : Ajay Singh Parmar
 Date : Febuary 12, 2019
 Description : COntaines all the database functinality for user authentication can be found here.
 - Thus module is written from scratch to simulate the behavior of any database query language.

 - The methods wriiten here will be imported inside data.py in main project directory.
'''


import os
import sys

#: re for regex functinality.
#: used in search.
import re

# importing werkzeug security features for password protection.
from werkzeug.security import check_password_hash, generate_password_hash

# importing db into the module
from student_db.student_db import get_db

from flask import flash


# '''
# 	Process flow:
# 	Read the file:
# 		- count = 0
# 		- if present :
# 			- count how many records -> count will be used for id
# 		- else if not present:
# 			- count = 1
# 		- open file in write mode and append the id and admin and password
# '''


'''
	Delete a particular user from database.
'''
# def delete_user(file, _id=1):
# 	#: read the data
# 	data = read_file_as_json(file)

# 	for user in data['users']:
# 		#: Can fetch user from its id.
# 		#: NOT Allowed to delete Admin with id as 1.
# 		if user['id'] == _id:
# 			#: delete the user from database list.
# 			data['users'].remove(user)

# 	#: write altered back to the file.
# 	write_json_to_file(data, file)


'''
	For add user functionality
'''


def add_user(username, password):
    #: read the data
    db = get_db()
    error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
    ).fetchone() is not None:
        error = 'User {} is already registered.'.format(username)

    if error is None:
        db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (username, password)
        )
        db.commit()
    else:
        flash(error, 'danger')


# def display_user_list(list):

# 	if list == [] :
# 		#: if nothing found in list.
# 		print('''
# 			Sorry :( No record match found...
# 			''')
# 	else:
# 		#: for item in list display all information.
# 		for item in list:
# 			print('''
# 				id : {}
# 				Username : {}
# 				Password : {}
# 			'''.format(item['id'], item['username'], item['password']), end='\n')


def login_authenticator(username='', password=''):
    #: flag for login
    login_flag = False

    #: get database for the query
    db = get_db()
    error = None

    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username, )
    ).fetchone()

    if user is None:
        error = 'Invalid Username.'
    elif user['id'] == 1:
        if user['password'] != password:
            error = 'Invalid Password.'
    elif not check_password_hash(user['password'], password):
        error = 'Invalid Password.'

    if error is None:
        login_flag = True
        print('login success.')
    else:
        login_flag = False
        flash(error, 'danger')

    return login_flag

    # for user in data['users']:

    # 	if user['username'] == username and user['username'] != 'admin':
    # 		if check_password_hash(user['password'], password):
    # 			print('login success.')
    # 			login_flag = True
    # 			break
    # 	else:
    # 		if user['username'] == username:
    # 			if user['password'] == password:
    # 				print('login success.')
    # 				login_flag = True
    # 				break

    # return login_flag

#: Here we have summarize all the methds with ther uses as they are represented.
#: These are the methods which can be exported to or imported into data.py for database use.


def main():
    # training()

    #: dummy user data to create new user
    username = 'user'
    password = 'password'

    #: Add user to user data target file.
    add_user(username, password)

    #: To delete particular user except for admin which has id = 1
    #: delete_user(target, _id=2)

    #: Display all fetched data.
    # display_user_list(user_list1)

    if login_authenticator(username='user', password='password'):
        print('Success')
    else:
        print('Fail')


# main()
