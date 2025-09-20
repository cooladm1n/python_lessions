"""
Lesson 13: SQLAlchemy ORM Basics
"""
from __future__ import annotations
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from tasks import Base, User, get_engine, create_schema, add_user, get_user_by_email

engine = get_engine("sqlite+pysqlite:///:memory:")
create_schema(engine)

# Insert + commit
with Session(engine) as session:
    u = add_user(session, name="Alice", email="alice@example.com")
    session.commit()

# Read
with Session(engine) as session:
    got = get_user_by_email(session, "alice@example.com")
    print("fetched:", got)

# Unique constraint demo
with Session(engine) as session:
    try:
        add_user(session, name="Alice2", email="alice@example.com")
        session.commit()
    except IntegrityError as e:
        session.rollback()
        print("integrity error:", type(e).__name__)
