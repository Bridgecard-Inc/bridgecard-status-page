from src.model.api import APITOMONITOR
from src.usecase.base_usecase import BaseUsecase
from src.repository.apis_repository import APIsRepository



class APIsUsecase(BaseUsecase):
    def __init__(self, apis_repository: APIsRepository):
        self.apis_repository = apis_repository
        super().__init__(apis_repository)

    def add_api_for_monitoring(self, data_in: APITOMONITOR):

      # Use the create method from the repository to add an API to the database
        created = self.apis_repository.create(data_in.api_id, data_in)

        if created:
            return "API added successfully"
        else:
            return "Failed to add API"
