insert into dwh.dim_leave_types
select
	*
from std.leave_types
order by id
on conflict (id)
do nothing;
