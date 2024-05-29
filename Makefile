.PHONY: make_migrations make_migrate

make_migrations:
	docker-compose run etl alembic --config migrations/alembic.ini revision --autogenerate -m "$(msg)"

make_migrate:
	docker-compose run etl alembic --config migrations/alembic.ini upgrade head

history:
	docker-compose run etl alembic --config migrations/alembic.ini history

downgrade:
	docker-compose run etl alembic --config migrations/alembic.ini downgrade -1
