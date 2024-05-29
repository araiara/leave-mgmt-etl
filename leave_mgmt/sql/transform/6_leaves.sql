insert into std.leaves
select
	id::int,
	"userId"::int,
	"startDate"::date,
	"endDate"::date,
	"leaveDays"::int,
	reason,
	status,
	"leaveTypeId"::int,
	"fiscalId"::int,
	"createdAt"::timestamp,
	"updatedAt"::timestamp
from flatfile
order by id
on conflict (id)
do nothing;
