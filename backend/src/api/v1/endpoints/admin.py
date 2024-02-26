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
from src.usecase.admin_usecase import AdminUsecase


# core imports
from src.core.config import settings
from src.core.error import InvalidToken, MissingPermission, MissingResource
from src.core.container import Container, expose_admin_usecase
from src.core import error

# crud imports

# model imports
from src.model.admin import AdminIn, AdminSettingsIn
from src.utils.auth import verify_access_token

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

router = APIRouter(prefix="/admin")


@router.post("/login", status_code=200)
@version(1)
@inject
async def login_admin(
    data_in: AdminIn,
    usecase: AdminUsecase = Depends(expose_admin_usecase),
):
    res = usecase.login_admin(data_in)

    if not res:

        raise error.InvalidLogin

    return {
        "status": "success",
        "message": "Admin logged in sucessfully",
        "data": {"access_token": res},
    }


@router.get("/", status_code=200)
@version(1)
@inject
async def fetch_admin(
    usecase: AdminUsecase = Depends(expose_admin_usecase),
    username: str = Depends(verify_access_token),
):
    res = usecase.fetch_admin(id=username)

    return {
        "status": "success",
        "message": "Admin fetched sucessfully",
        "data": {"admin": res},
    }


@router.patch("/", status_code=200)
@version(1)
@inject
async def update_admin_settings(
    data_in: AdminSettingsIn,
    usecase: AdminUsecase = Depends(expose_admin_usecase),
    username: str = Depends(verify_access_token),
):
    res = usecase.update_admin(id=username, data_in=data_in)

    if not res:

        return JSONResponse(
            status_code=400,
            content={
                "status": "failed",
                "message": "Unsuccessful, unable to update admin",
            },
        )

    return {
        "status": "success",
        "message": "Admin updated sucessfully",
    }
