create database sql5;
use sql5;
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    salary DECIMAL(10,2),
    bonus DECIMAL(10,2),
    experience DECIMAL(4,1),
    rating DECIMAL(3,2),
    age INT

);

INSERT INTO employees (name, salary, bonus, experience, rating, age)
VALUES
('Akash', 45000.75, 5000.50, 2.5, 4.75, 22),
('Rahul', 52340.25, 4500.75, 3.2, 4.20, 25),
('Amit', 38750.80, 3200.40, 1.8, 3.90, 21),
('Rohan', 67500.99, 8500.25, 5.6, 4.85, 28),
('Priya', 48900.45, 6000.80, 2.9, 4.50, 24),
('Neha', 55000.60, 7200.35, 4.1, 4.65, 27),
('Vikas', 41200.30, 3800.60, 1.5, 3.75, 23),
('Sneha', 72000.95, 9500.45, 6.2, 4.95, 30);


SELECT * FROM employees;

-- abs()
SELECT ABS(-500);
SELECT name, ABS(salary - 50000)
FROM employees;

-- round()
SELECT name, ROUND(salary)
FROM employees;

-- ceil ()
SELECT name, CEIL(salary)
FROM employees;

-- floor()
select name, floor(salary)
from employees; 


-- mod()
SELECT name, age,
MOD(age, 2) AS remainder
FROM employees;

-- power
SELECT name, POWER(age, 2)
FROM employees;

-- SQRT
SELECT name, SQRT(age)
FROM employees;

-- RAND()
SELECT name, RAND()
FROM employees;

-- tasks
select name , round(salary)
from employees;

select name , floor(salary)
from employees;

select name , ceil(salary)
from employees;

select name , power(age,2)
from employees;

select name , sqrt(age)
from employees;

select name ,age, mod(age,2) as remainder
from employees;


-- aggregate function 
-- sum()
SELECT SUM(salary)
FROM employees;

-- AVG()
select avg(salary) as avg_salary
from employees;

-- Max()
select max(salary)
from employees;

-- MIN()
select min(salary)
from employees;


-- tasks
select name ,abs(salary-5000) 
from employees ;

select name ,salary ,salary+bonus as total_income
from employees ;

select name ,salary, salary/10 as '10%ofsaalary'
from employees;

select sum(salary)
from employees;

select avg(salary)
from employees ;

select MIN(salary)
from employees ;

select MAX(salary)
from employees ;

SELECT name, ROUND(salary, -3)
FROM employees;

select sum(salary)
from employees;

select sum(bonus)
from employees;


select name , power(age,3)
from employees;

select name , rand()
from employees;

SELECT name, salary, ROUND(salary, 3) AS rounded_salary
FROM employees;







