"""
Lesson 14: FastAPI Basics
"""
from __future__ import annotations
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class ItemIn(BaseModel):
    name: str
    price: float

class ItemOut(ItemIn):
    id: int


def create_demo_app() -> FastAPI:
    app = FastAPI()
    storage = {}
    next_id = {"v": 0}

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.post("/items", response_model=ItemOut)
    def create_item(item: ItemIn):
        next_id["v"] += 1
        data = ItemOut(id=next_id["v"], **item.dict())
        storage[data.id] = data
        return data

    @app.get("/items/{item_id}", response_model=ItemOut)
    def get_item(item_id: int):
        if item_id not in storage:
            raise HTTPException(status_code=404, detail="not found")
        return storage[item_id]

    return app


if __name__ == "__main__":
    uvicorn.run(create_demo_app(), host="127.0.0.1", port=8001)
