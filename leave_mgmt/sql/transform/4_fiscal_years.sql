insert into std.fiscal_years
select
	distinct "fiscalId"::int,
	"fiscalStartDate"::timestamp,
	"fiscalEndDate"::timestamp,
	"fiscalIsCurrent":: bool
from flatfile
order by "fiscalId"
on conflict (id)
do nothing;
