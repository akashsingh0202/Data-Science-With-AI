CREATE DATABASE student;
USE student;
CREATE table users(
	userID INT primary key auto_increment,
    username VARCHAR(50) not null,
    useremail VARCHAR(50) unique,
    age int check(age>=18),
    userphone int
);

CREATE TABLE students(
	serial_num INt primary key auto_increment,
	student_name varchar(50) not null,
    student_father_name VARCHAR(50) not null,
    student_mother_Name varchar(50) not null,
    student_marks int not null,
    mobile_num bigint 
);

-- add new column
alter table students 
ADD age varchar(50);

-- change the size of datatype that varchar 50 to varchar 100

alter table students modify student_mother_Name varchar(100) not null;


-- add the column in table
alter table students 
ADD email varchar(50) unique;

-- to modification in the table 
alter table students modify email varchar(100) not null;


-- rename the column name 
alter table students change column student_mother_name mother_name 
varchar (50);

alter table students change column student_father_name father_name 
varchar(50);


-- remove the column
alter table students
drop column email;


-- rename the table name 
alter table students 
rename to student ;

insert into 
student(student_name,father_name,mother_name,
		student_marks,mobile_num,age,email)
values('akash singh','rajesh singh','krishna singh',
		84,8103412074,22,'akashsinghsinghraul@gmail.com'),
        ('raj gautam','ramesh gautam','shubhashree gautam',
        90,7415044221,22,'raju@gmail.com'),
        ('rahul','bablu','rekha',80,9889812431,26,'rahul@gmail.com');

select * from student;

-- delete query IT DELETES SINGLE ROW
DELETE FROM student WHERE serial_num=2;


-- delete multiple line using index = use between
DELETE FROM student
WHERE serial_num BETWEEN 5 AND 7;

-- DELETE FROM student
-- WHERE serial_num IN (3,5,7);


-- using truncate we can erase all data from the data
-- trucate table student;


-- using drop we can delete the table 
-- drop table student;



-- update the value
UPDATE student
SET student_marks=91
WHERE serial_num=3;

