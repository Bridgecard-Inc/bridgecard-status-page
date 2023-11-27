from dependency_injector import containers, providers
from dependency_injector.wiring import Provide

from src.core.config import settings
from src.database.db import Database
from src.repository import *
from src.usecase import *
from src.utils.constants import BRIDGECARD_ISSUING_SERVICE_BASE_URL


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.v1.endpoints.apis",
            # "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, config=settings)
    
    urls_repository = providers.Factory(
        APIsRepository, db_session_factory=db.provided.session
    )

    urls_usecase = providers.Factory(APIsUsecase, urls_repository=urls_repository)


def expose_urls_usecase():

    db = providers.Singleton(Database, config=settings)
    
    urls_repository = providers.Factory(
        APIsRepository, db_session_factory=db.provided.session
    )

    apis_usecase = APIsUsecase(urls_repository=urls_repository)

    return apis_usecase
