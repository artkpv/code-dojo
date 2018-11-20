/*
—чита€, что первый пункт вылета €вл€етс€ местом жительства, найти не москвичей, которые прилетали в ћоскву более одного раза. 
¬ывод: им€ пассажира, количество полетов в ћоскву 
*/
select pa.[name], count(p.trip_no) 
from 
 trip t 
  inner join pass_in_trip p on p.trip_no = t.trip_no
  inner join passenger pa on pa.id_psg = p.id_psg
where 
town_to = 'Moscow'
and 
--он не москвич
exists 
(
 select p1.id_psg, p1.date
 from trip t1 
  inner join pass_in_trip p1 on t1.trip_no = p1.trip_no
 where 
  p1.id_psg = p.id_psg
  and
  p1.trip_no = (
  select top 1 p2.trip_no
   from pass_in_trip p2 inner join trip t2 on t2.trip_no = p2.trip_no
   where p2.id_psg = p1.id_psg 
   order by p2.date, t2.time_out
  ) 
  and 
  t1.town_from <> 'Moscow'
)
group by pa.[name], pa.id_psg
having count(p.trip_no) > 1

