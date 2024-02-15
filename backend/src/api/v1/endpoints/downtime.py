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
from src.usecase.downtime_usecase import DowntimeUsecase


# core imports
from src.core.config import settings
from src.core.error import InvalidToken, MissingPermission, MissingResource
from src.core.container import Container, expose_downtime_usecase

# crud imports

# model imports
from src.model.downtime import DowntimeIn

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

router = APIRouter(prefix="/downtime")


@router.post("/", status_code=200)
@version(1)
@inject
async def add_downtime(
    data_in: DowntimeIn,
    usecase: DowntimeUsecase = Depends(expose_downtime_usecase),
):
    res = usecase.add_downtime(data_in)

    if not res:

        return JSONResponse(
            status_code=400,
            content={
                "status": "failed",
                "message": "Unsuccessful, unable to create downtime",
            },
        )

    return {
        "status": "success",
        "message": "Downtime created sucessfully",
    }


@router.get("/", status_code=200)
@version(1)
@inject
async def fetch_all_downtimes(
    usecase: DowntimeUsecase = Depends(expose_downtime_usecase),
):
    res = usecase.fetch_all_downtimes()

    if not res and type(res) is not list:

        return JSONResponse(
            status_code=400,
            content={
                "status": "failed",
                "message": "Unsuccessful, unable to fetch all downtimes",
            },
        )

    return {
        "status": "success",
        "message": "Downtimes fetched sucessfully",
        "data": {
            "downtimes": res,
        },
    }


@router.patch("/{downtime_id}", status_code=200)
@version(1)
@inject
async def update_downtime(
    downtime_id: str,
    data_in: DowntimeIn,
    usecase: DowntimeUsecase = Depends(expose_downtime_usecase),
):
    res = usecase.update_downtime(downtime_id=downtime_id, update_schema=data_in)

    if not res:

        return JSONResponse(
            status_code=400,
            content={
                "status": "failed",
                "message": "Unsuccessful, unable to update downtime",
            },
        )

    return {
        "status": "success",
        "message": "Downtime updated sucessfully",
    }
