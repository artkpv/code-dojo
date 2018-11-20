/*
Выбрать все белые квадраты, которые окрашивались только из баллончиков,
пустых к настоящему времени. Вывести имя квадрата 
*/

select 
	q.q_name
from 
	utB b 
	inner join 
	(
		--пустые баллончики 
		select b1.b_v_id, v1.v_color
		from 
		 utB b1 inner join utV v1 on b1.b_v_id = v1.v_id
		where b1.b_datetime < getdate()
		group by b1.b_v_id, v1.v_color
		having sum(b1.b_vol) = 255

	) v on b.b_v_id = v.b_v_id

	inner join 
	utQ q on b.b_q_id = q.q_id

group by b.b_q_id, q.q_name
having sum(b.b_vol) = 765