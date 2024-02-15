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
from src.usecase.resource_usecase import ResourceUsecase


# core imports
from src.core.config import settings
from src.core.error import InvalidToken, MissingPermission, MissingResource
from src.core.container import Container, expose_resource_usecase

# crud imports

# model imports
from src.model.resource import ResourceIn

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

router = APIRouter(prefix="/resource")


@router.post("/", status_code=200)
@version(1)
@inject
async def add_resource(
    data_in: ResourceIn,
    usecase: ResourceUsecase = Depends(expose_resource_usecase),
):
    res = usecase.add_resource_for_monitoring(data_in)

    if not res:

        return JSONResponse(
            status_code=400,
            content={
                "status": "failed",
                "message": "Unsuccessful, unable to create resource",
            },
        )

    return {
        "status": "success",
        "message": "Resource created sucessfully",
    }


@router.get("/", status_code=200)
@version(1)
@inject
async def fetch_all_resources(
    usecase: ResourceUsecase = Depends(expose_resource_usecase),
):
    res = usecase.fetch_all_resources()

    if not res and type(res) is not list:

        return JSONResponse(
            status_code=400,
            content={
                "status": "failed",
                "message": "Unsuccessful, unable to fetch all resources",
            },
        )

    return {
        "status": "success",
        "message": "Resources fetched sucessfully",
        "data": {
            "resources": res,
        },
    }
