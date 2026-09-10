use doxa;
select * from doxa3;

select department,count(*) 
from doxa3
group by department;

select department,sum(salary) as sum
from doxa3
group by department;

select department,city,count(*) as sum
from doxa3
group by city, department;



-- having
select department ,city,avg(salary)as average, year(joining_date)as joining_year,age
from doxa3
group by department,city,year(joining_date),age
having avg(salary)>45000 and joining_year<2024 and age>25
order by age asc
limit 3;