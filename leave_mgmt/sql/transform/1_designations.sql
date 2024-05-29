insert into std.designations
select
	distinct "designationId"::int,
	"designationName"
from flatfile
order by "designationId"
on conflict (id)
do nothing;
