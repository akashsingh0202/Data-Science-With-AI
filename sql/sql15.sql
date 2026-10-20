create database window_func;
use window_func;

CREATE TABLE window_employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    joining_date DATE
);
INSERT INTO window_employees VALUES
(1, 'Akash', 'IT', 80000, '2022-01-15'),
(2, 'Rahul', 'IT', 60000, '2023-03-10'),
(3, 'Priya', 'IT', 70000, '2021-07-20'),

(4, 'Rohit', 'Finance', 90000, '2020-05-12'),
(5, 'Neha', 'Finance', 70000, '2022-08-18'),
(6, 'Amit', 'Finance', 90000, '2021-11-25'),

(7, 'Pooja', 'HR', 65000, '2023-01-05'),
(8, 'Karan', 'HR', 55000, '2022-06-15'),
(9, 'Sneha', 'HR', 75000, '2020-09-30'),

(10, 'Vikas', 'Sales', 60000, '2021-04-22'),
(11, 'Anjali', 'Sales', 80000, '2022-02-14'),
(12, 'Sahil', 'Sales', 70000, '2023-05-19');

SELECT *
FROM window_employees;

-- over()
SELECT
    employee_name,
    department,
    salary,
    AVG(salary) OVER() AS avg_salary
FROM window_employees;

SELECT
    employee_name,
    salary,
    MAX(salary) OVER() AS max_salary
FROM window_employees;


-- partition by
SELECT
    employee_name,
    department,
    salary,
    AVG(salary) OVER(PARTITION BY department) AS dept_avg_salary
FROM window_employees;

-- order by
SELECT
    employee_name,
    salary,
    SUM(salary) OVER(
        ORDER BY salary desc
    ) AS running_salary
FROM window_employees;


-- row_number()
SELECT
    employee_name,
    department,
    salary,
    ROW_NUMBER() OVER(
        ORDER BY salary DESC
    ) AS row_num
FROM window_employees;

SELECT
    employee_name,
    department,
    salary,
    ROW_NUMBER() OVER(
        PARTITION BY department
        ORDER BY salary DESC
    ) AS row_num
FROM window_employees;


-- RANK()
SELECT
    employee_name,
    salary,
    RANK() OVER(
        ORDER BY salary DESC
    ) AS salary_rank
FROM window_employees;

SELECT
    employee_name,
    department,
    salary,
    RANK() OVER(
        PARTITION BY department
        ORDER BY salary DESC
    ) AS salary_rank
FROM window_employees;


-- dense_rank()
SELECT
    employee_name,
    salary,
    DENSE_RANK() OVER(
        ORDER BY salary DESC
    ) AS salary_rank
FROM window_employees;

SELECT
    employee_name,
    department,
    salary,
    DENSE_RANK() OVER(
    partition by department
        ORDER BY salary DESC
    ) AS salary_rank
FROM window_employees;

-- ROW_NUMBER() vs RANK() vs DENSE_RANK()
SELECT
    employee_name,
    salary,

    ROW_NUMBER() OVER(
        ORDER BY salary DESC
    ) AS row_num,

    RANK() OVER(
        ORDER BY salary DESC
    ) AS rank_num,

    DENSE_RANK() OVER(
        ORDER BY salary DESC
    ) AS dense_rank_num

FROM window_employees;


-- sum()
SELECT SUM(salary) AS total_salary
FROM window_employees;
SELECT
    employee_name,
    salary,
    SUM(salary) OVER() AS total_salary
FROM window_employees;

SELECT
    employee_name,
    department,
    salary,
    SUM(salary) OVER(
        PARTITION BY department
    ) AS dept_total_salary
FROM window_employees;
SELECT
    employee_name,
    salary,
    SUM(salary) OVER(
        ORDER BY employee_id
    ) AS running_total
FROM window_employees;


-- avg() over()
SELECT
    employee_name,
    salary,
    AVG(salary) OVER() AS avg_salary
FROM window_employees;

SELECT
    employee_name,
    salary,
    AVG(salary) OVER(partition by department
    order  by employee_id) AS avg_salary
FROM window_employees;

SELECT
    employee_name,
    department,
    salary,
    avg(salary) OVER(
        PARTITION BY department
        ORDER BY employee_id
    ) AS dept_running_total
FROM window_employees;

WITH employee_data AS (
    SELECT
        employee_name,
        department,
        salary,
        AVG(salary) OVER(
            PARTITION BY department
        ) AS dept_avg_salary
    FROM window_employees
)
SELECT *
FROM employee_data
WHERE salary > dept_avg_salary;


-- max() over
SELECT
    employee_name,
    salary,
    MAX(salary) OVER() AS highest_salary
FROM window_employees;

SELECT
    employee_name,
    department,
    salary,
    MAX(salary) OVER(
        PARTITION BY department
    ) AS dept_max_salary
FROM window_employees;

-- min over()
SELECT
    employee_name,
    salary,
    MIN(salary) OVER() AS lowest_salary
FROM window_employees;
SELECT
    employee_name,
    department,
    salary,
    MIN(salary) OVER(
        PARTITION BY department
    ) AS dept_min_salary
FROM window_employees;

-- MIN() + MAX()
SELECT
    employee_name,
    department,
    salary,

    MIN(salary) OVER(
        PARTITION BY department
    ) AS min_dept_salary,

    MAX(salary) OVER(
        PARTITION BY department
    ) AS max_dept_salary

FROM window_employees;
-- Running Total
SELECT
    employee_id,
    employee_name,
    salary,
    SUM(salary) OVER(
        ORDER BY employee_id
    ) AS running_total
FROM window_employees;

SELECT
    employee_id,
    employee_name,
    department,
    salary,
    SUM(salary) OVER(
        PARTITION BY department
        ORDER BY employee_id
    ) AS dept_running_total
FROM window_employees;


-- Ranking Problems
select 
employee_id ,
employee_name,
salary,
department,
rank() over(order by salary desc ) as salary_rank
from window_employees;

select 
employee_id ,
employee_name,
salary,
department,
rank() over(partition by department
order by salary desc ) as salary_rank


from window_employees;


WITH ranked_employees AS (
    SELECT
        employee_name,
        salary,
        DENSE_RANK() OVER(
            ORDER BY salary DESC
        ) AS salary_rank
    FROM window_employees
)
SELECT
    employee_name,
    salary
FROM ranked_employees
WHERE salary_rank = 2;

WITH ranked_employees AS (
    SELECT
        employee_name,
        salary,
        DENSE_RANK() OVER(
            ORDER BY salary DESC
        ) AS salary_rank
    FROM window_employees
)
SELECT *
FROM ranked_employees
WHERE salary_rank <= 3;


-- window +cte
WITH ranked_employees AS (
    SELECT
        employee_name,
        department,
        salary,
        DENSE_RANK() OVER(
            ORDER BY salary DESC
        ) AS salary_rank
    FROM window_employees
)
SELECT *
FROM ranked_employees
WHERE salary_rank = 1;

WITH ranked_employees AS (
    SELECT
        employee_name,
        department,
        salary,
        DENSE_RANK() OVER(
            PARTITION BY department
            ORDER BY salary DESC
        ) AS dept_rank
    FROM window_employees
)
SELECT
    employee_name,
    department,
    salary
FROM ranked_employees
WHERE dept_rank = 1;

-- cte+running total
WITH salary_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        SUM(salary) OVER(
            ORDER BY employee_id
        ) AS running_total
    FROM window_employees
)
SELECT *
FROM salary_data
WHERE running_total > 500000;

-- CTE + Average Window
WITH employee_data AS (
    SELECT
        employee_name,
        department,
        salary,
        AVG(salary) OVER(
            PARTITION BY department
        ) AS dept_avg_salary
    FROM window_employees
)
SELECT *
FROM employee_data
WHERE salary > dept_avg_salary;



















