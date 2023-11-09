from fastapi import APIRouter

from .endpoints import urls_router
router = APIRouter()
router.include_router(urls_router, tags=["urls"])