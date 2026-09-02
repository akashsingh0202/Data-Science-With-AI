CREATE DATABASE schooldb;
USE schooldb;

CREATE table students1(
	student_id int primary key auto_increment,
    student_name varchar(50) not null,
    email varchar(100) unique,
    age int check(age>18),
    course varchar(50) default 'BCA'
);
show tables;
drop table students;

INSERT INTO students1
(student_name , email,age ,course)
values('akash','akashsinghsinghraul@gmail.com',
22,'Btech');

select * from students1;

insert into students1
(student_name , email,age )
values('aman','aman@gmail.com',23);

update students1
set course='MCA'
where student_id =1;