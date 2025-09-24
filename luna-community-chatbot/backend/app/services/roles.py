from collections import defaultdict
from typing import Dict


# toy scoring for demo
_scores: Dict[str, int] = defaultdict(int)


ROLE_RULES = [
("Legend", 200),
("Mentor", 120),
("Contributor", 60),
("Newbie", 0),
]


def add_activity(user: str, points: int = 5):
_scores[user] += points


def get_role(user: str) -> str:
s = _scores.get(user, 0)
for name, thr in ROLE_RULES:
if s >= thr:
return name
return "Newbie"


def leaderboard(top: int = 10):
return sorted(_scores.items(), key=lambda x: x[1], reverse=True)[:top]