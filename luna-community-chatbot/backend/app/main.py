from fastapi import FastAPI
from .deps import add_cors
from .routers import classify, summarize, polls, roles, trends
from .ws import hub


app = FastAPI(title="Luna API", version="0.1.0")
add_cors(app)


app.include_router(classify.router)
app.include_router(summarize.router)
app.include_router(polls.router)
app.include_router(roles.router)
app.include_router(trends.router)
app.include_router(hub.router)


@app.get("/")
async def root():
return {"ok": True, "service": "luna"}