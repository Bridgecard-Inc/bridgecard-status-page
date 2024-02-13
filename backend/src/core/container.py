from dependency_injector import containers, providers
from dependency_injector.wiring import Provide

from src.core.config import settings
from src.database.db import Database
from src.repository import *
from src.usecase import *



class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.v1.endpoints.apis",
            # "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, config=settings)
    
    apis_repository = providers.Factory(
        APIsRepository, db_session_factory=db.provided.session
    )

    apis_usecase = providers.Factory(APIsUsecase, apis_repository=apis_repository)


def expose_apis_usecase():

    db = Database(config=settings)
    
    apis_repository = APIsRepository(db_session_factory=db.session())

    apis_usecase = APIsUsecase(apis_repository=apis_repository)

    return apis_usecase
