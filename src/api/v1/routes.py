from fastapi import APIRouter

from .endpoints import issuing_router
router = APIRouter()
router.include_router(issuing_router, tags=["issuing"])