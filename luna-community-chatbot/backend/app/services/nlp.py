from transformers import pipeline
from typing import List, Tuple
import os


LABELS = [
"announcement", "important", "spam", "casual", "greeting"
]


_classifier = None
_summarizer = None


def get_classifier():
global _classifier
if _classifier is None:
model = os.getenv("HF_MODEL", "distilbert-base-uncased")
_classifier = pipeline("text-classification", model=model, return_all_scores=True, truncation=True)
return _classifier


def get_summarizer():
global _summarizer
if _summarizer is None:
model = os.getenv("SUMMARIZER_MODEL", "facebook/bart-large-cnn")
_summarizer = pipeline("summarization", model=model)
return _summarizer


def classify_messages(msgs: List[str]) -> Tuple[List[str], List[float]]:
clf = get_classifier()
labels, scores = [], []
for m in msgs:
# Map model labels to our set via max score; if custom fine-tuned model is used, ensure label names match
preds = clf(m)[0]
best = max(preds, key=lambda x: x["score"]) # type: ignore
labels.append(best["label"].lower())
scores.append(float(best["score"]))
return labels, scores


def summarize_text(text: str, max_words: int = 120) -> str:
s = get_summarizer()
# approx tokens:words ~ 1.3; keep safe margin
max_len = max(32, min(180, int(max_words * 1.3)))
out = s(text, max_length=max_len, min_length=32, do_sample=False)[0]["summary_text"]
return out