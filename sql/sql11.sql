CREATE DATABASE subquery_practice;
USE subquery_practice;

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
(105, 'Marketing', 'Bangalore');

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    salary INT,
    age INT,
    city VARCHAR(50),
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

INSERT INTO employees VALUES
(1, 'Akash', 101, 60000, 24, 'Hyderabad'),
(2, 'Rahul', 101, 75000, 27, 'Hyderabad'),
(3, 'Priya', 102, 50000, 25, 'Delhi'),
(4, 'Rohit', 103, 90000, 30, 'Mumbai'),
(5, 'Neha', 103, 85000, 28, 'Mumbai'),
(6, 'Amit', 104, 45000, 23, 'Pune'),
(7, 'Pooja', 104, 55000, 26, 'Pune'),
(8, 'Karan', 105, 70000, 29, 'Bangalore'),
(9, 'Anjali', 101, 65000, 25, 'Hyderabad'),
(10, 'Vikas', 103, 95000, 32, 'Mumbai'),
(11, 'Sahil', 102, 48000, 24, 'Delhi'),
(12, 'Manish', 105, 80000, 31, 'Bangalore');


CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    department_id INT,
    budget INT
);

INSERT INTO projects VALUES
(201, 'E-Commerce', 101, 500000),
(202, 'Banking App', 101, 800000),
(203, 'Recruitment', 102, 300000),
(204, 'Audit System', 103, 600000),
(205, 'Sales Portal', 104, 400000),
(206, 'Marketing App', 105, 450000);

SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

select * 
from employees 
where salary =
(select max(salary) 
from employees 
);
select * 
from employees 
where salary=(select min(salary)
from employees);

select *
from employees
where department_id in (
     select department_id
     from departments 
     where department_name in('IT','Finance')
);

select * from employees 
where department_id not in (select department_id 
from departments where department_name='IT');

SELECT *
FROM (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
) AS dept_avg
WHERE avg_salary > 60000;

SELECT
    employee_name,
    salary,
    (SELECT AVG(salary) FROM employees) AS avg_salary
FROM employees;

SELECT *
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE department_id = 102
);

SELECT *
FROM employees
WHERE salary > ALL (
    SELECT salary
    FROM employees
    WHERE department_id = 102
);

SELECT *
FROM departments d
WHERE EXISTS (
    SELECT *
    FROM employees e
    WHERE e.department_id = d.department_id
);


SELECT *
FROM departments d
WHERE NOT EXISTS (
    SELECT *
    FROM employees e
    WHERE e.department_id = d.department_id
);

SELECT
    e.employee_name,
    e.salary,
    e.department_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);



SELECT *
FROM employees
WHERE department_id = (
    SELECT department_id
    FROM (
        SELECT department_id, AVG(salary) AS avg_salary
        FROM employees
        GROUP BY department_id
    ) AS x
    WHERE avg_salary = (
        SELECT MAX(avg_salary)
        FROM (
            SELECT department_id, AVG(salary) AS avg_salary
            FROM employees
            GROUP BY department_id
        ) AS y
    )
);


SELECT
    department_id,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM employees
);

UPDATE employees
SET salary = salary * 1.10
WHERE department_id = (
    SELECT department_id
    FROM departments
    WHERE department_name = 'IT'
);

DELETE FROM employees
WHERE department_id = (
    SELECT department_id
    FROM departments
    WHERE department_name = 'IT'
);


SELECT e.*
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_name = 'IT';




select * from employees
where salary =(select max(salary)
from employees );


select * from employees
where salary >(select avg(salary)
from employees );

select * from employees where department_id in (select 
department_id 
from departments
where department_name in ('IT','Finance'));


select *
from employees 
where department_id not in(
select department_id 
from departments
where department_name ='HR' );

select * from employees
where salary > any(select salary
from employees
where department_id = 102
);



