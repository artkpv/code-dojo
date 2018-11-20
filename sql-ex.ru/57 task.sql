/*
Для классов, имеющих потери в виде потопленных кораблей и не менее 3 кораблей в базе данных, вывести имя класса и число потопленных кораблей. 
*/
select class, sum(r)
from
(
select s.class class, s.name [name] from classes c join ships s on s.class = c.class where s.class <> s.name
union 
select s.name, s.name from ships s where s.class = s.name
union
select o.ship, o.ship from outcomes o join classes c on c.class = o.ship
) T
left join
( select ship, 1 r from outcomes where result = 'sunk') T1 on T1.ship = T.name
group by class
having count(name) > 2 and sum(r) > 0