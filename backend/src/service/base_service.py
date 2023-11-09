from src.service.api_helper import ApiHelper


class BaseService:
    def __init__(self, token, base_url) -> None:
        self.api_helper = ApiHelper(token=token)
        self.base_url = base_url
        self.base_url = base_url
