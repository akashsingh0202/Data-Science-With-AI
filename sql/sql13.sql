create database mp1;
use mp1;
CREATE TABLE project_employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    salary INT,
    city VARCHAR(50)
);

INSERT INTO project_employees VALUES
(1, 'Akash', 101, 60000, 'Hyderabad'),
(2, 'Rahul', 101, 75000, 'Hyderabad'),
(3, 'Anjali', 101, 65000, 'Hyderabad'),
(4, 'Priya', 102, 50000, 'Delhi'),
(5, 'Sahil', 102, 48000, 'Delhi'),
(6, 'Rohit', 103, 90000, 'Mumbai'),
(7, 'Neha', 103, 85000, 'Mumbai'),
(8, 'Vikas', 103, 95000, 'Mumbai'),
(9, 'Amit', 104, 45000, 'Pune'),
(10, 'Pooja', 104, 55000, 'Pune'),
(11, 'Karan', 105, 70000, 'Bangalore'),
(12, 'Manish', 105, 80000, 'Bangalore');

CREATE TABLE project_departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO project_departments VALUES
(101, 'IT', 'Hyderabad'),
(102, 'HR', 'Delhi'),
(103, 'Finance', 'Mumbai'),
(104, 'Sales', 'Pune'),
(105, 'Marketing', 'Bangalore');



create view high_salary_employees as 
select*
from project_employees
where salary>70000;

select employee_name, salary,
city from high_salary_employees;

CREATE OR REPLACE VIEW employee_department_details AS
SELECT
    pe.employee_name,
    pe.salary,
    pd.department_name,
    pd.location
FROM project_employees AS pe
JOIN project_departments AS pd
    ON pe.department_id = pd.department_id;
    
    create view department_summary as
    select pd.department_name,
    COUNT(pe.employee_id) AS total_employees,
    avg(pe.salary) as avg_salary,
    max(pe.salary) as highest_salary
    from project_departments as pd
    join project_employees as pe
    on pd.department_id = pe.department_id
    group by department_name;
SELECT *
FROM department_summary;


create or replace view high_average_departments as
select pd.department_name ,
count(pe.employee_id)as total_employee,
 avg(pe.salary) as avg_salary
from project_departments as pd
    join project_employees as pe
    on pd.department_id = pe.department_id
    group by pd.department_name
    having avg_salary>60000;
    
    
    select * from high_average_departments;
    
    
    
    create view above_average_salary as 
    select pe.employee_name,
pe.salary,
pd.department_name,
pd.location
    from project_employees as pe
    join project_departments as pd
    on pe.department_id = pd.department_id
    where pe.salary>(select avg(salary)
    from project_employees );
    select * from above_average_salary ;

SELECT *
FROM above_average_salary;
