from src.model.downtime import DowntimeIn
from src.repository.resource_status_repository import ResourceStatusRepository
from src.usecase.base_usecase import BaseUsecase
from src.repository.downtime_repository import DowntimeRepository


class DowntimeUsecase(BaseUsecase):
    def __init__(
        self,
        downtime_repository: DowntimeRepository,
        resource_status_repository: ResourceStatusRepository,
    ):
        self.downtime_repository = downtime_repository

        self.resource_status_repository = resource_status_repository

        super().__init__(downtime_repository)

    def add_downtime(self, data_in: DowntimeIn):

        new_result = self.downtime_repository.create(data_in, context=None)

        downtime_id = str(new_result["_id"])

        if new_result:

            return self.resource_status_repository.update_downtime_id_on_affected_failed_resource_status(
                downtime_id=downtime_id, schema=data_in, context=None
            )

        return None

    def fetch_all_downtimes(self):

        return self.downtime_repository.fetch_all(context=None)

    def update_downtime(self, downtime_id: str, update_schema):

        new_result = self.downtime_repository.update(
            document_id=downtime_id, schema=update_schema, context=None
        )

        if new_result:

            return self.resource_status_repository.update_downtime_id_on_affected_failed_resource_status(
                downtime_id=downtime_id, schema=update_schema, context=None
            )

        return None
