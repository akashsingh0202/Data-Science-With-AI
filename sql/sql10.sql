CREATE DATABASE join_practice1;

USE join_practice;

CREATE TABLE employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT
);

INSERT INTO employee (employee_id, employee_name, department_id)
VALUES
(1, 'Akash', 101),
(2, 'Rahul', 102),
(3, 'Aman', 103),
(4, 'Rohit', 104),
(5, 'Vikas', 105),
(6, 'Suresh', 101),
(7, 'Karan', 102),
(8, 'Arjun', 103),
(9, 'Ravi', 104),
(10, 'Deepak', 105),

(11, 'Ankit', 101),
(12, 'Mohit', 102),
(13, 'Sumit', 103),
(14, 'Nikhil', 104),
(15, 'Raj', 105),
(16, 'Manish', 101),
(17, 'Pankaj', 102),
(18, 'Abhishek', 103),
(19, 'Sachin', 104),
(20, 'Vijay', 105),

(21, 'Amit', 101),
(22, 'Rakesh', 102),
(23, 'Sanjay', 103),
(24, 'Ajay', 104),
(25, 'Neeraj', 105),
(26, 'Gaurav', 101),
(27, 'Shivam', 102),
(28, 'Harsh', 103),
(29, 'Tarun', 104),
(30, 'Varun', 105),

(31, 'Ashish', 101),
(32, 'Yash', 102),
(33, 'Kunal', 103),
(34, 'Aditya', 104),
(35, 'Prince', 105),
(36, 'Ramesh', 101),
(37, 'Dinesh', 102),
(38, 'Lokesh', 103),
(39, 'Mukesh', 104),
(40, 'Naresh', 105),

(41, 'Kartik', 101),
(42, 'Rajat', 102),
(43, 'Dev', 103),
(44, 'Naveen', 104),
(45, 'Vishal', 105),

(46, 'Unknown1', NULL),
(47, 'Unknown2', NULL),
(48, 'Unknown3', NULL),
(49, 'Unknown4', NULL),
(50, 'Unknown5', NULL);

SELECT * FROM employees;

CREATE TABLE department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO department (department_id, department_name, location)
VALUES
(101, 'IT', 'Hyderabad'),
(102, 'HR', 'Mumbai'),
(103, 'Finance', 'Delhi'),
(104, 'Marketing', 'Bangalore'),
(105, 'Sales', 'Pune'),
(106, 'Support', 'Chennai'),
(107, 'Research', 'Hyderabad'),
(108, 'Testing', 'Noida'),
(109, 'Security', 'Mumbai'),
(110, 'Management', 'Delhi');

SELECT * FROM department;

select
 e.employee_id,
 e.employee_name,
 e.department_id,
 d.department_name,
 d.location
from employee e
inner join department d
on e.department_id=d.department_id
order by employee_id;


-- left join
select
 e.employee_id,
 e.employee_name,
 e.department_id,
 d.department_name,
 d.location
from employee e
left join department d
on e.department_id=d.department_id
order by employee_id;


select
 e.employee_id,
 e.employee_name,
 e.department_id,
 d.department_name,
 d.location
from employee e
right join department d
on e.department_id=d.department_id
order by employee_id;





