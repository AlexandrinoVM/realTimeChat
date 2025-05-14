from fastapi import WebSocket
from typing import Dict,List

class ConnectionManager:
    def __init__(self):
        self.active_connection: Dict[str,List[WebSocket]] ={}
    
    async def connetion(self,room_id:int,websocket:WebSocket):
        await websocket.accept()
        if room_id not in self.active_connection:
            self.active_connection[room_id] = []
        self.active_connection[room_id].append(websocket)

    async def disconnect(self,room_id:int,websocket:WebSocket):
        self.active_connection[room_id].remove(websocket)
        if not self.active_connection[room_id]:
            del self.active_connection[room_id]

    async def broadcast(self,room_id:str,message:str):
         for connection in self.active_connection.get(room_id, []):
            try:
                await connection.send_text(message)
            except RuntimeError:
                pass