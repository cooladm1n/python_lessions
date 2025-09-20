"""
Tasks for Lesson 03 (Query Optimization)
"""
from __future__ import annotations
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import func, and_, or_
from typing import List, Dict, Any, Optional


def get_user_with_posts(session, user_id: int) -> Optional[User]:
    raise NotImplementedError


def get_posts_by_tag(session, tag_name: str) -> List[Post]:
    raise NotImplementedError


def get_user_stats(session) -> Dict[str, Any]:
    raise NotImplementedError


def get_popular_posts(session, limit: int = 10) -> List[Post]:
    raise NotImplementedError


def get_user_activity(session, user_id: int) -> Dict[str, Any]:
    raise NotImplementedError


