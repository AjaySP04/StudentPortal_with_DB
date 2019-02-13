import os
import sys

#: re for regex functinality.
#: used in search.
import re

# importing db into the module
from student_db.student_db import get_db

from flask import flash


#: Will get the all user_list
def list_data_student():
    #: read the data
    db = get_db()

    student_list = db.execute(
        'SELECT id, "S0000" || CAST( id AS TEXT)  AS roll_number, name, age, gender, add_date FROM student'
    ).fetchall()

    return student_list


#: Add student to the database records.
def add_data_student(name, age, gender):

    error = None
    if not name:
        error = 'Name is required.'

    if error is not None:
        flash(error)
    else:
        db = get_db()  #: read the database
        db.execute(
            'INSERT INTO student (name, age, gender) VALUES (?, ?, ?)',
            (name, age, gender)
        )
        db.commit()


#: get the specific student using the id for the student.
def get_students(id):
    student = get_db().execute(
        'SELECT id, "S0000" || CAST( id AS TEXT)  AS roll_number, name, age, gender, add_date '
        ' FROM student WHERE id=?', (id,)).fetchone()

    if student is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    return student


#: edit/update the details for the student.
def update_student_detail(name='', age=0, gender='', id=0):
        #: get the student data for specific id that need to be updated
    student = get_students(id)

    error = None

    if not name:
        error = 'Student Name is required.'

    if error is not None:
        flash(error)
    else:
        db = get_db()  #: read the database
        db.execute(
            'UPDATE student SET name = ?, age = ?, gender=? WHERE id = ?',
            (name,
             age,
             gender,
             id,
             ))
        db.commit()  #: commit the update.


#: delete the particular student using the id.
def delete_student(id=0):
    #: read the data for the student
    get_students(id)

    #: read the db with db object
    db = get_db()
    db.execute('DELETE FROM student WHERE id = ?', (id,))
    db.commit()


#: search for the pattern provided by the user in search form.
def search_student(search_string=''):
    #: list of matched student.
    #: initialized to empty list
    list_of_matched_student = []
    error = None

    pattern = '%' + search_string + '%'
    print(pattern)

    if not pattern:
        error = 'Search field cannot be empty.'

    if error is not None:
        flash(error)
    else:
        db = get_db()
        students = db.execute(
            'SELECT id, "S0000" || CAST( id AS TEXT)  AS roll_number, name, age, gender, add_date FROM student'
            ' WHERE name LIKE ?', (pattern, )).fetchall()
        list_of_matched_student = students

    return list_of_matched_student
