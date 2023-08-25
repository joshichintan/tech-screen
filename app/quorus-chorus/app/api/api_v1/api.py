from app.api.api_v1.endpoints import login, payouts, songs, users
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(payouts.router, prefix="/payouts", tags=["Payouts"])
api_router.include_router(songs.router, prefix="/songs", tags=["Songs"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
