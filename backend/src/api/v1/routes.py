from fastapi import APIRouter

from .endpoints import apis_router
router = APIRouter()
router.include_router(apis_router, tags=["apis"])