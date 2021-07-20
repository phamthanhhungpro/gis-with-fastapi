from app.models.model import Diadiem
from fastapi import APIRouter

from app.api import home, diadiem, vector_tiles

api_router = APIRouter()
api_router.include_router(home.router, prefix="/home", tags=["Home"])
api_router.include_router(diadiem.router, prefix="/diadiem", tags=["diadiem"])
api_router.include_router(vector_tiles.router, prefix="/tms", tags=["mvt"])