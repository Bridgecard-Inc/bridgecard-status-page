from src.model.resource import ResourceIn
from src.usecase.base_usecase import BaseUsecase
from src.repository.resource_repository import ResourceRepository


class ResourceUsecase(BaseUsecase):
    def __init__(self, resource_repository: ResourceRepository):
        self.resource_repository = resource_repository
        super().__init__(resource_repository)

    def add_resource_for_monitoring(self, data_in: ResourceIn):

        return self.resource_repository.create(data_in, context=None)

    def fetch_all_resources(self):

        return self.resource_repository.fetch_all(context=None)
