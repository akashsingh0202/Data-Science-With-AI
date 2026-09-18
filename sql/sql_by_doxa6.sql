create database doxa2;
use doxa2;
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT
);
INSERT INTO employees (employee_id, employee_name, department_id)
VALUES
(1, 'Akash', 101),
(2, 'Rahul', 102),
(3, 'Priya', 103),
(4, 'Rohan', 101),
(5, 'Sneha', 102),
(6, 'Amit', 104),
(7, 'Neha', NULL),
(8, 'Vikas', 103),
(9, 'Pooja', 101),
(10, 'Arjun', 105);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO departments (department_id, department_name, location)
VALUES
(101, 'IT', 'Hyderabad'),
(102, 'HR', 'Mumbai'),
(103, 'Finance', 'Delhi'),
(104, 'Marketing', 'Bangalore'),
(106, 'Sales', 'Pune'),
(107, 'Support', 'Chennai');

select * from departments;
select * from employees;


-- inner join
select 
	e.employee_id,
	e.employee_name,
    d.department_name,
    d.location,
    d.department_id
from employees as e
inner join departments as d
on e.department_id=d.department_id;
-- left join
select 
	e.employee_id,
	e.employee_name,
    d.department_name,
    d.location,
    d.department_id
from employees as e
left join departments as d
on e.department_id=d.department_id;

-- right join
select 
	e.employee_id,
	e.employee_name,
    d.department_name,
    d.location,
    d.department_id
from employees as e
right join departments as d
on e.department_id=d.department_id;

-- cross join
SELECT
    e.employee_name,
    d.department_name
FROM employees e
CROSS JOIN departments d;


-- union 

SELECT
    e.employee_id,
    e.employee_name,
    e.department_id,
    d.department_name,
    d.location
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id

UNION

SELECT
    e.employee_id,
    e.employee_name,
    d.department_id,
    d.department_name,
    d.location
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;

-- natural join
SELECT *
FROM employees
NATURAL JOIN departments;

