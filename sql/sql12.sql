create database views;
use views;
CREATE TABLE employees_view (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary INT,
    department VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO employees_view VALUES
(1, 'Akash', 60000, 'IT', 'Hyderabad'),
(2, 'Rahul', 75000, 'IT', 'Hyderabad'),
(3, 'Priya', 50000, 'HR', 'Delhi'),
(4, 'Rohit', 90000, 'Finance', 'Mumbai'),
(5, 'Neha', 85000, 'Finance', 'Mumbai'),
(6, 'Amit', 45000, 'Sales', 'Pune'),
(7, 'Pooja', 55000, 'Sales', 'Pune'),
(8, 'Karan', 70000, 'Marketing', 'Bangalore'),
(9, 'Anjali', 65000, 'IT', 'Hyderabad'),
(10, 'Vikas', 95000, 'Finance', 'Mumbai');

SELECT *
FROM employees_view;


CREATE VIEW it_employees AS
SELECT *
FROM employees_view
WHERE department = 'IT';

SELECT *
FROM it_employees;

create view high_salary_view AS
select * from employees_view 
where salary>70000;

SELECT *
FROM high_salary_view;

create view it_employee_view AS
select * from 
employees_view 
where department='IT';
select * from it_employee_view;



create view employee_view as 
select * from employees_view
where salary >60000;
select employee_name,
salary,
department
from employee_view;


create view mumbai_employees as 
select * from employees_view
where city='Mumbai';
select employee_name,
salary,
department from mumbai_employees;

create view high_salary_employees as
select * from employees_view
where salary >= 75000
order by salary desc;
select employee_name,
salary,
city from high_salary_employees; 


create or replace view high_salary_employees as
select * from employees_view
where salary >=80000;

SELECT employee_name, salary, department
FROM high_salary_employees;

DROP VIEW high_salary_employees;


SELECT * FROM high_salary_employees;

CREATE VIEW department_salary AS
SELECT
    department,
    COUNT(*) AS total_employees,
    AVG(salary) AS average_salary,
    MAX(salary) AS highest_salary
FROM employees_view
GROUP BY department;


CREATE TABLE employee_view_practice (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    city VARCHAR(50)
);

INSERT INTO employee_view_practice VALUES
(1, 'Akash', 'IT', 60000, 'Hyderabad'),
(2, 'Rahul', 'IT', 75000, 'Hyderabad'),
(3, 'Anjali', 'IT', 65000, 'Hyderabad'),

(4, 'Priya', 'HR', 50000, 'Delhi'),
(5, 'Sahil', 'HR', 48000, 'Delhi'),

(6, 'Rohit', 'Finance', 90000, 'Mumbai'),
(7, 'Neha', 'Finance', 85000, 'Mumbai'),
(8, 'Vikas', 'Finance', 95000, 'Mumbai'),

(9, 'Amit', 'Sales', 45000, 'Pune'),
(10, 'Pooja', 'Sales', 55000, 'Pune'),

(11, 'Karan', 'Marketing', 70000, 'Bangalore'),
(12, 'Manish', 'Marketing', 80000, 'Bangalore');

RENAME TABLE employee_view_practice
TO departments_view;
rollback;

CREATE TABLE departments_views(
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO departments_views VALUES
(101, 'IT', 'Hyderabad'),
(102, 'HR', 'Delhi'),
(103, 'Finance', 'Mumbai'),
(104, 'Sales', 'Pune'),
(105, 'Marketing', 'Bangalore');


CREATE VIEW employee_department_view AS
SELECT
    e.employee_name,
    e.salary,
    d.department_name,
    d.location
FROM employees_view e
JOIN departments_views d
ON e.department_id = d.department_id;


CREATE VIEW it_employeess AS
SELECT *
FROM employees_view
WHERE department = ''
WITH CHECK OPTION;

UPDATE it_employeess
SET salary = 80000
WHERE employee_id = 1;



CREATE VIEW above_average_salary AS
SELECT
    employee_name,
    salary,
    department
FROM employees_view
WHERE salary > (
    SELECT AVG(salary)
    FROM employees_view
);

SELECT *
FROM above_average_salary;



