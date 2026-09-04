create database sql4;
use sql4;

create table department(
emp_id int auto_increment unique,
emp_name varchar(50),
emp_email varchar(90),
department varchar(50),
salary int 
) ;

insert into department
 ( emp_name,emp_email,department,salary)
 values('akash','akash@gmail.com','it',25000),
 ('aman','aman@gmail.com','hr',30000),
 ('ashu','ashu@gmail.com','sales',20000);
 
 
 update department
 set emp_name='Akash singh'
 where emp_id=1;
 
 select * from department;
 
 
 -- upper()
--  select emp_name,
--  upper(emp_name) as employee
--  from department;
 
 -- lower()
-- select emp_name,
--  lower(emp_name) as employee
--  from department;
 
 
 -- concat()
-- select concat(emp_name, ' ' , department) as employee
--  from department;
 
 
 alter table department 
 add column passcode varchar(50);

update department 
set passcode =
concat(emp_name,' ', department)
where emp_id = 3;
 
 
select * from department;
  
  
delete from department
where emp_id between 4 and 15;


-- substring() 
select emp_name ,
substring(emp_name,1,4) from department;

-- length()
select emp_name ,
length(emp_name) from department;
 
 
 select * from department;
 
 -- left()
 select left(emp_name,4)
 from department;
 
 -- right()
select right(emp_name,4)
 from department;
 
 -- trim()
select trim(emp_name)
 from department;
 
 -- replace()
select replace(emp_name,'aman','rahul')
 from department;
 
 -- reverse()
  select reverse(emp_name)
 from department;
 
 
 -- locate
select locate('a',emp_name)
 from department;
 
 
 
