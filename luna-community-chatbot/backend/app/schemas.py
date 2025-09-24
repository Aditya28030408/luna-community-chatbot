from pydantic import BaseModel
from typing import List, Optional, Dict


class ClassifyIn(BaseModel):
messages: List[str]


class ClassifyOut(BaseModel):
labels: List[str]
scores: List[float]


class SummarizeIn(BaseModel):
text: str
max_words: int = 120


class SummarizeOut(BaseModel):
summary: str


class PollCreate(BaseModel):
question: str
options: List[str]


class PollVote(BaseModel):
poll_id: str
option: int


class TrendOut(BaseModel):
top_members: List[str]
topics: List[str]