from enum import Enum

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_name: str
    db_port: int
    db_username: str
    db_password: str
    db_host_name: str
    source_api_endpoint: str
    auth_bearer_token: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class SqlDirPaths(str, Enum):
    TRANSFORM_SQL_DIR = "leave_mgmt/sql/transform"
    LOAD_SQL_DIR = "leave_mgmt/sql/load"


class ExtractConfig(Enum):
    BATCH_SIZE = 5000
    START_DATE = "2021-07-17"
    END_DATE = "2024-04-23"


__all__ = ["Settings", "SqlDirPaths", "ExtractConfig"]
