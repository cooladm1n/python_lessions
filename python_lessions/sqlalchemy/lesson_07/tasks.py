"""
Tasks for Lesson 07 (Database Events and Hooks)
"""
from __future__ import annotations
from sqlalchemy import event
from sqlalchemy.orm import Session
from typing import Dict, Any, List
import hashlib
import json
from datetime import datetime


class UserValidator:
    def __init__(self):
        self.validation_errors: List[str] = []

    def validate_user(self, user) -> bool:
        raise NotImplementedError

    def setup_event_listeners(self, User) -> None:
        raise NotImplementedError

    def get_validation_errors(self) -> List[str]:
        raise NotImplementedError


class AuditLogger:
    def __init__(self):
        self.audit_logs: List[Dict[str, Any]] = []

    def log_change(self, entity, action: str, changes: Dict[str, Any]) -> None:
        raise NotImplementedError

    def setup_event_listeners(self, model) -> None:
        raise NotImplementedError

    def get_audit_logs(self) -> List[Dict[str, Any]]:
        raise NotImplementedError


class DataEncryptor:
    def __init__(self, encryption_key: str):
        self.encryption_key = encryption_key
        self.encrypted_fields: List[str] = []

    def encrypt_field(self, value: str) -> str:
        raise NotImplementedError

    def decrypt_field(self, encrypted_value: str) -> str:
        raise NotImplementedError

    def setup_event_listeners(self, model, fields: List[str]) -> None:
        raise NotImplementedError


