import requests
from pydantic import parse_obj_as

from leave_mgmt.config import ExtractConfig, Settings
from leave_mgmt.database import DB
from leave_mgmt.models import FlatFile
from leave_mgmt.pipeline.schema import LeaveEventSchema


class Extract:
    def __init__(self, config: Settings, db: DB, logger):
        self.db = db
        self.config = config
        self.logger = logger

    def fetch_records_from_api(self, api_url: str, bearer_token: str, batch_size: int, page: int) -> dict:
        query_params = {
            "fetchType": "all",
            "startDate": ExtractConfig.START_DATE.value,
            "endDate": ExtractConfig.END_DATE.value,
            "size": batch_size,
            "roleType": "issuer",
            "page": page,
        }

        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.get(api_url, headers=headers, params=query_params)

        if response.status_code == 200:
            payload = response.json()
            return payload
        else:
            self.logger.error(f"Request failed with status code {response.status_code}")

    def run_extraction(self) -> None:
        """
        Fetch data from API and store to raw flatfile.
        """
        page = 1
        batch_size = ExtractConfig.BATCH_SIZE.value
        total_fetched_data_size = 0
        api_url = self.config.source_api_endpoint
        bearer_token = self.config.auth_bearer_token

        while True:
            payload = self.fetch_records_from_api(api_url, bearer_token, batch_size, page)
            total_data_size = payload.get("meta", {}).get("total", 0)
            fetched_data_size = payload.get("meta", {}).get("size", 0)

            # batch insertion
            leave_records = parse_obj_as(list[LeaveEventSchema], payload["data"])
            self.logger.info(f"Insert {batch_size=}.")
            self.insert_into_raw_flatfile(leave_records)

            page += 1
            total_fetched_data_size += fetched_data_size

            if total_fetched_data_size == total_data_size:
                break

    def insert_into_raw_flatfile(self, leave_records: list[LeaveEventSchema]) -> None:
        """
        Insert record into raw flatfile table.
        """
        with self.db.session_scope() as session:
            for leave_record in leave_records:
                record = FlatFile(**leave_record.dict())
                session.add(record)
            self.logger.info("[EXTRACT] Record extracted successfully.")
