from fastapi import APIRouter
from ..schemas import ClassifyIn, ClassifyOut
from ..services.nlp import classify_messages
from ..services.trends import ingest_message


router = APIRouter(prefix="/classify", tags=["classification"])


@router.post("/", response_model=ClassifyOut)
async def classify(body: ClassifyIn):
labels, scores = classify_messages(body.messages)
for msg in body.messages:
ingest_message("user", msg) # replace with real user id
return ClassifyOut(labels=labels, scores=scores)