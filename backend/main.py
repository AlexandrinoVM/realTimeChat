import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from backend.database import Base,db
from typing import Union
from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from backend.router import UserRouter,RoomRouter,MessageRouter,AuthRouter
from fastapi.middleware.cors import CORSMiddleware
from backend.utils import ConnectionManager

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


manager = ConnectionManager()

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=db)

app.include_router(UserRouter)
app.include_router(RoomRouter)
app.include_router(MessageRouter)
app.include_router(AuthRouter)

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket:WebSocket,room_id:int,):
    await manager.connetion(room_id,websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(room_id,f"room {room_id}:{data}")
    except WebSocketDisconnect:
        await manager.broadcast(room_id,"um usuario saiu da sala")
        await manager.disconnect(room_id,websocket)