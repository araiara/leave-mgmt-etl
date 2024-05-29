insert into dwh.dim_departments
select
	*
from std.departments
order by id
on conflict (id)
do nothing;
