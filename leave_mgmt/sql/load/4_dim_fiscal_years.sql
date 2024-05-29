insert into dwh.dim_fiscal_years
select
	*
from std.fiscal_years
order by id
on conflict (id)
do nothing;
