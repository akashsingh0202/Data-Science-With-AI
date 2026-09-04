create database sql4;
insert into company
(emp_name,department,salary,city)
values('AKASH SINGH','sales',25000,'Hyderabad'),
	  ('Raj Singh', 'business', 12000,'pune'),
      ('ayush Singh','construction',10000,'Bhopal'),
      ('Aditya Singh','Electrician',12300,'Indore'),
      ('Om','Production',14900,'Ahemdabad'),
      ('Harshit','Training',25000,'Bhuj'),
      ('sidhhant Mishra','Logistics',23000,'Ahemdabad');

insert into company
(emp_name,salary,city)
values('Pavan',250000,"Ahemdabad"),
('Anubhav',25000,'Begaluru'),
('Akash',2000,'Hyderabad');

SELECT * from company;

DELETE FROM company where emp_id BETWEEN 11 AND 13;





-- select Where clause operator
select * from company where  city = 'hyderabad';
select * from company where  city != 'hyderabad';
select * from company where  salary < 15000;
select * from company where  salary > 15000;
select * from company where  salary <= 14900;
select * from company where  salary >= 14900;
select * from company where  salary between 12000 and 23000;
select * from company where  city in ('hyderabad','begaluru');
select * from company where  city not in ('hyderabad','begaluru');
select * from company where  city like 'A%';
select * from company where  city like '%d';
select * from company where  city not like 'A%';


-- WHERE CLAUSE OPERATOR -Logical & Null operators 
select * from company;

select * from company where salary = 25000 and city = 'hyderabad' ;
select * from company where salary > 20000 or city = 'Ahemdabad' ;
select * from company where not city = 'Ahemdabad' ;
select * from company where city IS NULL ;
select * from company where city IS NOT NULL ;



-- order by
select * from company;

-- SELECT * FROM company
-- order by salary ASC;

-- select * from company
-- order by city desc;

-- select * from company
-- order by department asc;

-- limit 



-- limit + sorting 
-- select * from company 
-- order by emp_id desc
-- limit 3;


-- limit 
select * from company
limit 1,5;

-- (0 --> start from 5 --> how many values




