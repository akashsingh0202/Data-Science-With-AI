create database set_;
use set_;
CREATE TABLE students_a (
    student_id INT,
    student_name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO students_a VALUES
(1, 'Akash', 'Rewa'),
(2, 'Rahul', 'Bhopal'),
(3, 'Priya', 'Indore'),
(4, 'Rohit', 'Delhi'),
(5, 'Neha', 'Pune'),
(6, 'Amit', 'Mumbai'),
(7, 'Pooja', 'Jaipur'),
(8, 'Karan', 'Rewa');

CREATE TABLE students_b (
    student_id INT,
    student_name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO students_b VALUES
(3, 'Priya', 'Indore'),
(4, 'Rohit', 'Delhi'),
(5, 'Neha', 'Pune'),
(9, 'Vikas', 'Chennai'),
(10, 'Anjali', 'Kolkata'),
(11, 'Sahil', 'Mumbai'),
(12, 'Manish', 'Delhi'),
(13, 'Karan', 'Rewa');

select * from students_a;
select * from students_b;


select student_name ,city
from students_a
union
select student_name ,city
from students_b;


select student_name ,city
from students_a
union all
select student_name ,city
from students_b;


SELECT student_name
FROM students_a

INTERSECT

SELECT student_name
FROM students_b;


SELECT student_name
FROM students_a

except

SELECT student_name
FROM students_b;


