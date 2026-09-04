create database task2;
use task2;

create table customer ( 
customer_id int unique auto_increment ,
customer_name varchar(50),
product_buy varchar(50) not null,
product_Q int ,
total_bill int 
);

alter table customer change column product_buy product_name varchar (50);



insert into customer(customer_name , product_name , product_Q , total_bill)
values('akash','fridge', 3 , 250000),
	  ('aman','AC', 6 , 400000),
      ('akshat','cooler', 3 , 25000),
      ('sachin','TV', 3 , 20000),
      ('Adarsh','Light', 200 , 10000),
      ('nikesh','BED', 3 , 200000);


select * from customer;


select * from customer 
 where customer_name like '%N%';
 
 
 select * from customer 
 where total_bill >= 25000 and product_name='cooler';
 
 
 select * from customer 
 where customer_name in ('Akash','Akshat','sachin');
 
 select * from customer 
 order by  total_bill desc
 limit 3;
 