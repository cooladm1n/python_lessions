"""
Tasks for Lesson 10 (Database Monitoring and Maintenance)
"""
from __future__ import annotations
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import threading
import time


class DatabaseMonitor:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.metrics: List[Dict[str, Any]] = []
        self.alerts: List[Dict[str, Any]] = []
        self.monitoring = False

    def start_monitoring(self) -> None:
        raise NotImplementedError

    def stop_monitoring(self) -> None:
        raise NotImplementedError

    def collect_metrics(self) -> Dict[str, Any]:
        raise NotImplementedError

    def check_performance_thresholds(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def get_health_status(self) -> Dict[str, Any]:
        raise NotImplementedError


class MaintenanceScheduler:
    def __init__(self):
        self.tasks: List[Dict[str, Any]] = []
        self.scheduler_running = False

    def add_maintenance_task(self, task_name: str, schedule: str, task_func) -> None:
        raise NotImplementedError

    def start_scheduler(self) -> None:
        raise NotImplementedError

    def stop_scheduler(self) -> None:
        raise NotImplementedError

    def run_maintenance_tasks(self) -> List[Dict[str, Any]]:
        raise NotImplementedError


class BackupManager:
    def __init__(self, connection_string: str, backup_dir: str):
        self.connection_string = connection_string
        self.backup_dir = backup_dir
        self.backups: List[Dict[str, Any]] = []

    def create_backup(self, backup_name: str) -> str:
        raise NotImplementedError

    def restore_backup(self, backup_path: str) -> bool:
        raise NotImplementedError

    def list_backups(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def cleanup_old_backups(self, days_to_keep: int) -> int:
        raise NotImplementedError


