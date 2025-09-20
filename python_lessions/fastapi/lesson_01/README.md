# Lesson 14: FastAPI Basics

In this lesson you will learn:
- App factory pattern (`create_app()`)
- Path and query parameters; validation with Pydantic models
- Response models and status codes
- Error handling with `HTTPException`
- Testing with `TestClient` (sync over async)
- (Preview) Dependencies and simple in-memory state

Best practices:
- Use app factory to keep tests isolated and configurable.
- Keep request/response models explicit; avoid leaking internals.
- Validate inputs with Pydantic; return proper status codes.

Endpoints to build (exercises):
1) `GET /health` -> `{ "status": "ok" }`.
2) `POST /items` -> create item with auto-increment id; returns `ItemOut`.
3) `GET /items/{item_id}` -> returns item or 404.
4) Bonus: `GET /items` -> list all items.

Testing hints:
- Use `TestClient(app)`; tests can remain synchronous.
- Assert both status code and response body.

Going further:
- Add dependency for DB session, integrate with SQLAlchemy models.
- Add pagination and filtering query params.
- Serve OpenAPI docs at `/docs` and `/redoc` (enabled by default).
