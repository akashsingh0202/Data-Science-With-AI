create database _select_where_;
use _select_where_;

create table company(
	emp_id int primary key auto_increment,
    emp_name varchar(50) not null,
    department varchar(50) default 'IT',
    salary int not null,
    city varchar(50)
);

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

select * from company where city='Hyderabad' and department='IT';
-- select emp_name as employee_list ,salary from company;

SELECT * from company;





