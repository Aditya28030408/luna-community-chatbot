from fastapi import APIRouter
from ..schemas import SummarizeIn, SummarizeOut
from ..services.nlp import summarize_text


router = APIRouter(prefix="/summarize", tags=["summarization"])


@router.post("/", response_model=SummarizeOut)
async def summarize(body: SummarizeIn):
return SummarizeOut(summary=summarize_text(body.text, body.max_words))