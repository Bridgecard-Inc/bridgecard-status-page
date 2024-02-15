from dependency_injector import containers, providers
from dependency_injector.wiring import Provide

from src.core.config import settings
from src.database.db import Database
from src.repository import *
from src.usecase import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.v1.endpoints.resource",
            # "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, config=settings)

    apis_repository = providers.Factory(
        ResourceRepository, db_session_factory=db.provided.session
    )

    apis_usecase = providers.Factory(ResourceUsecase, apis_repository=apis_repository)


def expose_resource_usecase():

    db = Database(config=settings)

    resource_repository = ResourceRepository(db_session_factory=db.session)

    resource_usecase = ResourceUsecase(resource_repository=resource_repository)

    return resource_usecase


def expose_resource_status_usecase():

    db = Database(config=settings)

    resource_status_repository = ResourceStatusRepository(db_session_factory=db.session)

    resource_status_usecase = ResourceStatusUsecase(
        resource_status_repository=resource_status_repository
    )

    return resource_status_usecase


def expose_downtime_usecase():

    db = Database(config=settings)

    downtime_repository = DowntimeRepository(db_session_factory=db.session)

    resource_status_repository = ResourceStatusRepository(db_session_factory=db.session)

    downtime_usecase = DowntimeUsecase(
        downtime_repository=downtime_repository,
        resource_status_repository=resource_status_repository,
    )

    return downtime_usecase
