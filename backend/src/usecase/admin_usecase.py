from src.model.admin import AdminLoginIn, AdminIn
from src.usecase.base_usecase import BaseUsecase
from src.repository.admin_repository import AdminRepository

from src.core.config import settings

from src.utils.auth import create_access_token


class AdminUsecase(BaseUsecase):
    def __init__(self, admin_repository: AdminRepository):
        self.admin_repository = admin_repository
        super().__init__(admin_repository)

    def login_admin(self, data_in: AdminLoginIn):

        if (
            data_in.password == settings.SUPERADMIN_PASSWORD
            and data_in.username == settings.SUPERADMIN_USERNAME
        ):

            encoded_jwt = create_access_token(data=data_in.dict())

            return encoded_jwt

    def update_admin(self, id: str, data_in: AdminIn):

        return self.admin_repository.update(id=id, schema=data_in, context=None)

    def fetch_admin(self, id: str):

        return self.admin_repository.read_admin_by_id(id=id, context=None)
