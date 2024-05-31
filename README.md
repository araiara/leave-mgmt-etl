# Leave Management ETL

## Local Setup
### Using Docker
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
```
docker-compose run leave_mgmt_data_pipeline python main.py
```
Link to access the following services:
| Service | URL   |
| :---:   | :---: |
| pgAdmin | http://localhost:5003 |
| Metabase| http://localhost:3000 |
