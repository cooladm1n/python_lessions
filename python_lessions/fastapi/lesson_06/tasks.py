"""
Tasks for Lesson 06 (Middleware and Background Tasks)
"""
from __future__ import annotations
from fastapi import FastAPI, Request, Response, BackgroundTasks
from fastapi.middleware.base import BaseHTTPMiddleware
from typing import Dict, Any, List, Optional, Callable
import time
import asyncio
from collections import defaultdict
from datetime import datetime, timedelta


class RequestLogger(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.logs: List[Dict[str, Any]] = []

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Log request
        request_log = {
            "method": request.method,
            "url": str(request.url),
            "timestamp": datetime.utcnow().isoformat(),
            "client_ip": request.client.host if request.client else None
        }
        
        # Process request
        response = await call_next(request)
        
        # Log response
        process_time = time.time() - start_time
        request_log.update({
            "status_code": response.status_code,
            "process_time": process_time
        })
        
        self.logs.append(request_log)
        return response

    def get_logs(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def clear_logs(self) -> None:
        raise NotImplementedError


class BackgroundTaskManager:
    def __init__(self):
        self.tasks: List[Dict[str, Any]] = []
        self.running_tasks: List[asyncio.Task] = []

    def add_task(self, task_func: Callable, *args, **kwargs) -> str:
        raise NotImplementedError

    async def execute_task(self, task_id: str) -> Any:
        raise NotImplementedError

    def get_task_status(self, task_id: str) -> Dict[str, Any]:
        raise NotImplementedError

    def cancel_task(self, task_id: str) -> bool:
        raise NotImplementedError

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        raise NotImplementedError


class RateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.requests_per_minute = requests_per_minute
        self.requests: Dict[str, List[datetime]] = defaultdict(list)

    def is_rate_limited(self, client_ip: str) -> bool:
        raise NotImplementedError

    def add_request(self, client_ip: str) -> None:
        raise NotImplementedError

    def get_rate_limit_status(self, client_ip: str) -> Dict[str, Any]:
        raise NotImplementedError


# FastAPI app
app = FastAPI()

# Add middleware
app.add_middleware(RequestLogger)

# Background task manager
task_manager = BackgroundTaskManager()

# Rate limiter
rate_limiter = RateLimiter(requests_per_minute=10)


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host if request.client else "unknown"
    
    if rate_limiter.is_rate_limited(client_ip):
        return Response(
            content="Rate limit exceeded",
            status_code=429
        )
    
    rate_limiter.add_request(client_ip)
    response = await call_next(request)
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/background-task")
async def create_background_task(background_tasks: BackgroundTasks, data: Dict[str, Any]):
    raise NotImplementedError


@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    raise NotImplementedError


@app.get("/logs")
async def get_logs():
    raise NotImplementedError


@app.get("/rate-limit-status")
async def get_rate_limit_status(request: Request):
    raise NotImplementedError


