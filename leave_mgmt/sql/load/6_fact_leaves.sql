insert into dwh.fact_leaves
select
	id,
	employee_id,
	start_date,
	end_date,
	leave_days,
	reason,
	status,
	leave_type_id,
	fiscal_id,
	e.department_id,
	e.designation_id,
	created_at,
	updated_at
from std.leaves l
left join std.employees e
	on l.employee_id = e.user_id
order by id
on conflict (id)
do nothing;
