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

'''
created by : Ajay Singh Parmar
Date : Febuary 12, 2019
Description : Containes database functionality for user authentication.
- The methods wriiten here will be imported inside data.py in main project directory.
'''


#: For add user function, add user to database.
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


#: authenticate the user for login success or fail
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
