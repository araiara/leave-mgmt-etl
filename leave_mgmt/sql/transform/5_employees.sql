insert into std.employees
select
	distinct "userId"::int,
	"empId"::int,
	initcap(concat_ws(' ', "firstName", "middleName", "lastName")) as full_name,
	email,
	dept.id,
	"designationId"::int
from flatfile ff
left join std.departments dept
	on ff."departmentDescription" = dept.name
order by "userId"
on conflict (user_id)
do nothing;
