insert into dwh.dim_employees
select
	user_id,
	emp_id,
	full_name,
	email
from std.employees
order by user_id
on conflict (user_id)
do nothing;
