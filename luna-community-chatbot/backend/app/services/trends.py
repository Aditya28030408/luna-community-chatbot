from collections import Counter
from typing import List


_topics = Counter()
_members = Counter()


def ingest_message(user: str, text: str):
_members[user] += 1
for w in text.lower().split():
if w.isalpha() and len(w) > 4:
_topics[w] += 1


def top_members(n=5):
return [u for u, _ in _members.most_common(n)]


def top_topics(n=5):
return [t for t, _ in _topics.most_common(n)]