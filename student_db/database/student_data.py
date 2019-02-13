import os
import sys

#: re for regex functinality.
#: used in search.
import re

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


# def display_student_list(list):

# 	if list == [] :
# 		#: if nothing found in list.
# 		print('''
# 			Sorry :( No record match found...
# 			''')
# 	else:
# 		#: for item in list display all information.
# 		for item in list:
# 			print('''
# 				Name : {}
# 				Roll Number : {}
# 				Age : {}
# 				Gender : {}
# 			'''.format(item['name'], item['roll_number'], item['age'], item['gender']), end='\n')


#: Here we have summarize all the methods with ther uses as they are represented.
#: These are the methods which can be exported to or imported into data.py for database use.
def main():
    # training()

    file = FILE_STUDENTS
    # training_file(file)
    target = 'temp/new_student_temp_data.txt'

    #: try to load data to target
    load_data_student(file, target)

    #: list all Students for index page
    #student_list = list_data_student(target)
    # display_student_list(student_list)

    #: dummy user data to create new user
    name = 'test student'
    age = 19
    gender = 'Male'
    #: Add user to user data target file.
    #add_data_student(target, name, age, gender)

    #: update/edit student information
    #update_student_detail(target, roll_number='S00001')

    #: To delete particular student with specified roll number
    #delete_student(target, roll_number='S00001')

    #: search for student with roll number or name
    #: this will return list of all match for search pattern.
    list_of_search = search_student(target, search_string='Stu')

    #: Display all fetched data.
    display_student_list(list_of_search)


# if __name__=='__main__':
# 	main()
