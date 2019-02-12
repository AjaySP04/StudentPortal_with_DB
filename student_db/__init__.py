import os

from flask import Flask

def create_app(test_config=None):
    # create and config app by creating app, an instance of Flask.
    app = Flask(__name__, instance_relative_config=True)

    # app configurations and security
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'student.sqlite'),
    )

    # for testing environment 
    if test_config is None:
       # load the config, if it exist, when not testing
       app.config.from_pyfile('config.py', silent=True)
    else:
       # load the test config if passed in
       app.config.from_mapping(test_config)

    # ensure the instance folder is created  and exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # app view for info
    @app.route('/info')
    def info():
        return 'Info Regarding the application'

    
    #: Initializing the database for our application and registering in factory.
    #  This will initialize the app data with the app currently created here.
    #: Adding the data module to the factory. which is in current directory.
    from . import student_db  # import from current directory to get register
    student_db.init_app(app)  # this will initialize the student_db with the app currently created here.


    #: registering the authentication module to the factory. which is in current directory.
    from . import auth
    app.register_blueprint(auth.bp)

    #: regitering the student module to the factory method. which is in current directory.
    from . import student
    app.register_blueprint(student.bp)

    return app