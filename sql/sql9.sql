CREATE DATABASE join_practice;

USE join_practice;

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments VALUES
(101, 'Computer Science'),
(102, 'Mechanical'),
(103, 'Civil'),
(104, 'Electrical'),
(105, 'Artificial Intelligence');

SELECT * FROM departments;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT,
    department_id INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

INSERT INTO students VALUES
(1, 'Akash', 22, 101),
(2, 'Rahul', 23, 102),
(3, 'Aman', 21, 101),
(4, 'Rohit', 24, 103),
(5, 'Vikas', 22, 104);

SELECT * FROM students;


SELECT *
FROM students
JOIN departments
ON students.department_id = departments.department_id;
