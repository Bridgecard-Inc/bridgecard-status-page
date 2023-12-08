# internal lib imports
import asyncio
from base64 import b64encode
import json
import os
import logging
from datetime import datetime
import uuid
from dependency_injector.wiring import Provide, inject

# external lib imports
from typing import List, Optional

# fast api imports
from fastapi_versioning import version
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Header, Depends, Request, BackgroundTasks
from src.usecase.apis_usecase import APIsUsecase


# core imports
from src.core.config import settings
from src.core.error import InvalidToken, MissingPermission, MissingResource
from src.core.container import Container, expose_urls_usecase

# crud imports

# model imports
from src.model.api import APITOMONITOR

# schema imports

# utils imports


logger = logging.getLogger(__name__)
# create logger with log app
real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)
LOGFILE = "src/logs/test.log"
# logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(LOGFILE)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

router = APIRouter(prefix="/apis-monitoring")


@router.post("/add-api", status_code=200)
@version(1)
@inject
async def add_api(
    data_in: APITOMONITOR,
    usecase: APIsUsecase = Depends(expose_urls_usecase),
):
    add_api_for_monitoring = usecase.add_api_for_monitoring(data_in)

    if not add_api_for_monitoring:
        return JSONResponse(
            status_code=400,
            content={
                "status": "failed",
                "message": "Unsuccessful, unable to upload reward",
            },
        )

    return {
        "status": "success",
        "message": "Reward uploaded sucessfully",
    }
