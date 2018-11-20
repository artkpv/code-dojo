
delete from pc
go
  
                               
----PC------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
insert into PC values(1,'1232',500,64,5,'12x',600)
insert into PC values(2,'1121',750,128,14,'40x',850)
insert into PC values(3,'1233',500,64,5,'12x',600)
insert into PC values(4,'1121',600,128,14,'40x',850)
insert into PC values(5,'1121',600,128,8,'40x',850)
insert into PC values(6,'1233',750,128,20,'50x',950)
insert into PC values(7,'1232',500,32,10,'12x',400)
insert into PC values(8,'1232',450,64,8,'24x',350)
insert into PC values(9,'1232',450,32,10,'24x',350)
insert into PC values(10,'1260',500,32,10,'12x',350)
insert into PC values(11,'1233',900,128,40,'40x',980)
insert into PC values(12,'1233',null,128,40,'50x',3333)

go

select chr, nullif([value], '<null>') value
from 
(
 select
 convert(varchar(100), model) COLLATE database_default as model,
 convert(varchar(100), speed) COLLATE database_default as speed,
 convert(varchar(100), ram) COLLATE database_default as ram ,
 convert(varchar(100), hd)  COLLATE database_default as hd ,
 convert(varchar(100), cd) COLLATE database_default as cd,
 coalesce ( convert(varchar(100), price), '<null>') COLLATE database_default as price
 from pc 
 where code = (select max(code) from pc)
) T
unpivot ([value] for chr in (model, speed, ram, hd, cd, price)) qq
