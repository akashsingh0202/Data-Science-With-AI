CREATE DATABASE window_practice;

USE window_practice;

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO departments VALUES
(1, 'IT', 'Hyderabad'),
(2, 'HR', 'Delhi'),
(3, 'Finance', 'Mumbai'),
(4, 'Sales', 'Pune'),
(5, 'Marketing', 'Bangalore');

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    job_role VARCHAR(50),
    salary INT,
    joining_date DATE,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


INSERT INTO employees VALUES
(101, 'Akash', 1, 'Python Developer', 60000, '2023-01-15'),
(102, 'Rahul', 1, 'Data Analyst', 75000, '2022-06-10'),
(103, 'Priya', 1, 'Senior Developer', 90000, '2021-03-20'),
(104, 'Amit', 1, 'Python Developer', 75000, '2024-02-05'),

(105, 'Neha', 2, 'HR Executive', 55000, '2022-08-12'),
(106, 'Rohit', 2, 'HR Manager', 80000, '2020-11-18'),
(107, 'Pooja', 2, 'Recruiter', 60000, '2023-07-25'),

(108, 'Vikas', 3, 'Accountant', 65000, '2021-09-14'),
(109, 'Anjali', 3, 'Finance Manager', 95000, '2019-04-22'),
(110, 'Sahil', 3, 'Financial Analyst', 75000, '2022-12-01'),

(111, 'Karan', 4, 'Sales Executive', 50000, '2024-01-10'),
(112, 'Manish', 4, 'Sales Manager', 85000, '2020-05-16'),
(113, 'Simran', 4, 'Sales Executive', 50000, '2023-10-08'),

(114, 'Deepak', 5, 'Marketing Executive', 58000, '2022-02-17'),
(115, 'Kavita', 5, 'Marketing Manager', 88000, '2020-07-30'),
(116, 'Arjun', 5, 'SEO Specialist', 70000, '2023-05-11');

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    sale_date DATE,
    amount INT,
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
);

INSERT INTO sales VALUES
(1, 101, '2026-01-05', 12000),
(2, 102, '2026-01-07', 18000),
(3, 103, '2026-01-10', 25000),
(4, 104, '2026-01-12', 15000),
(5, 101, '2026-01-15', 22000),
(6, 102, '2026-01-18', 20000),
(7, 103, '2026-01-20', 30000),
(8, 104, '2026-01-22', 17000),
(9, 101, '2026-02-02', 14000),
(10, 102, '2026-02-05', 24000),
(11, 103, '2026-02-08', 28000),
(12, 104, '2026-02-10', 19000),
(13, 105, '2026-02-12', 11000),
(14, 106, '2026-02-15', 21000),
(15, 107, '2026-02-18', 16000),
(16, 108, '2026-02-20', 23000),
(17, 109, '2026-02-22', 32000),
(18, 110, '2026-02-25', 27000),
(19, 111, '2026-03-01', 13000),
(20, 112, '2026-03-03', 26000);





-- 





-- window function

select * from 
employees;

select employee_id , salary ,sum(salary) over() as sum_salary
from employees;

SELECT
    employee_name,
    salary,
    AVG(salary) OVER() AS average_salary
FROM employees;

SELECT
    employee_name,
    salary,
    COUNT(*) OVER() AS total_employees
FROM employees;

SELECT
    employee_name,
    salary,
    MIN(salary) OVER() AS minimum_salary,
    MAX(salary) OVER() AS maximum_salary
FROM employees;

select employee_name , 
salary, 
max(salary)  over() as max_salary  , 
min(salary)over() as min_salary
from employees;

select employee_name , 
salary, 
sum(salary)  over() as sum_salary  , 
avg(salary)over() as avg_salary
from employees;

-- partition By
select employee_name, department_id,
salary,
avg(salary) over(partition by department_id) as avg_salary
from employees;

select employee_name, department_id,
salary,
sum(salary) over(partition by department_id) as sum_salary
from employees;

select employee_name, department_id,
salary,
count(*) over(partition by department_id) as count_employee
from employees;

select employee_name, department_id,
salary,
max(salary) over(partition by department_id) as max_salary
from employees;

select employee_name, department_id,
salary,
min(salary) over(partition by department_id) as min_salary;


select employee_name , department_id , salary,
max(salary) over(partition by department_id) as maximum_salary
from employees;

-- order by
select employee_name , department_id , salary,
avg(salary) over(partition by department_id 
order by salary desc) as avg_salary
from employees;


-- row number
SELECT
    employee_name,
    salary,
    ROW_NUMBER() OVER(
        ORDER BY salary DESC
    ) AS row_num
FROM employees;

select employee_name ,
department_id,
salary,
row_number() over( partition by department_id order by salary) as count_dept
from employees;

-- rank()
SELECT
    employee_name,
    salary,
    RANK() OVER(
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;

select employee_name ,
department_id,
salary,
rank() over(partition by department_id order by salary desc) as ranked
from employees ;


-- dense Rank()
SELECT
    employee_name,
    department_id,
    salary,
    DENSE_RANK() OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;


select employee_name,
department_id ,
salary,
dense_rank() over(partition by department_id order by salary desc)
from employees;

-- ntile()
SELECT
    employee_name,
    salary,
    NTILE(4) OVER(
        ORDER BY salary DESC
    ) AS salary_group
FROM employees;

SELECT
    employee_name,
    department_id,
    salary,
    NTILE(2) OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS salary_group
FROM employees;


select employee_name ,
salary,
ntile(4) over(order by salary desc) as grooup_salary
from employees;

























