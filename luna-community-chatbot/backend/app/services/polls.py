from typing import Dict, List
from uuid import uuid4


# In-memory for demo; replace with DB
_POLLS: Dict[str, Dict] = {}


def create_poll(question: str, options: List[str]) -> str:
pid = str(uuid4())
_POLLS[pid] = {"q": question, "opt": options, "votes": [0]*len(options)}
return pid


def vote(pid: str, idx: int):
if pid in _POLLS and 0 <= idx < len(_POLLS[pid]["votes"]):
_POLLS[pid]["votes"][idx] += 1


def get_poll(pid: str):
return _POLLS.get(pid)