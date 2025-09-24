from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter()


@router.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
await ws.accept()
try:
while True:
data = await ws.receive_text()
await ws.send_text(data) # echo demo; extend to broadcast
except WebSocketDisconnect:
pass