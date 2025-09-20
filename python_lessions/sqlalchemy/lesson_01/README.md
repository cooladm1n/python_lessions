# Lesson 13: SQLAlchemy ORM Basics (SQLite)

In this lesson you will learn:
- Engines, connections and `sessionmaker`
- Declarative models, columns, constraints, indexes
- Creating tables (`Base.metadata.create_all`)
- CRUD: insert, select, update, delete
- Query building: filtering, ordering, limits
- Transactions: commit/rollback patterns and error handling
- Uniqueness constraints and exceptions
- (Preview) Relationships, eager vs lazy loading

Best practices:
- Keep a single `Engine` per DB per process; create short‑lived `Session`s.
- Handle integrity errors explicitly for better UX.
- Use `String(length)`, `unique=True`, `index=True` where appropriate.
- Prefer explicit queries over raw SQL for maintainability.

Quickstart
1) Create engine: `get_engine("sqlite+pysqlite:///:memory:")`
2) Create schema: `create_schema(engine)`
3) Use `Session(engine)` context to interact with DB

Core APIs to know
- `Mapped[...]`, `mapped_column`, `String`, `Integer`, constraints
- `session.add`, `session.add_all`, `session.flush`, `session.commit`, `session.rollback`
- `select(User)`, `session.execute(stmt)`, `.scalars().first()`

Exercises:
1) Implement `get_engine(database_url)` that returns an SQLAlchemy `Engine` with future mode (SQLAlchemy 2.x defaults are fine).
2) Implement `create_schema(engine)` that creates tables for the models.
3) Implement `add_user(session, name, email)` that inserts a user and returns it. Ensure that `id` is populated (flush or commit).
4) Implement `get_user_by_email(session, email)` that returns a `User` or `None`.
5) Bonus: Add a query to return all users ordered by name (not required by tests, but try it in REPL).

Common pitfalls:
- Forgetting to `commit()` after writes (data not persisted).
- Assuming `id` exists without flushing/committing.
- Catching too broad exceptions; prefer SQLAlchemy integrity errors.

Going further:
- Add a `Post` model with `relationship('User')` and a foreign key; explore lazy/eager loading.
- Use Alembic for migrations; separate models and DB config into modules.
