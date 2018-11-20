/*
Какое максимальное количество черных квадратов можно было бы окрасить в белый цвет оставшейся краской 
*/

select 
min(C)
from
(
select floor( ( (select count(*) from utv v1 where v1.v_color = v.v_color) * 255 - sum(b_vol)) / 255) C
from utv v join utb on b_v_id = v_id
group by v_color 
) T