"""
Tasks for Lesson 03 (Authentication and Authorization)
"""
from __future__ import annotations
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"


class JWTManager:
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = 30

    def create_access_token(self, data: Dict[str, Any]) -> str:
        raise NotImplementedError

    def verify_token(self, token: str) -> Dict[str, Any]:
        raise NotImplementedError

    def refresh_token(self, token: str) -> str:
        raise NotImplementedError


class OAuth2Provider:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_authorization_url(self, state: str) -> str:
        raise NotImplementedError

    def exchange_code_for_token(self, code: str) -> Dict[str, Any]:
        raise NotImplementedError

    def get_user_info(self, access_token: str) -> Dict[str, Any]:
        raise NotImplementedError


class RoleBasedAccess:
    def __init__(self):
        self.user_roles: Dict[str, List[UserRole]] = {}
        self.permissions: Dict[UserRole, List[str]] = {}

    def assign_role(self, user_id: str, role: UserRole) -> None:
        raise NotImplementedError

    def check_permission(self, user_id: str, permission: str) -> bool:
        raise NotImplementedError

    def get_user_permissions(self, user_id: str) -> List[str]:
        raise NotImplementedError


# FastAPI app setup
app = FastAPI()
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post("/login")
async def login(username: str, password: str) -> Dict[str, Any]:
    raise NotImplementedError


@app.post("/register")
async def register(username: str, email: str, password: str) -> Dict[str, Any]:
    raise NotImplementedError


@app.get("/protected")
async def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict[str, Any]:
    raise NotImplementedError


@app.get("/admin-only")
async def admin_only_route(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict[str, Any]:
    raise NotImplementedError


