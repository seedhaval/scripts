#!/bin/bash
cd /storage/internal/data/
sqlite3 actions.db <<eof
.headers on
create temp table hr_list (
    hr integer
) ;

with cte as (
select 0 nr
union all
select nr+1
from cte
where nr < 24
)
insert into hr_list
select nr from cte;

select
a.hr
,b.action_nm
,b.strt_hr
,b.end_hr
from hr_list a
left outer join action b
on a.hr >= b.strt_hr
and a.hr <= b.end_hr
order by 1 ;

select
a.hr
,count(*)
from hr_list a
inner join action b
on a.hr >= b.strt_hr
and a.hr <= b.end_hr
group by 1 ;
eof
