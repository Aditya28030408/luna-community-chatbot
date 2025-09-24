from fastapi import APIRouter
from ..services.roles import get_role, leaderboard, add_activity


router = APIRouter(prefix="/roles", tags=["roles"])


@router.get("/{user}")
async def get_user_role(user: str):
return {"user": user, "role": get_role(user)}


@router.get("/leaderboard/top")
async def get_leaderboard():
return {"leaderboard": leaderboard()}


@router.post("/activity/{user}")
async def add_user_activity(user: str):
add_activity(user)
return {"ok": True}