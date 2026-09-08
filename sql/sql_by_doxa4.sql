use doxa;
select * from doxa3;
ALTER TABLE doxa3
ADD COLUMN bonus DECIMAL(10,2);
desc doxa3;
UPDATE doxa3
SET bonus = CASE employee_id
    WHEN 1 THEN 5000
    WHEN 2 THEN 3500
    WHEN 3 THEN 4200
    WHEN 4 THEN 6000
    WHEN 5 THEN 2800
    WHEN 6 THEN 7500
    WHEN 7 THEN 3200
    WHEN 8 THEN 4500
    WHEN 9 THEN 5500
    WHEN 10 THEN 3000
    WHEN 11 THEN 6800
    WHEN 12 THEN 2500
    WHEN 13 THEN 4800
    WHEN 14 THEN 7200
    WHEN 15 THEN 3900
    WHEN 16 THEN 5100
    WHEN 17 THEN 2900
    WHEN 18 THEN 6300
    WHEN 19 THEN 4100
    WHEN 20 THEN 8000
    WHEN 21 THEN 3600
    WHEN 22 THEN 4700
    WHEN 23 THEN 5400
    WHEN 24 THEN 3100
    WHEN 25 THEN 6900
    WHEN 26 THEN 2700
    WHEN 27 THEN 5800
    WHEN 28 THEN 4300
    WHEN 29 THEN 7600
    WHEN 30 THEN 3400
    WHEN 31 THEN 5200
    WHEN 32 THEN 6600
    WHEN 33 THEN 2900
    WHEN 34 THEN 4900
    WHEN 35 THEN 7100
    WHEN 36 THEN 3800
    WHEN 37 THEN 5600
    WHEN 38 THEN 2400
    WHEN 39 THEN 6200
    WHEN 40 THEN 4600
    WHEN 41 THEN 7800
    WHEN 42 THEN 3300
    WHEN 43 THEN 5100
    WHEN 44 THEN 6700
    WHEN 45 THEN 2800
    WHEN 46 THEN 5900
    WHEN 47 THEN 4400
    WHEN 48 THEN 7300
    WHEN 49 THEN 3500
    WHEN 50 THEN 5000
    WHEN 51 THEN 6400
    WHEN 52 THEN 2600
    WHEN 53 THEN 5700
    WHEN 54 THEN 4200
    WHEN 55 THEN 8100
    WHEN 56 THEN 3700
    WHEN 57 THEN 5300
    WHEN 58 THEN 6900
    WHEN 59 THEN 3000
    WHEN 60 THEN 4800
    WHEN 61 THEN 7400
    WHEN 62 THEN 3900
    WHEN 63 THEN 5500
    WHEN 64 THEN 2300
    WHEN 65 THEN 6100
    WHEN 66 THEN 4700
    WHEN 67 THEN 7900
    WHEN 68 THEN 3200
    WHEN 69 THEN 5200
    WHEN 70 THEN 6500
    WHEN 71 THEN 2700
    WHEN 72 THEN 5800
    WHEN 73 THEN 4300
    WHEN 74 THEN 7000
    WHEN 75 THEN 3600
    WHEN 76 THEN 5400
    WHEN 77 THEN 6800
    WHEN 78 THEN 3100
    WHEN 79 THEN 4900
    WHEN 80 THEN 7700
    WHEN 81 THEN 4000
    WHEN 82 THEN 5600
    WHEN 83 THEN 2500
    WHEN 84 THEN 6300
    WHEN 85 THEN 4500
    WHEN 86 THEN 8200
    WHEN 87 THEN 3400
    WHEN 88 THEN 5100
    WHEN 89 THEN 6600
    WHEN 90 THEN 2900
    WHEN 91 THEN 6000
    WHEN 92 THEN 4100
    WHEN 93 THEN 7500
    WHEN 94 THEN 3700
    WHEN 95 THEN 5300
    WHEN 96 THEN 6800
    WHEN 97 THEN 2600
    WHEN 98 THEN 5700
    WHEN 99 THEN 4400
    WHEN 100 THEN 8000
END;

-- round()
select round(bonus,-3) as rounded_bonus
from doxa3; 


-- sum()
select sum(bonus) as total_bonus
from doxa3; 

-- avg()
select avg(bonus) as average_bonus
from doxa3; 

-- max()
select max(bonus) as maximum_bonus
from doxa3; 

-- min()
select min(bonus) as minimum_bonus
from doxa3; 

-- ceil()
select bonus, ceil(bonus/1000) as ceil_bonus
from doxa3; 


-- floor()
select bonus, floor(bonus/1000) as floor_bonus
from doxa3; 


-- abs()
select bonus, abs(bonus-5000) as absolute_bonus
from doxa3;


-- power()
select bonus,power(bonus/1000,2) as power_bonus
from doxa3;


-- sqrt()
select bonus,sqrt(bonus) as sqrt_bonus
from doxa3;

-- mod()
select bonus , mod(bonus,1000) as remainder
from doxa3;

select round( avg(bonus),2) as round_avg_bonus
from doxa3;


select bonus,ceil(bonus/1000) as ceil_bonus
from doxa3;


select bonus,floor(bonus/1000) as floor_bonus
from doxa3;


select bonus, abs(bonus-5000) as absolute_bonus
from doxa3;

select bonus,power(bonus/1000,2) as power_bonus
from doxa3;

select bonus,sqrt(bonus) as sqrt_bonus
from doxa3;

select bonus, abs(bonus-5000) as absolute_bonus
from doxa3;

select bonus,power(bonus/1000,2) as power_bonus
from doxa3;

select bonus,sqrt(bonus) as sqrt_bonus
from doxa3;


select round(avg(bonus),-2) as round_avg_bonus
from doxa3;

select  max(bonus)-min(bonus) as difference_bonus
from doxa3;


select round(bonus+bonus/10 ,2)as new_bonus
from doxa3;
 
 
 select bonus,abs(bonus-5000) as difference
 from doxa3
 where bonus<5000; 
 
 
 select bonus,
 ceil(bonus/1000) as ceil_bonus,
 floor(bonus/1000) as floor_bonus
 from doxa3;
 
 select round(sqrt(bonus),2)
 from doxa3;
 
 select * from doxa3;
 select distinct(city) from doxa3;
 
-- date and time
select curdate();
select curtime();
select now();
select year(curdate());
select month(curdate());
 
select * from doxa3;
select year(joining_date) as year_of_joining
from doxa3;

select month(joining_date) as month_of_joining
from doxa3;

select day(joining_date) as date_of_joining
from doxa3;

select dayname(joining_date) as date_of_joining
from doxa3;

alter table doxa3
add column current_date_ date;

update doxa3
set current_date_ = curdate()
where employee_id between 1 and 100;

select * from doxa3;

-- select *, datediff(current_date_,joining_date)
-- from doxa3;




-- case expressions
-- always prefer to write your case expression in between select and from clause

-- syntax
-- case
  -- when condition then value
  -- else value end col_name
  
  
select *,
case  
    when salary>50000 then 'high paid'
    when salary<50000 and salary>40000 then 'moderate'
    else 'low paid'
    end as levels
from doxa3;
alter table doxa3
add column status varchar(50);

update doxa3
set status = case 
    when salary>50000 then 'high paid'
    when salary<50000 and salary>40000 then 'moderate'
    else 'low paid'
    end ;
    
select * from doxa3;
    
update doxa3
set city = case 
               when city='Hyderabad'then "Hyd"
               when city='Mumbai' then "Mum"
               when city = 'Delhi' then "Del"
               when city = "Pune" then "pun"
               end;
select * from doxa3;

rollback;    

    







