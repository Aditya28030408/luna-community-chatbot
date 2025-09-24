from fastapi import APIRouter, HTTPException
from ..schemas import PollCreate, PollVote
from ..services import polls as svc


router = APIRouter(prefix="/polls", tags=["polls"])


@router.post("/create")
async def create_poll(body: PollCreate):
pid = svc.create_poll(body.question, body.options)
return {"poll_id": pid}


@router.post("/vote")
async def vote(body: PollVote):
if not svc.get_poll(body.poll_id):
raise HTTPException(404, "Poll not found")
svc.vote(body.poll_id, body.option)
return {"ok": True, "poll": svc.get_poll(body.poll_id)}


@router.get("/{pid}")
async def get_poll(pid: str):
p = svc.get_poll(pid)
if not p: raise HTTPException(404, "Poll not found")
return p