create database market;
use market;
create table Vegetables (veg_Name varchar(25) ,Price int ,quantity float);
insert into Vegetables values ('tomato',40,20),('brinjal',60,15),('potato',35,18),('mirchi',50,30),('carrot',30,15),('drumstick',20,12);
select * from Vegetables;
update vegetables set quantity=30 where veg_Name='tomato';
update vegetables set quantity=20 where veg_Name='brinjal';
update vegetables set quantity=20 where veg_Name='potato';
update vegetables set quantity=30 where veg_Name='mirchi';
update vegetables set quantity=20 where veg_Name='carrot';
update vegetables set quantity=15 where veg_Name='drumstick';
update vegetables set quantity=50 where veg_Name='onion';
update vegetables set quantity=20 where veg_Name='ladyfinger';
alter table Vegetables modify column Price int not null ;
alter table vegetables add column purchased_price int;
update  vegetables set purchased_price=price-10;


delimiter ##
drop function if exists item_check;
create function item_check (n varchar(25)) returns varchar(20)
deterministic
begin
	declare output varchar(30);
    set output='False';
    if Exists (select * from Vegetables where veg_name=n) then
		set output='True';
	end if;
    return output;
end ##

select item_check('tomato');


delimiter $$
drop function if exists Quantity;
create function Quantity (n varchar(25), num float) returns varchar(20)
deterministic
begin
		declare output varchar(20);
        declare vegExists varchar(10);
        
        set vegExists=item_check(n);
        if vegExists= 'True' then
			if num<=(select quantity from vegetables where veg_Name=n and num<=quantity) then
				set output='True';
			else
				set output='False';
			end if;
		else
			set output=concat('vegetable', n,'does not exist');
		end if;
        return output;
end $$

select Quantity( 'tomato',15);

drop function get_price;
delimiter $$

create function get_price(veg_name varchar(25)) returns int
deterministic
begin 
    declare price int;
    select Price as price from Vegetables where veg_Name = veg_name LIMIT 1;
    return price;
end $$

delimiter ;



select get_price('tomato');
select 
* from vegetables;


SHOW FULL COLUMNS FROM Vegetables WHERE Field = 'veg_Name';
select * from information_schema.columns where table_schema='market' and table_name='Vegetables';


create table Customer_Details(Name varchar(30), phn_nbr bigint ,Location varchar(30)); 
select * from Customer_Details;
alter table Customer_Details modify column Name varchar(30);
delete from Customer_Details;

