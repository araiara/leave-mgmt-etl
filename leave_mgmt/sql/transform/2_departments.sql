insert into std.departments(name)
select
	distinct "departmentDescription"
from flatfile
on conflict (name)
do nothing;
