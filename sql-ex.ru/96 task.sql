/*
ѕри условии, что баллончики с красной краской использовались более одного раза, выбрать из них такие, которыми окрашены квадраты, имеющие голубую компоненту.
¬ывести название баллончика 
*/

select distinct v.v_name
from
utv v inner join 
 utb b on b.b_v_id = v.v_id
where 
v.v_color='R'
and
exists
(
	select *
	from utb b1 
	where b1.b_v_id = v.v_id
	and b1.b_vol > 0 
	having count(b1.b_v_id) > 1
)
and
exists 
(
	select b1.*
	from utb b1 inner join utv v1 on v1.v_id = b1.b_v_id
	where
	b1.b_q_id = b.b_q_id
	and 
	v1.v_color = 'B' 
	and 
	b1.b_vol > 0
)
order by v.v_name