use doxa;

select * from doxa3;
-- Upper() and lower()
select city ,
upper(city)as upper_city,
lower(city)as lower_city
from doxa3;

-- concat()
select employee_name, concat(employee_name, ' ' , department) as concat_name
from doxa3;

-- length 
select employee_name,city ,
length(city) as length_city
from doxa3;

-- trim()->ltrim()->rtrim()
select ('      hello     ');
select trim('      hello     ');
select rtrim('      hello     ');
select ltrim('      hello     ');

select * from doxa3;

select city, replace(city,'Delhi','NCR')as replace_data
from doxa3;

-- subsstring
select city,concat(substring(city,1,2), substring(employee_name,1,2))as passcode
from doxa3;

select * from doxa3;

