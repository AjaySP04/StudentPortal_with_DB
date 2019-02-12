DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS student;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE student (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age TEXT NOT NULL,
  gender CHAR(6) NOT NULL,
  add_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO user (username, password) VALUES ('admin', 'password');

INSERT INTO student (name, age, gender) VALUES ( 'Test Student 1', 18, 'Male');