"""
Tasks for Lesson 02 (Advanced Request Handling)
"""
from __future__ import annotations
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel, EmailStr, validator
from typing import List, Dict, Any, Optional
import csv
import io


class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v

    @validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v


class BulkDataItem(BaseModel):
    id: int
    name: str
    value: float


app = FastAPI()


@app.post("/register")
async def register_user(user_data: UserRegistration) -> Dict[str, Any]:
    raise NotImplementedError


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)) -> Dict[str, Any]:
    raise NotImplementedError


@app.post("/bulk-process")
async def bulk_process_data(items: List[BulkDataItem]) -> Dict[str, Any]:
    raise NotImplementedError


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> Dict[str, Any]:
    raise NotImplementedError


@app.put("/users/{user_id}")
async def update_user(user_id: int, user_data: Dict[str, Any]) -> Dict[str, Any]:
    raise NotImplementedError


