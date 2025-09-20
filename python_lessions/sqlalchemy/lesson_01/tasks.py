"""
Tasks for Lesson 13 (SQLAlchemy ORM)
"""
from __future__ import annotations
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.engine import Engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name!r}, email={self.email!r})"


def get_engine(database_url: str) -> Engine:
    raise NotImplementedError


def create_schema(engine: Engine) -> None:
    raise NotImplementedError


def add_user(session, name: str, email: str) -> User:
    raise NotImplementedError


def get_user_by_email(session, email: str) -> Optional[User]:
    raise NotImplementedError
