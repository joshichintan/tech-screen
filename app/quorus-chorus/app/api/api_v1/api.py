from fastapi import APIRouter

from app.api.api_v1.endpoints import payouts, users, songs

api_router = APIRouter()
api_router.include_router(payouts.router, prefix="/payouts", tags=["Payouts"])
api_router.include_router(songs.router, prefix="/songs", tags=["Songs"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
