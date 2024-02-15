from fastapi import APIRouter

from .endpoints import resource_router, resource_status_router, downtime_router
router = APIRouter()
router.include_router(resource_router, tags=["resource"])
router.include_router(resource_status_router, tags=["resource status"])
router.include_router(downtime_router, tags=["downtime"])