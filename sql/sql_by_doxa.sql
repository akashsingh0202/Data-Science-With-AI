create database doxa;
use doxa;

create table doxa1(
id int primary key,
name varchar(40) not null,
age int check (age >22),
product varchar(40) default 'none'
);


insert into doxa1
values(1,'harish',35,default),
(2,'yogesh',40,'jeans');

select * from doxa1;

-- update 
update doxa1
set product = 'shirt'
where id =1;

--  update multiple values
update doxa1
set product='baggy'
where id in (1,2);

insert into doxa1 
values( 3 , 'akash',34,'sleeper'),
( 4 , 'aaditya',37,'pen'),
( 5 , 'aayush',39,'Book'),
( 6 , 'akshat',41,'copy');
-- 3rd way
update doxa1
set product='phone'
where id between 2 and 5;

select * from doxa1;

alter table doxa1
rename column name to emp_name;


alter table doxa1
add column email varchar(50);

update doxa1 
set email= case
			when id =1 then 'harish@gmial.com'
            when id =2 then 'yogesh@gmial.com'
            when id =3 then 'akash@gmial.com'
            when id =4 then 'aaditya@gmial.com'
            when id =5 then 'aayush@gmial.com'
            when id =6 then 'akshat@gmial.com'
            end
where id in (1,2,3,4,5,6);

select * from doxa1;
            

alter table doxa1
modify column email varchar(100);


-- tcl (transaction control language)
set autocommit = 0;
set SQL_SAFE_UPDATES=0;
delete from doxa1;
select * from doxa1;
rollback;





















