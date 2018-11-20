/*
Среди тех, кто пользуется услугами только какой-нибудь одной компании, определить имена разных пассажиров, летавших чаще других.
Вывести: имя пассажира и число полетов.
*/
select pa.[name], count(t.trip_no)
from trip t 
 inner join pass_in_trip p on t.trip_no = p.trip_no
 inner join passenger pa on pa.id_psg = p.id_psg
where
 not exists (
  select * from trip t1 inner join pass_in_trip p1 on t1.trip_no = p1.trip_no 
  where p1.id_psg = p.id_psg and t1.id_comp <> t.id_comp
  )
group by pa.[name], p.id_psg, pa.id_psg
having count(t.trip_no) = 
(
 select top 1 count(t.trip_no) trip_count
from trip t 
 inner join pass_in_trip p on t.trip_no = p.trip_no
 inner join passenger pa on pa.id_psg = p.id_psg
where
 not exists (
  select * from trip t1 inner join pass_in_trip p1 on t1.trip_no = p1.trip_no 
  where p1.id_psg = p.id_psg and t1.id_comp <> t.id_comp
  )
group by pa.[name], p.id_psg, pa.id_psg
order by trip_count desc
)