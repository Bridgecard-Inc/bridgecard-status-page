from dependency_injector import containers, providers
from dependency_injector.wiring import Provide

from src.core.config import settings
from src.database.db import Database
from src.repository import *
from src.usecase import *
from src.service import *
from src.utils.constants import BRIDGECARD_ISSUING_SERVICE_BASE_URL


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.v1.endpoints.issuing",
            # "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, config=settings)

    issuing_service = providers.Factory(
        IssuingService,
        token=settings.BRIDGECARD_ISSUING_LIVE_AUTHORIZATION_TOKEN,
        base_url=BRIDGECARD_ISSUING_SERVICE_BASE_URL,
    )

    issuing_usecase = providers.Factory(IssuingUsecase, issuing_service=issuing_service)


def expose_issuing_usecase():
    
    issuing_service = IssuingService(
        token=settings.BRIDGECARD_ISSUING_LIVE_AUTHORIZATION_TOKEN,
        base_url=BRIDGECARD_ISSUING_SERVICE_BASE_URL,
    )

    issuing_usecase = IssuingUsecase(issuing_service=issuing_service)

    return issuing_usecase
