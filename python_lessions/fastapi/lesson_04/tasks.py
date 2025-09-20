"""
Tasks for Lesson 04 (Database Integration)
"""
from __future__ import annotations
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

# Database setup
Base = declarative_base()
engine = create_engine("sqlite:///./test.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# Pydantic models
class UserCreate(BaseModel):
    username: str
    email: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DatabaseManager:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserCreate) -> User:
        raise NotImplementedError

    def get_user(self, user_id: int) -> Optional[User]:
        raise NotImplementedError

    def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        raise NotImplementedError

    def update_user(self, user_id: int, user_data: UserCreate) -> Optional[User]:
        raise NotImplementedError

    def delete_user(self, user_id: int) -> bool:
        raise NotImplementedError


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.db_manager = DatabaseManager(db)

    def create_user(self, user_data: UserCreate) -> UserResponse:
        raise NotImplementedError

    def get_user(self, user_id: int) -> UserResponse:
        raise NotImplementedError

    def get_users(self, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        raise NotImplementedError

    def update_user(self, user_id: int, user_data: UserCreate) -> UserResponse:
        raise NotImplementedError

    def delete_user(self, user_id: int) -> bool:
        raise NotImplementedError


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        raise NotImplementedError

    def get_product(self, product_id: int) -> ProductResponse:
        raise NotImplementedError

    def get_products(self, skip: int = 0, limit: int = 100) -> List[ProductResponse]:
        raise NotImplementedError

    def update_product(self, product_id: int, product_data: ProductCreate) -> ProductResponse:
        raise NotImplementedError

    def delete_product(self, product_id: int) -> bool:
        raise NotImplementedError


# FastAPI app
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)


@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    raise NotImplementedError


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    raise NotImplementedError


@app.get("/users/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raise NotImplementedError


@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    raise NotImplementedError


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    raise NotImplementedError


@app.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    raise NotImplementedError


@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    raise NotImplementedError


@app.get("/products/", response_model=List[ProductResponse])
async def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raise NotImplementedError


