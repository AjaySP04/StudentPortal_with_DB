'''
    This module needs to be registered to the initial app to use this database.
'''

import sqlite3

import click

'''
    importing neccessary objects for database these special objects are:
    current_app = this handles the flask related requests
    g - speacial object which is unique to each request 
'''
from flask import current_app, g


from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# close database when not required.
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# initialze the database 
def init_db():
    db = get_db()

    # open a file for data 
    with current_app.open_resource('db_schema.sql') as file:
        '''
            read databsse as file data.
        '''
        db.executescript(file.read().decode('utf8'))


'''
    here we are adding command into flask for initializing app database.
'''
@click.command('init_db')
@with_appcontext
def init_db_command():
    ''' clear the existing data and make fresh tables using the command.'''
    init_db()
    click.echo('Initialized Student Database')

def init_app(app):
    app.teardown_appcontext(close_db) # makes flask to call function while clean up 
    app.cli.add_command(init_db_command) # add the command into flask <command>
