
select 
i.point, 
Coalesce(sum(inc),0) - 
Coalesce(
(select sum(out) from outcome_o o where o.point = i.point and o.date < cast('april 15 2001' as datetime))
, 0)
from 
income_o i
where i.date < cast('april 15 2001' as datetime)
group by i.point
