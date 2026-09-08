CREATE DATABASE groupby_practice;

USE groupby_practice;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    city VARCHAR(50),
    gender VARCHAR(10),
    salary DECIMAL(10,2),
    age INT
);

INSERT INTO employees 
(employee_name, department, city, gender, salary, age)
VALUES

('Akash', 'IT', 'Hyderabad', 'Male', 50000, 22),
('Rahul', 'HR', 'Mumbai', 'Male', 40000, 25),
('Aman', 'IT', 'Hyderabad', 'Male', 60000, 28),
('Neha', 'HR', 'Delhi', 'Female', 45000, 24),
('Ravi', 'IT', 'Mumbai', 'Male', 55000, 30),
('Priya', 'Sales', 'Delhi', 'Female', 35000, 26),
('Rohit', 'Sales', 'Mumbai', 'Male', 38000, 27),
('Sneha', 'IT', 'Hyderabad', 'Female', 65000, 29),
('Vikas', 'HR', 'Delhi', 'Male', 42000, 31),
('Pooja', 'Sales', 'Hyderabad', 'Female', 36000, 23),
('Karan', 'IT', 'Delhi', 'Male', 70000, 32),
('Anjali', 'HR', 'Mumbai', 'Female', 48000, 28),
('Suresh', 'Sales', 'Delhi', 'Male', 39000, 30),
('Meena', 'IT', 'Mumbai', 'Female', 58000, 27),
('Arjun', 'HR', 'Hyderabad', 'Male', 44000, 26);

select * from employees;
select count(*)
from employees;


select department, count(*)
from employees
group by department; 

select * from employees;


select city, department,count(*) as total_employee_in_cityvise
from employees
group by city ,department; 


select city, department,sum(salary) as total_salary
from employees
group by city ,department;

select city, department,gender,count(*) as total_count
from employees
group by city ,department,gender; 
 

select city, department,gender,sum(salary) as total_salary
from employees
group by city ,department,gender; 

select * from employees;


-- tasks
select department, count(*)
from employees 
group by department;

select city, count(*)
from employees 
group by city;

select gender, count(*)
from employees 
group by gender;

select department, sum(salary)
from employees 
group by department;


select department, avg(salary)
from employees 
group by department;

select department, max(salary)
from employees 
group by department;

select department, min(salary)
from employees 
group by department;



-- group and having concept
