CREATE DATABASE groupby_having_practice;

USE groupby_having_practice;

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    department VARCHAR(30),
    city VARCHAR(30),
    salary INT
);

INSERT INTO employees (name, department, city, salary)
VALUES
('Akash', 'IT', 'Hyderabad', 50000),
('Aman', 'IT', 'Hyderabad', 60000),
('Ravi', 'IT', 'Mumbai', 55000),
('Sneha', 'IT', 'Hyderabad', 65000),
('Karan', 'IT', 'Delhi', 70000),

('Rahul', 'HR', 'Mumbai', 40000),
('Neha', 'HR', 'Delhi', 45000),
('Vikas', 'HR', 'Delhi', 42000),
('Anjali', 'HR', 'Mumbai', 48000),

('Priya', 'Sales', 'Delhi', 35000),
('Rohit', 'Sales', 'Mumbai', 38000),
('Pooja', 'Sales', 'Hyderabad', 36000);


SELECT * FROM employees;



select department , count(*) as total_employee
from employees 
group by department
having count(*)>=4;

select department, avg(salary) as avg_salary
from employees 
group by department
having avg(salary)>=50000;

select department,city,count(*) as total_employees
from employees 
group by city,department
having count(*)>=2;

