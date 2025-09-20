"""
Tasks for Lesson 14 (FastAPI)
"""
from __future__ import annotations
from typing import Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class ItemIn(BaseModel):
    name: str
    price: float


class ItemOut(ItemIn):
    id: int


def create_app() -> FastAPI:
    raise NotImplementedError
