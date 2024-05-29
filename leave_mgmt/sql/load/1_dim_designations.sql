insert into dwh.dim_designations
select
	*
from std.designations
order by id
on conflict (id)
do nothing;
