#: Importing all dependencies.
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

#: from importing all neccessary mthods for user actions and login
from .data import (
    list_student_data, add_student_data, update_student,
    delete_student_data, search_student_record
)
#: import student related forms
from .form import CreateStudentForm, UpdateStudentForm

#: import login required to check for user login
from student_db.auth import login_required

#: import for the databases
from student_db.student_db import get_db

#: exceptions to add abort to our functionality.
#: In case of  http request-response error send abort.
from werkzeug.exceptions import abort

'''
Created By: Ajay
Date: Febuary 12, 2019
'''
'''
This module is the main module for the Student Application.
It will provide all the vew functionalities to our app
which deals with student processes like.
1. Add Student record to database. (Create)
2. Edit particular student record. (Update)
3. Delete a particular student. (Delete)
4. Search or view all or few students. (Read)
This contain all the views related to the functinality of the student.
'''

#: blueprint for the student app with url prefix of '/student'
bp = Blueprint('student', __name__, url_prefix='/')

#: Below will contain all the views related to the student data processing.
@bp.route('/')
@login_required
def index():
    #: fetch the list of students from database.
    students = list_student_data()
    return render_template(
        'student/index.html',
        title='Index',
        students=students)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    form = CreateStudentForm()
    if form.validate_on_submit():

        #: perform add student
        add_student_data(
            name=form.name.data,
            age=form.age.data,
            gender=form.gender.data)
        #: flash message if successful
        flash(f'Student {form.name.data} added successfully.', 'success')

        return redirect(url_for('student.index'))
    return render_template(
        'student/create.html',
        title='Add Student',
        form=form)


#: get the student for particular roll number
def get_students(id):
    student = []
    students = list_student_data()
    for item in students:
        if item['id'] == id:
            student.append(item)

    student = student[0]

    if student is None:
        abort(404, "Student {0} doesn't exist.".format(roll_number))

    return student


#: update for the student
@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    student = get_students(id)
    form = UpdateStudentForm()

    if form.validate_on_submit():

        #: perform update for student details
        update_student(
            name=form.name.data,
            age=form.age.data,
            gender=form.gender.data,
            id=id)

        #: flash message if updated
        flash(
            f'Student {form.name.data} details updated successfully.',
            'success')

        return redirect(url_for('student.index'))
    return render_template(
        'student/update.html',
        title='Edit Student',
        form=form,
        student=student)


@bp.route('/delete/<int:id>', methods=('POST',))
@login_required
def delete(id):
    student = get_students(id)

    #: perform delete
    delete_student_data(id=id)

    flash(f'Student removed successfully.', 'success')

    return redirect(url_for('student.index'))


@bp.route('/search', methods=('GET', 'POST'))
@login_required
def search():
    students = []

    if request.method == 'GET':
        pattern = request.args.get('search')
        print(pattern)
        error = None

        if not pattern:
            error = 'Search field cannot be empty.'

        if error is not None:
            flash(error, 'warning')
        else:
            pattern = request.args.get('search')
            #: perform search
            students = search_student_record(pattern)
            return render_template('student/index.html', students=students)

    return render_template('student/index.html', students=students)
#: end of module
