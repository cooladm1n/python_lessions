import pytest
from sqlalchemy.orm import Session
from tasks import get_engine, create_schema, Base, User, add_user, get_user_by_email


def test_crud_in_memory():
    engine = get_engine("sqlite+pysqlite:///:memory:")
    create_schema(engine)

    with Session(engine) as session:
        u = add_user(session, "Bob", "bob@example.com")
        session.commit()

    with Session(engine) as session:
        got = get_user_by_email(session, "bob@example.com")
        assert isinstance(got, User)
        assert got.name == "Bob"


def test_unique_email():
    engine = get_engine("sqlite+pysqlite:///:memory:")
    create_schema(engine)
    with Session(engine) as session:
        add_user(session, "A", "a@example.com")
        session.commit()
        with pytest.raises(Exception):
            add_user(session, "B", "a@example.com")
            session.commit()
