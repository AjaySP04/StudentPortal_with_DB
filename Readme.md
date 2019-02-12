# Readme for Student Portal Web Application with Relational Database (SQLite)

This project is part of an in-house assignment, and also a copy of the already existing Student Portal Application with an only difference 
of the database use. This uses SQLite database for data management through an RDBMS and SQL.

# Install the dependencies for the project
1. Must install the virtualenv on Linux using 
  'pip intall virtualenv'
  
2. Open an empty folder in any directory create virtualenv (with command for linux 'virtualenv venv') likewise in windows.

3. Place the project folder into directory of your virtualenv and run venv with command as mentioned below:
  'source venv/bin/activate'
  This will activate the virtual env with the name as mentioned (like in this case venv)
  
4. Now install all the dependencies as are listed in 'requirements.txt'. You need to install Flask version=1.0.2 and WTForms version=2.2.1 from flask_wtf (use 'pip install flask && pip install flask_wtf' )
   


# To Run this app in development mode.

1. Setup the flask app and its environment
  a. Linux shell type below command
    'export FLASK_APP=student_nodb'
    'export FLASK_ENV=development' OR,
  b. Windows replace "export" with "set" for windows command will be:
    'set FLASK_APP=student_nodb'
    'set FLASK_ENV=development'
    
2. Set up database for the app Use the following command in command shell
  'flask init_db'
  
  Output:
  Initialized Student Database
  
3. Now run the flask app through command:
  'flask run'
  
  Output:
  * Serving Flask app "student_nodb" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx

You can open the mentioned url for runnig the app on your local machine.
  

# credentials for first time users of the application. 
- If you see the login page for admin user in you browser. 
Use below highly confidential credentials for this app.
  

* Username: "admin"    // best username for an application admin, I know.... :D
* Password: "password" // I understand this is a bad idea to keep password such as this. Sorry :(

- Don't worry you can add more users but once you should enter into the portal. 