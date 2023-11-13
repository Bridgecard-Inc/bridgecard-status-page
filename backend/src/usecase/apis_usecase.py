from src.model.api import API_TO_MONITOR
from src.usecase.base_usecase import BaseUsecase
from src.repository.apis_repository import APIsRepository



class APIsUsecase(BaseUsecase):
    def __init__(self, apis_repository: APIsRepository):
        self.apis_repository = apis_repository
        super().__init__(apis_repository)

    def add_api_for_monitoring(self, data_in: API_TO_MONITOR):

        return 
