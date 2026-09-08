use doxa;
select * from doxa1;

--  fetching data from differeb=nt table  and insert into new table
create table doxa2 as 
select * from doxa1;

select * from doxa2;

-- where - it is used to filter the data
select *
from doxa2
where product='phone';

select *
from doxa2;

select *
from doxa2
where product='phone' and age>=35;

select *
from doxa2;


CREATE TABLE doxa3 (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    city VARCHAR(50),
    salary DECIMAL(10,2),
    joining_date DATE
);

INSERT INTO doxa3
(employee_id, employee_name, age, department, city, salary, joining_date)
VALUES

(1, 'Akash', 22, 'IT', 'Hyderabad', 45000, '2023-01-15'),
(2, 'Rahul', 25, 'HR', 'Mumbai', 40000, '2022-03-20'),
(3, 'Amit', 28, 'Finance', 'Delhi', 55000, '2021-07-10'),
(4, 'Rohit', 24, 'IT', 'Pune', 48000, '2023-05-12'),
(5, 'Vikas', 30, 'Sales', 'Hyderabad', 60000, '2020-02-18'),
(6, 'Ankit', 26, 'Marketing', 'Mumbai', 50000, '2022-08-22'),
(7, 'Suresh', 29, 'IT', 'Delhi', 65000, '2021-09-14'),
(8, 'Ramesh', 27, 'HR', 'Pune', 42000, '2023-03-11'),
(9, 'Karan', 23, 'Sales', 'Hyderabad', 38000, '2024-01-05'),
(10, 'Arjun', 31, 'Finance', 'Mumbai', 70000, '2020-06-17'),

(11, 'Manish', 25, 'IT', 'Delhi', 47000, '2022-02-10'),
(12, 'Deepak', 28, 'Marketing', 'Pune', 52000, '2021-04-15'),
(13, 'Nikhil', 24, 'HR', 'Hyderabad', 41000, '2023-07-20'),
(14, 'Raj', 32, 'Sales', 'Mumbai', 68000, '2020-09-25'),
(15, 'Vijay', 27, 'Finance', 'Delhi', 58000, '2021-11-12'),
(16, 'Ajay', 26, 'IT', 'Pune', 49000, '2022-05-19'),
(17, 'Sunil', 29, 'Marketing', 'Hyderabad', 54000, '2021-08-08'),
(18, 'Pankaj', 23, 'HR', 'Mumbai', 39000, '2024-02-14'),
(19, 'Mohit', 30, 'Sales', 'Delhi', 62000, '2020-10-30'),
(20, 'Ravi', 28, 'Finance', 'Pune', 57000, '2021-06-25'),

(21, 'Sachin', 24, 'IT', 'Hyderabad', 46000, '2023-04-12'),
(22, 'Aman', 27, 'Marketing', 'Mumbai', 51000, '2022-01-18'),
(23, 'Sumit', 31, 'Finance', 'Delhi', 69000, '2020-03-22'),
(24, 'Varun', 26, 'HR', 'Pune', 43000, '2022-09-16'),
(25, 'Abhishek', 29, 'Sales', 'Hyderabad', 61000, '2021-05-11'),
(26, 'Nitin', 25, 'IT', 'Mumbai', 48000, '2023-02-09'),
(27, 'Gaurav', 28, 'Marketing', 'Delhi', 53000, '2021-10-15'),
(28, 'Tarun', 24, 'HR', 'Pune', 40000, '2023-08-21'),
(29, 'Harsh', 30, 'Sales', 'Hyderabad', 64000, '2020-07-19'),
(30, 'Yash', 27, 'Finance', 'Mumbai', 59000, '2021-12-24'),

(31, 'Neeraj', 26, 'IT', 'Delhi', 50000, '2022-06-13'),
(32, 'Kunal', 29, 'Marketing', 'Pune', 55000, '2021-03-08'),
(33, 'Prakash', 23, 'HR', 'Hyderabad', 39000, '2024-03-17'),
(34, 'Lokesh', 32, 'Sales', 'Mumbai', 71000, '2020-04-26'),
(35, 'Rajat', 28, 'Finance', 'Delhi', 60000, '2021-08-30'),
(36, 'Sanjay', 25, 'IT', 'Pune', 47000, '2022-11-05'),
(37, 'Ashish', 27, 'Marketing', 'Hyderabad', 52000, '2022-07-14'),
(38, 'Naveen', 24, 'HR', 'Mumbai', 41000, '2023-09-20'),
(39, 'Dinesh', 31, 'Sales', 'Delhi', 67000, '2020-12-10'),
(40, 'Rakesh', 29, 'Finance', 'Pune', 61000, '2021-02-28'),

(41, 'Aditya', 22, 'IT', 'Hyderabad', 44000, '2023-06-15'),
(42, 'Shivam', 26, 'Marketing', 'Mumbai', 50000, '2022-04-09'),
(43, 'Kishan', 30, 'Finance', 'Delhi', 66000, '2020-08-18'),
(44, 'Mukesh', 25, 'HR', 'Pune', 42000, '2023-01-27'),
(45, 'Pradeep', 29, 'Sales', 'Hyderabad', 63000, '2021-07-07'),
(46, 'Vivek', 27, 'IT', 'Mumbai', 51000, '2022-03-15'),
(47, 'Hemant', 28, 'Marketing', 'Delhi', 54000, '2021-09-29'),
(48, 'Sandeep', 24, 'HR', 'Pune', 40000, '2023-10-11'),
(49, 'Jatin', 31, 'Sales', 'Hyderabad', 68000, '2020-05-22'),
(50, 'Dev', 26, 'Finance', 'Mumbai', 56000, '2022-08-16'),

(51, 'Anil', 28, 'IT', 'Delhi', 52000, '2021-04-05'),
(52, 'Bhavesh', 25, 'Marketing', 'Pune', 49000, '2022-12-12'),
(53, 'Chandan', 23, 'HR', 'Hyderabad', 38000, '2024-01-25'),
(54, 'Darshan', 30, 'Sales', 'Mumbai', 65000, '2020-06-09'),
(55, 'Eshan', 27, 'Finance', 'Delhi', 58000, '2021-11-18'),
(56, 'Farhan', 26, 'IT', 'Pune', 50000, '2022-05-23'),
(57, 'Girish', 29, 'Marketing', 'Hyderabad', 56000, '2021-08-14'),
(58, 'Himanshu', 24, 'HR', 'Mumbai', 41000, '2023-02-28'),
(59, 'Ishan', 31, 'Sales', 'Delhi', 69000, '2020-09-19'),
(60, 'Jay', 28, 'Finance', 'Pune', 60000, '2021-03-30'),

(61, 'Kapil', 25, 'IT', 'Hyderabad', 47000, '2023-04-18'),
(62, 'Lalit', 27, 'Marketing', 'Mumbai', 53000, '2022-02-21'),
(63, 'Mohan', 32, 'Finance', 'Delhi', 72000, '2020-07-16'),
(64, 'Naresh', 26, 'HR', 'Pune', 44000, '2022-10-25'),
(65, 'Om', 29, 'Sales', 'Hyderabad', 62000, '2021-06-13'),
(66, 'Parth', 24, 'IT', 'Mumbai', 46000, '2023-05-09'),
(67, 'Qasim', 28, 'Marketing', 'Delhi', 55000, '2021-01-20'),
(68, 'Rohan', 25, 'HR', 'Pune', 42000, '2023-08-08'),
(69, 'Shubham', 30, 'Sales', 'Hyderabad', 66000, '2020-11-17'),
(70, 'Tushar', 27, 'Finance', 'Mumbai', 59000, '2021-09-02'),

(71, 'Umesh', 26, 'IT', 'Delhi', 51000, '2022-04-27'),
(72, 'Vinay', 29, 'Marketing', 'Pune', 57000, '2021-07-11'),
(73, 'Wasim', 23, 'HR', 'Hyderabad', 39000, '2024-02-19'),
(74, 'Yogesh', 31, 'Sales', 'Mumbai', 70000, '2020-03-08'),
(75, 'Zaid', 28, 'Finance', 'Delhi', 61000, '2021-12-15'),
(76, 'Arnav', 25, 'IT', 'Pune', 48000, '2022-06-22'),
(77, 'Bharat', 27, 'Marketing', 'Hyderabad', 52000, '2022-09-01'),
(78, 'Chetan', 24, 'HR', 'Mumbai', 40000, '2023-03-16'),
(79, 'Dhruv', 30, 'Sales', 'Delhi', 64000, '2020-08-24'),
(80, 'Ekansh', 28, 'Finance', 'Pune', 60000, '2021-05-28'),

(81, 'Faisal', 26, 'IT', 'Hyderabad', 49000, '2022-11-19'),
(82, 'Ganesh', 29, 'Marketing', 'Mumbai', 56000, '2021-02-07'),
(83, 'Hari', 23, 'HR', 'Delhi', 39000, '2024-01-11'),
(84, 'Inder', 32, 'Sales', 'Pune', 71000, '2020-04-14'),
(85, 'Javed', 27, 'Finance', 'Hyderabad', 58000, '2021-08-31'),
(86, 'Kartik', 25, 'IT', 'Mumbai', 47000, '2023-07-18'),
(87, 'Lakshya', 28, 'Marketing', 'Delhi', 55000, '2021-03-25'),
(88, 'Mayank', 24, 'HR', 'Pune', 41000, '2023-09-12'),
(89, 'Naman', 31, 'Sales', 'Hyderabad', 68000, '2020-06-21'),
(90, 'Ojas', 29, 'Finance', 'Mumbai', 62000, '2021-10-08'),

(91, 'Pranav', 26, 'IT', 'Delhi', 50000, '2022-05-16'),
(92, 'Raghav', 28, 'Marketing', 'Pune', 54000, '2021-01-29'),
(93, 'Sameer', 24, 'HR', 'Hyderabad', 40000, '2023-11-03'),
(94, 'Tejas', 30, 'Sales', 'Mumbai', 66000, '2020-07-12'),
(95, 'Utkarsh', 27, 'Finance', 'Delhi', 59000, '2021-04-26'),
(96, 'Vishal', 25, 'IT', 'Pune', 48000, '2022-08-14'),
(97, 'Yuvraj', 29, 'Marketing', 'Hyderabad', 57000, '2021-06-10'),
(98, 'Zeeshan', 23, 'HR', 'Mumbai', 39000, '2024-02-22'),
(99, 'Abhay', 31, 'Sales', 'Delhi', 69000, '2020-09-28'),
(100, 'Aryan', 28, 'Finance', 'Pune', 61000, '2021-12-06');

select * from doxa3;


select*
from doxa3
where city='Hyderabad' and department='HR' and salary>=39000
and year(joining_date)=2024 and month(joining_date)=3;


select * from doxa3;



select * from doxa3
-- where city like 'h%' ;
-- where city like '%i' ;
-- where city like '_u%' ;
-- where city like '____' ;
where city like '%n%' ;






