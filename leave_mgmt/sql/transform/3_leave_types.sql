insert into std.leave_types
select
	distinct "leaveTypeId"::int,
	"leaveTypeName",
	"defaultDays":: int,
	"transferableDays":: int
from flatfile
order by "leaveTypeId"
on conflict (id)
do nothing;
