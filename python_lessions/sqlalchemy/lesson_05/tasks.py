"""
Tasks for Lesson 05 (Advanced Query Techniques)
"""
from __future__ import annotations
from sqlalchemy import func, desc, asc, text
from sqlalchemy.orm import sessionmaker
from typing import List, Dict, Any


def get_top_users(session, limit: int = 10) -> List[Dict[str, Any]]:
    raise NotImplementedError


def get_posts_with_comments(session) -> List[Dict[str, Any]]:
    raise NotImplementedError


def get_user_rankings(session) -> List[Dict[str, Any]]:
    raise NotImplementedError


def get_posts_by_date_range(session, start_date, end_date) -> List[Dict[str, Any]]:
    raise NotImplementedError


def get_tag_statistics(session) -> List[Dict[str, Any]]:
    raise NotImplementedError


