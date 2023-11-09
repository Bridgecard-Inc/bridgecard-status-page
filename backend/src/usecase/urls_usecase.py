from src.model.issuing import UploadReward
from src.usecase.base_usecase import BaseUsecase
from src.repository.urls_repository import UrlsRepository



class UrlsUsecase(BaseUsecase):
    def __init__(self, urls_repository: UrlsRepository):
        self.urls_repository = urls_repository
        super().__init__(urls_repository)

    def upload_rewards(self, data_in: UploadReward):

        return 
