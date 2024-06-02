# Leave Management ETL
## Local Setup
### Using Docker
Clone the repository.
```
git clone git@github.com:araiara/leave-mgmt-etl.git
```
Set up environment variables.
```
DB_NAME=
DB_PORT=
DB_USERNAME=
DB_PASSWORD=
DB_HOST_NAME=
SOURCE_API_ENDPOINT=
AUTH_BEARER_TOKEN=
```
Go to the project working directory and build docker image.
```
docker-compose up --build -d
```
The above command creates three services:
- `etl` - script to perform ETL
- `db` - create postgres DB
- `pgadmin` - management tool for PostgreSQL
- `metabase` - visualization tool

### Perform DB migration
Uses alembic to perform DDL to create required schema and tables.
```
make make_migrate
```
Creates 
- Schema `std` and `dwh`
- Required tables on each schema

### Run ETL Pipeline
Update configs for extraction if required in `leave_mgmt/config/config.py`, the default values are:
```
BATCH_SIZE = 5000
START_DATE = "2021-07-17"
END_DATE = "2024-04-23"
```
```
docker-compose run etl python main.py
```
Link to access the following services:
| Service | URL   |
| :---:   | :---: |
| pgAdmin | http://localhost:5003 |
| Metabase| http://localhost:3000 |
