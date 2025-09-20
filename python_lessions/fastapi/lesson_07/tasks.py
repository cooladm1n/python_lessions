"""
Tasks for Lesson 07 (WebSocket Integration)
"""
from __future__ import annotations
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict, Any, List, Optional
import json
import asyncio
from datetime import datetime


class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.connection_metadata: Dict[WebSocket, Dict[str, Any]] = {}

    async def connect(self, websocket: WebSocket, client_id: str) -> None:
        raise NotImplementedError

    async def disconnect(self, websocket: WebSocket) -> None:
        raise NotImplementedError

    async def send_personal_message(self, message: str, websocket: WebSocket) -> None:
        raise NotImplementedError

    async def broadcast(self, message: str) -> None:
        raise NotImplementedError

    def get_connection_count(self) -> int:
        raise NotImplementedError

    def get_connection_info(self, websocket: WebSocket) -> Optional[Dict[str, Any]]:
        raise NotImplementedError


class ChatRoom:
    def __init__(self, room_id: str):
        self.room_id = room_id
        self.messages: List[Dict[str, Any]] = []
        self.participants: List[WebSocket] = []
        self.message_history_limit = 100

    async def add_participant(self, websocket: WebSocket, username: str) -> None:
        raise NotImplementedError

    async def remove_participant(self, websocket: WebSocket) -> None:
        raise NotImplementedError

    async def send_message(self, websocket: WebSocket, message: str, username: str) -> None:
        raise NotImplementedError

    def get_message_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def get_participant_count(self) -> int:
        raise NotImplementedError


class NotificationService:
    def __init__(self):
        self.notifications: List[Dict[str, Any]] = []
        self.user_subscriptions: Dict[str, List[WebSocket]] = {}

    async def send_notification(self, user_id: str, message: str, notification_type: str = "info") -> None:
        raise NotImplementedError

    async def subscribe_user(self, user_id: str, websocket: WebSocket) -> None:
        raise NotImplementedError

    async def unsubscribe_user(self, user_id: str, websocket: WebSocket) -> None:
        raise NotImplementedError

    def get_notification_history(self, user_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        raise NotImplementedError


# FastAPI app
app = FastAPI()

# WebSocket manager
websocket_manager = WebSocketManager()

# Chat rooms
chat_rooms: Dict[str, ChatRoom] = {}

# Notification service
notification_service = NotificationService()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket_manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            if message_data.get("type") == "chat":
                room_id = message_data.get("room_id")
                message = message_data.get("message")
                username = message_data.get("username")
                
                if room_id in chat_rooms:
                    await chat_rooms[room_id].send_message(websocket, message, username)
            
            elif message_data.get("type") == "notification":
                user_id = message_data.get("user_id")
                message = message_data.get("message")
                notification_type = message_data.get("notification_type", "info")
                
                await notification_service.send_notification(user_id, message, notification_type)
    
    except WebSocketDisconnect:
        await websocket_manager.disconnect(websocket)


@app.post("/chat/rooms/{room_id}/join")
async def join_chat_room(room_id: str, username: str):
    raise NotImplementedError


@app.get("/chat/rooms/{room_id}/messages")
async def get_chat_messages(room_id: str, limit: int = 50):
    raise NotImplementedError


@app.post("/notifications/send")
async def send_notification(user_id: str, message: str, notification_type: str = "info"):
    raise NotImplementedError


@app.get("/notifications/{user_id}")
async def get_user_notifications(user_id: str, limit: int = 50):
    raise NotImplementedError


