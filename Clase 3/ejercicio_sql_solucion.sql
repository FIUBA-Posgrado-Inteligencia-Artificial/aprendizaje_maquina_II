with tabla_compras_persona as (
select *
from compras c
left join tarjeta t
on c.nro_tarjeta = t.nro_tarjeta),

personas_que_compraron_mas_de_5k as (
select id_titular, sum(monto) as monto_total
from tabla_compras_persona
where rubro = 'FARMACIA' OR rubro = 'SUPERMERCADOS'
group by id_titular
having sum(monto) > 5000),

tarjetas_sin_compras as ( 
select *
from tarjeta t 
where nro_tarjeta  not in ( select nro_tarjeta from compras c)  
)


select personas_que_compraron_mas_de_5k.id_titular, tarjeta.nro_tarjeta
from personas_que_compraron_mas_de_5k
left join tarjeta
on personas_que_compraron_mas_de_5k.id_titular = tarjeta.id_titular 
where nro_tarjeta not in (select nro_tarjeta from compras )