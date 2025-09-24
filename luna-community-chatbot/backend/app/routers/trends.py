from fastapi import APIRouter
from ..services.trends import top_members, top_topics
from ..schemas import TrendOut


router = APIRouter(prefix="/trends", tags=["trends"])


@router.get("/", response_model=TrendOut)
async def get_trends():
return {"top_members": top_members(), "topics": top_topics()}