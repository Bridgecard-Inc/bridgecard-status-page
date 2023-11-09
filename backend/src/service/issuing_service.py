from typing import Dict
from src.service.base_service import BaseService


class IssuingService(BaseService):
    def __init__(self, token, base_url):
        super().__init__(token, base_url)

    def upload_reward(self, payload: Dict):

        url = self.base_url + "/v1/issuing/reward/upload_reward"

        response_code, response_data = self.api_helper.post(
            url=url, data=payload
        )

        if response_code == 201:
            return response_data["data"]

        elif response_code == 400:
            return False

        else:
            return False
