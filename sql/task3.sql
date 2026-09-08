USE groupby_having_practice;

select * from employees;

select department ,count(*) as employees_in_each_sector
from employees 
group by department;



select city ,count(*) as employees_in_each_sector
from employees 
group by city;

select department ,sum(salary) as employees_salary
from employees 
group by department;

select department ,avg(salary) as employees_avg_salary
from employees 
group by department;

select city ,max(salary) as employees_max_salary
from employees 
group by city;

select city ,min(salary) as employees_max_salary
from employees 
group by city;

select department, city ,sum(salary) as employees_salary
from employees 
group by city,department;

select department, city ,avg(salary) as employees_salary
from employees 
group by city,department;


select department, city ,max(salary) as employees_salary
from employees 
group by city,department;


select department, count(*)
from employees
group by department
having count(*)>=4;


select city, count(*)
from employees
group by city
having count(*)>=4;

select department, avg(salary)
from employees
group by department
having avg(salary)>=50000;

select department, sum(salary)
from employees
group by department
having sum(salary)>=150000;

select city , department ,count(*)
from employees
group by city ,department
having count(*)>=2;

select city,department, avg(salary)
from employees
group by city,department
having avg(salary)>=45000;

select city , department ,sum(salary)
from employees 
group by city,department
having sum(salary)>=100000;


select department,count(*)
from employees
where salary>40000
group by department
having count(*)>3;


select 
city,
department,
count(*) as total_employee,
sum(salary)as total_salary,
avg(salary) as avg_salary
from employees
group by city,department
having count(*)>=2;
