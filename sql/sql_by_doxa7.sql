CREATE DATABASE doxa1;
USE doxa1;

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO departments VALUES
(101, 'IT', 'Hyderabad'),
(102, 'HR', 'Delhi'),
(103, 'Finance', 'Mumbai'),
(104, 'Sales', 'Pune'),
(105, 'Marketing', 'Bangalore'),
(106, 'Operations', 'Chennai');

select * from departments;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    manager_id INT,
    salary INT
);

INSERT INTO employees VALUES
(1, 'Akash', 101, NULL, 60000),
(2, 'Rahul', 101, 1, 50000),
(3, 'Amit', 102, 1, 45000),
(4, 'Priya', 103, 3, 55000),
(5, 'Neha', 101, 1, 48000),
(6, 'Rohit', 104, 4, 52000),
(7, 'Sneha', 105, 4, 47000),
(8, 'Vikas', NULL, 2, 40000),
(9, 'Pooja', 103, 4, 58000),
(10, 'Karan', 999, 2, 42000);

select * from employees;

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    department_id INT,
    budget INT
);

INSERT INTO projects VALUES
(201, 'Banking App', 101, 500000),
(202, 'HR Portal', 102, 300000),
(203, 'Finance System', 103, 450000),
(204, 'Sales Dashboard', 104, 250000),
(205, 'Marketing Website', 105, 200000),
(206, 'AI Analytics', 101, 700000),
(207, 'Operations Tool', 106, 350000),
(208, 'New Project', 999, 150000);

select * from projects;
CREATE TABLE employee_projects (
    employee_id INT,
    project_id INT,
    hours_worked INT
);

INSERT INTO employee_projects VALUES
(1, 201, 120),
(1, 206, 100),
(2, 201, 150),
(3, 202, 130),
(4, 203, 110),
(5, 206, 140),
(6, 204, 125),
(7, 205, 100),
(9, 203, 160),
(10, 208, 90);
select * from employee_projects;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    employee_id INT
);

INSERT INTO customers VALUES
(301, 'Ramesh', 'Hyderabad', 1),
(302, 'Suresh', 'Delhi', 3),
(303, 'Anita', 'Mumbai', 4),
(304, 'Meena', 'Pune', 6),
(305, 'Raj', 'Bangalore', 7),
(306, 'Arjun', 'Hyderabad', 2),
(307, 'Kavita', 'Chennai', NULL),
(308, 'Deepak', 'Mumbai', 9);

select * from customers;


select * from departments; -- department_id pm,department_name,location
select * from employees;-- employee_id pm,employee_name,department_id,manager_id,salary
select * from projects;-- department_id ,project_id pm,project_name,budget
select * from employee_projects; -- employee_id,project_id,hours_worked
select * from customers;-- customer_id pm,customer_name,city,employee_id


-- first join

select *
from departments as d 
join employees as  e on d.department_id = e.department_id;

select *
from departments as d 
left join employees as  e on d.department_id = e.department_id;

select *
from departments as d 
right join employees as  e on d.department_id = e.department_id;

SELECT *
FROM employees e
LEFT JOIN departments d
ON d.department_id = e.department_id
UNION
SELECT *
FROM employees e
RIGHT JOIN departments d
ON d.department_id = e.department_id;


SELECT *
FROM employees e
CROSS JOIN departments d;


select * 
from departments as d 
join employees as e 
     on d.department_id = e.department_id
join projects as p
    on d.department_id = p.department_id;


select * 
from employees as e
join  employee_projects as ep
     on e.employee_id = ep.employee_id
join projects as p
    on ep.project_id = p.project_id;
select * from employees;
select * from employee_projects;
select * from projects;


select * 
from employees as e 
join customers as c 
  on e.employee_id=c.employee_id;
  select * from customers;
  
select e.employee_name
from employees as e 
left join departments as  d on e.department_id=d.department_id 
WHERE d.department_id IS NULL;

select
d.department_id,
d.department_name
from departments as d 
left join employees as  e on d.department_id=e.department_id 
WHERE e.employee_id IS NULL;

select 
d.department_name,
count(e.employee_id) as total_employee
from departments as d 
join employees as e 
 on d.department_id = e.department_id 
group by  d.department_name;

select 
d.department_name,
avg(e.salary) as total_salary
from departments as d 
join employees as e 
 on d.department_id = e.department_id 
group by  d.department_name;

select * from projects;-- department_id ,project_id pm,project_name,budget
select * from employee_projects; -- employee_id,project_id,hours_worked


select p.project_name,
sum(ep.hours_worked)as total_hours
from projects as p
join employee_projects as ep 
on p.project_id =ep.project_id
group by p.project_name ;


select * from departments; -- department_id pm,department_name,location
select * from employees;-- employee_id pm,employee_name,department_id,manager_id,salary

select e.employee_name,e.salary,d.department_name
from employees as e 
join departments as d
on e.department_id=d.department_id

order by e.salary desc
limit 1;

select*from employees;
select * from employee_projects; -- employee_id,project_id,hours_worked



select e.employee_name,
count(project_id)
from employees as e
join employee_projects as ep
on e.employee_id=ep.employee_id
group by e.employee_id 
having count(project_id)>=1
limit 1;


select c.customer_name,e.employee_name
from customers as c 
join employees as e
on c.employee_id = e.employee_id ;

select e.employee_name,c.customer_name
from employees as e
join customers as c
on e.employee_id = c.employee_id ;


select d.department_id ,
d.department_name 
from departments as d 
left join projects as p
on d.department_id=p.department_id 
where p.project_id is null;

select * from departments; -- department_id pm,department_name,location
select * from employees;-- employee_id pm,employee_name,department_id,manager_id,salary
select * from projects;-- department_id ,project_id pm,project_name,budget
select * from employee_projects; -- employee_id,project_id,hours_worked
select * from customers;-- customer_id pm,customer_name,city,employee_id


select * 
from departments as d 
join employees as  e
  on d.department_id = e.department_id
join projects as p
  on e.department_id = p.department_id 
join employee_projects as ep
 on e.employee_id=ep.employee_id
join customers as c 
 on ep.employee_id = c.employee_id;
 
 
 

