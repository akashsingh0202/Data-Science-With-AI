create database brez;
use brez;
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Sales'),
(4, 'Finance'),
(5, 'Marketing');

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    salary INT,
    city VARCHAR(50),
    experience INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

INSERT INTO employees VALUES
(101, 'Amit', 1, 60000, 'Delhi', 3),
(102, 'Priya', 2, 45000, 'Mumbai', 2),
(103, 'Rahul', 1, 75000, 'Pune', 5),
(104, 'Neha', 3, 50000, 'Delhi', 4),
(105, 'Vikas', 2, 40000, 'Bhopal', 1),
(106, 'Sneha', 3, 65000, 'Mumbai', 6),
(107, 'Arjun', 1, 80000, 'Bangalore', 7),
(108, 'Pooja', 4, 55000, 'Pune', 3),
(109, 'Karan', 3, 50000, 'Delhi', 2),
(110, 'Anjali', 4, 70000, 'Mumbai', 5),
(111, 'Rohit', 5, 35000, 'Bhopal', 1),
(112, 'Simran', 1, 60000, 'Delhi', 4);


SELECT * FROM departments;

SELECT * FROM employees;

with employee as (
  select * from employees
  where salary>35000
  )
select * from employee;


with employeee as (
  select employee_name,salary
  from employees
  where salary>30000
  )
  
select * from employeee
order by salary desc;

with xperienced_employees as (
  select * from employees 
  where salary>30000 and department_id=2
  )
  
select * from xperienced_employees
order by salary desc;


with department_salary as (
   select department_id, avg(salary) as average_salary
   from employees 
   group by department_id
   having avg(salary)>35000
   )
   
select * from department_salary
order by average_salary desc; 



with department_count as (
  select count(*) ,department_id as total_employees
  from employees
  group by department_id
  having count(*)>2
  )
  
select * from department_count
order by total_employees desc;
  

with department_avg as (
  select department_id , avg(salary) as average_salary
  from employees
  group by department_id
  ),
  high_avg_departments as (
  select * from department_avg
  where average_salary>35000
  )
  
select * from high_avg_departments;


with department_avg as (
  select department_id , avg(salary) as avg_salary
  from employees
  group by department_id
  )
  select d.department_name,da.avg_salary
  from department_avg as da
  join departments as d
    on da.department_id = d.department_id
  WHERE d.department_name IN ('IT', 'HR')
  order by da.avg_salary desc;
  
  
with department_count as (
 select department_id , count(*) as department_member
 from employees
 group by department_id
 having count(*) >2
 )
 select d.department_name ,dc.department_member
 from department_count as dc
 join departments as d 
  on dc.department_id=d.department_id
order by department_member desc
;


with department_avg as (
 select department_id,avg(salary) as avg_salary
 from employees
 group by department_id
 having avg(salary)>35000
 ),department_count as (
  select department_id,count(*) as employee_count 
  from employees
  group by department_id 
  )
  select 
    d.department_name ,
    da.avg_salary,
    dc.employee_count 
    from department_avg as da
    join departments as d
     on da.department_id = d.department_id
	join department_count as dc
    on dc.department_id =d.department_id;
    
with  salary_category as (
  select department_id , avg(salary) as avg_salary
  from employees
  group by department_id
  )
select * ,
 CASE 
	when avg_salary>=50000 then 'Excellent'
    when avg_salary>=35000 then 'Good'
    else 'need improvement'
    end as salary_categ
from salary_category;


with avg_salary as (
  select department_id ,avg(salary) as avg_sal
  from employees 
  group by department_id
  )
  select * from avg_salary
  order by avg_sal desc 
  limit 2;
  
  
  
with ranked_employees as (
select employee_id,
department_id , 
employee_name,
salary,
row_number() over (
partition by department_id
order by salary asc)as rn
from employees
)
 select * from ranked_employees
 where rn>=2
 order by rn;
 
 with ranked_employees as (
   select department_id ,employee_name , salary,employee_id,
   rank() over(
   partition by department_id 
         order by salary desc
         ) as salary_rank
   from employees 
   )
   
 select * from 
 ranked_employees
 ORDER BY department_id, salary_rank;
  
  

with ranked_employees as (
   select department_id ,employee_name , salary,employee_id,
   dense_rank() over(
   partition by department_id 
         order by salary desc
         ) as dense_rank_column
   from employees 
   )
   
 select * from 
 ranked_employees
 ORDER BY department_id, dense_rank_column;
 
 with ranked_employees as (
   select department_id ,employee_name , salary,employee_id,
   dense_rank() over(
   partition by department_id 
         order by salary desc
         ) as dense_rank_column
   from employees 
   )
   
 select * from 
 ranked_employees
 where dense_rank_column<=2
 ORDER BY department_id, dense_rank_column;
 
 
 WITH employee_running_total AS (
 select employee_id, employee_name,
        sum(salary) over( 
        order by employee_id  
         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW 
         ) AS running_total
         
         from employees 
         )
select * from employee_running_total order by employee_id
 

