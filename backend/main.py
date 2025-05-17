import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)
import json
from backend.database import Base,db
from typing import Union
from sqlalchemy.orm import Session
from fastapi import FastAPI,WebSocket,WebSocketDisconnect,Depends
from backend.database import get_db,SessionLocal
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from backend.router import UserRouter,RoomRouter,MessageRouter,AuthRouter
from fastapi.middleware.cors import CORSMiddleware
from backend.utils import ConnectionManager
from backend.service import CreateMessage,GetUserById
from backend.schemas import Message

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
async def websocket_endpoint(websocket:WebSocket,room_id:int):
    await manager.connetion(room_id,websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_dict = json.loads(data)
            db:Session = SessionLocal()
            message_data = Message(**message_dict)
            saved_message = CreateMessage(message_data,db)
            user = GetUserById(saved_message.user,db)
            await manager.broadcast(room_id,f"{user.user}:{saved_message.content}")
    except WebSocketDisconnect:
        await manager.disconnect(room_id,websocket)

@app.get("/chat/connection/{room_id}")
async def get_connections(room_id:int):
    return manager.count(room_id)