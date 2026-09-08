CREATE DATABASE college_db;
USE college_db;

CREATE TABLE students (
    student_id INT,
    student_name VARCHAR(50),
    age INT
);

INSERT INTO students VALUES
(1, 'Akash', 22),
(2, 'Rahul', 23),
(3, 'Aman', 21);

SELECT * FROM students;

INSERT INTO students VALUES
(1, 'Rohit', 25);

DROP TABLE students;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT
);

INSERT INTO students VALUES
(1, 'Akash', 22),
(2, 'Rahul', 23),
(3, 'Aman', 21);



select * from students;


CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments (department_id, department_name)
VALUES
(101, 'Computer Science'),
(102, 'Mechanical'),
(103, 'Civil'),
(104, 'Electrical');

SELECT * FROM departments;


CREATE TABLE student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT,
    department_id INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);
DELETE FROM students;
INSERT INTO student (student_id, student_name, age, department_id)
VALUES
(1, 'Akash', 22, 101),
(2, 'Rahul', 23, 102),
(3, 'Aman', 21, 101),
(4, 'Rohit', 24, 103),
(5, 'Vikas', 22, 104);

select * from student;