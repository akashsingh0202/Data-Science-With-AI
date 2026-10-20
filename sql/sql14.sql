use mp1;
select * from project_employees;
select* from  project_departments;



-- where 
with high_salary as (
select * from  project_employees
where salary >70000)
select * from high_salary; 

-- order by
with high_salary as (
select * from project_employees
where salary> 70000)
-- order by salary desc)
select * from high_salary
order by salary desc;

-- common alias
WITH employee_details AS (
    SELECT
        employee_id,
        employee_name AS name,
        salary AS monthly_salary,
        salary*12 as annual_salary
    FROM project_employees    
)
SELECT *
FROM employee_details;

WITH employee_details AS (
    SELECT
        employee_id,
        employee_name AS name,
        salary AS monthly_salary
    FROM project_employees
)
SELECT name, monthly_salary
FROM employee_details
WHERE monthly_salary > 70000;


-- filtering CTE
WITH employee_details AS (
    SELECT
        employee_id,
        employee_name,
        salary
    FROM project_employees
)
SELECT employee_name, salary
FROM employee_details
WHERE salary > 70000;

-- select multiple columns 
WITH employee_details AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)
SELECT employee_name, salary
FROM employee_details;


-- DIstinct
WITH employee_details AS (
    SELECT department_id
    FROM project_employees
)
SELECT DISTINCT department_id
FROM employee_details;

-- Distinct in multiple column 
WITH employee_details AS (
    SELECT employee_name, department_id
    FROM project_employees
)
SELECT DISTINCT department_id
FROM employee_details;



-- CTE + CASE
with employee_details as (
select employee_name , salary , 
CASE 
	when salary>=70000 then 'High pay'
    when salary>=60000 then 'moderate pay'
    when salary>=50000 then 'sufficient pay'
    else 'low pay'
end as Salary_category
 from project_employees
 )
  select * from employee_details;

-- limit
WITH employee_details AS (
    SELECT
        employee_name,
        salary
    FROM project_employees
)
SELECT *
FROM employee_details
ORDER BY salary DESC
LIMIT 3;

WITH employee_details AS (
    SELECT employee_name, salary
    FROM project_employees
)
SELECT *
FROM employee_details
WHERE salary > 70000
ORDER BY salary DESC
LIMIT 3;


-- join 
with employee_detail as (
select employee_id,
employee_name ,
salary,
department_id
from project_employees)
select e.employee_name , e.salary, d.department_name 
from employee_detail as e
join project_departments as d
on e.department_id = d.department_id;

-- multiple CTEs
WITH high_salary AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
    WHERE salary > 70000
),

mumbai_departments AS (
    SELECT
        department_id,
        department_name,
        location
    FROM project_departments
    WHERE location = 'Mumbai'
)

-- SELECT *
-- FROM high_salary;

SELECT
    h.employee_name,
    h.salary,
    m.department_name,
    m.location
FROM high_salary AS h
JOIN mumbai_departments AS m
    ON h.department_id = m.department_id;
    
    
-- Ek CTE ko doosre CTE mein use karna
WITH high_salary AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
    WHERE salary > 70000
),

high_salary_with_department AS (
    SELECT
        h.employee_name,
        h.salary,
        d.department_name
    FROM high_salary AS h
    JOIN project_departments AS d
        ON h.department_id = d.department_id
)

SELECT *
FROM high_salary_with_department;

-- group by
WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)

SELECT
    department_id,
    COUNT(*) AS total_employees
FROM employee_data
GROUP BY department_id;

WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
    WHERE salary > 60000
)

SELECT
    department_id,
    COUNT(*) AS total_employees
FROM employee_data
GROUP BY department_id;

-- CTE _ aggregate function
WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)

SELECT COUNT(*) AS total_employees
FROM employee_data;


WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)

SELECT AVG(salary) AS average_salary
FROM employee_data;

WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)

SELECT
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM employee_data;

-- CTE + having
WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)

SELECT
    department_id,
    COUNT(*) AS total_employees
FROM employee_data
GROUP BY department_id
HAVING COUNT(*) > 2;


WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)

SELECT
    department_id,employee_name,
    AVG(salary) AS average_salary
FROM employee_data
GROUP BY 1,2
HAVING AVG(salary) > 70000;


-- Department-wise Calculations using CTE
WITH department_data AS (
    SELECT
        department_id,
        COUNT(*) AS total_employees,
        AVG(salary) AS average_salary,
        MAX(salary) AS highest_salary,
        MIN(salary) AS lowest_salary,
        SUM(salary) AS total_salary
    FROM project_employees
    GROUP BY department_id
)

SELECT *
FROM department_data;

WITH department_data AS (
    SELECT
        department_id,
        COUNT(*) AS total_employees,
        AVG(salary) AS average_salary,
        MAX(salary) AS highest_salary,
        MIN(salary) AS lowest_salary
    FROM project_employees
    GROUP BY department_id
)

SELECT
    d.department_name,
    dd.total_employees,
    dd.average_salary,
    dd.highest_salary,
    dd.lowest_salary
FROM department_data AS dd
JOIN project_departments AS d
    ON dd.department_id = d.department_id;

-- CTE se Summary Result Banana
WITH department_summary AS (
    SELECT
        department_id,
        COUNT(*) AS total_employees,
        AVG(salary) AS average_salary,
        MAX(salary) AS highest_salary,
        MIN(salary) AS lowest_salary
    FROM project_employees
    GROUP BY department_id
)
SELECT *
FROM department_summary;

WITH department_summary AS (
    SELECT
        department_id,
        COUNT(*) AS total_employees,
        AVG(salary) AS average_salary,
        MAX(salary) AS highest_salary,
        MIN(salary) AS lowest_salary
    FROM project_employees
    GROUP BY department_id
)
SELECT
    d.department_name,
    ds.total_employees,
    ds.average_salary,
    ds.highest_salary,
    ds.lowest_salary
FROM department_summary AS ds
JOIN project_departments AS d
    ON ds.department_id = d.department_id;
    
    
    
-- CTE + Subquery
WITH high_salary AS (
    SELECT
        employee_name,
        salary
    FROM project_employees
    WHERE salary > (
        SELECT AVG(salary)
        FROM project_employees
    )
)
SELECT *
FROM high_salary;

WITH department_avg AS (
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM project_employees
    GROUP BY department_id
)
SELECT
    employee_name,
    salary,
    department_id
FROM project_employees AS e
WHERE salary > (
    SELECT avg_salary
    FROM department_avg AS d
    WHERE d.department_id = e.department_id
);

WITH employee_data AS (
    SELECT
        employee_name,
        salary,
        department_id,
        (SELECT AVG(salary)
         FROM project_employees) AS avg_salary
    FROM project_employees
)
SELECT
    employee_name,
    salary,
    avg_salary,
    department_id
FROM employee_data
WHERE salary > avg_salary;


WITH employee_data AS (
    SELECT
        employee_name,
        salary,
        AVG(salary) OVER() AS avg_salary
    FROM project_employees
)
SELECT
    employee_name,
    salary,
    avg_salary
FROM employee_data
WHERE salary > avg_salary;

-- CTE + Correlated Subquery
WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)
SELECT
    employee_name,
    salary,
    department_id
FROM employee_data AS e
WHERE salary > (
    SELECT AVG(e2.salary)
    FROM employee_data AS e2
    WHERE e2.department_id = e.department_id
);

-- CTE + EXISTS
WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)
SELECT
    employee_name,
    salary,
    department_id
FROM employee_data AS e
WHERE EXISTS (
    SELECT 1
    FROM project_departments AS d
    WHERE d.department_id = e.department_id
);

-- CTE + IN
WITH employee_data AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        department_id
    FROM project_employees
)
SELECT
e.employee_name,
e.salary,    
e.department_id,
d.department_name
FROM employee_data as e
join project_departments as d 
on e.department_id = d.department_id
WHERE e.department_id IN (
    SELECT department_id
    FROM project_departments
    WHERE department_name IN ('IT', 'Finance')
);













