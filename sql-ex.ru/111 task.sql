select q_name, R.vol

from 
(select b_q_id, sum(b_vol) vol from utb inner join utv on b_v_id = v_id where v_color ='R' group by b_q_id) R
inner join 
(select b_q_id, sum(b_vol) vol from utb inner join utv on b_v_id = v_id where v_color ='G' group by b_q_id) G 
on R.b_q_id = G.b_q_id and R.vol=G.vol
inner join
(select b_q_id, sum(b_vol) vol from utb inner join utv on b_v_id = v_id where v_color ='B' group by b_q_id) B
on R.b_q_id = B.b_q_id and R.vol=B.vol
inner join 
utq on q_id = R.b_q_id
where 
R.vol <> 0 and R.vol <> 255
case