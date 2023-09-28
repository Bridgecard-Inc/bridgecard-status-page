from src.model.issuing import UploadReward
from src.usecase.base_usecase import BaseUsecase
from src.service.issuing_service import IssuingService



class IssuingUsecase(BaseUsecase):
    def __init__(self, issuing_service: IssuingService):
        self.issuing_service = issuing_service
        super().__init__(issuing_service)

    def upload_rewards(self, data_in: UploadReward):

        res = self.issuing_service.upload_reward(payload=data_in.dict())

        return res
