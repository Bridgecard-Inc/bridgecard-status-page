from src.model.resource import ResourceIn
from src.usecase.base_usecase import BaseUsecase
from src.repository.resource_status_repository import ResourceStatusRepository


class ResourceStatusUsecase(BaseUsecase):
    def __init__(self, resource_status_repository: ResourceStatusRepository):
        self.resource_status_repository = resource_status_repository
        super().__init__(resource_status_repository)

    def add_resource_status_after_monitoring(self, data_in: ResourceIn):

        return self.resource_status_repository.create(data_in, context=None)
