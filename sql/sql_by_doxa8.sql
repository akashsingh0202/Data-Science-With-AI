create database doxa3;
use doxa3;
CREATE TABLE self_join_employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    job_role VARCHAR(50),
    manager_id INT,
    salary INT
);

INSERT INTO self_join_employees VALUES
(1, 'Akash', 'CEO', NULL, 100000),
(2, 'Rahul', 'Manager', 1, 80000),
(3, 'Amit', 'Manager', 1, 75000),
(4, 'Priya', 'Developer', 2, 60000),
(5, 'Neha', 'Developer', 2, 55000),
(6, 'Rohit', 'Tester', 2, 50000),
(7, 'Sneha', 'Developer', 3, 58000),
(8, 'Vikas', 'Tester', 3, 52000),
(9, 'Pooja', 'HR Executive', 3, 48000),
(10, 'Karan', 'Intern', 4, 30000);

select * from self_join_employees;
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager,
    e.salary as employee_salary,
    m.salary as manager_salary
FROM self_join_employees e
JOIN self_join_employees m
    ON e.manager_id = m.employee_id;
    
-- cross join