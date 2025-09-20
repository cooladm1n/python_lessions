from tasks import DatabaseMonitor, MaintenanceScheduler, BackupManager


def test_database_monitor():
    monitor = DatabaseMonitor("sqlite:///:memory:")
    
    # Test monitoring start/stop
    monitor.start_monitoring()
    assert monitor.monitoring is True
    
    monitor.stop_monitoring()
    assert monitor.monitoring is False
    
    # Test metrics collection
    metrics = monitor.collect_metrics()
    assert isinstance(metrics, dict)
    assert "connection_count" in metrics
    
    # Test performance thresholds
    alerts = monitor.check_performance_thresholds()
    assert isinstance(alerts, list)
    
    # Test health status
    health = monitor.get_health_status()
    assert "status" in health
    assert "timestamp" in health


def test_maintenance_scheduler():
    scheduler = MaintenanceScheduler()
    
    # Test adding maintenance tasks
    def cleanup_task():
        return "cleanup completed"
    
    scheduler.add_maintenance_task("cleanup", "daily", cleanup_task)
    assert len(scheduler.tasks) == 1
    
    # Test scheduler start/stop
    scheduler.start_scheduler()
    assert scheduler.scheduler_running is True
    
    scheduler.stop_scheduler()
    assert scheduler.scheduler_running is False
    
    # Test running maintenance tasks
    results = scheduler.run_maintenance_tasks()
    assert isinstance(results, list)


def test_backup_manager():
    manager = BackupManager("sqlite:///:memory:", "/tmp/backups")
    
    # Test backup creation
    backup_path = manager.create_backup("test_backup")
    assert backup_path is not None
    assert "test_backup" in backup_path
    
    # Test backup listing
    backups = manager.list_backups()
    assert isinstance(backups, list)
    assert len(backups) >= 1
    
    # Test backup restoration
    restore_success = manager.restore_backup(backup_path)
    assert restore_success is True
    
    # Test cleanup
    cleaned_count = manager.cleanup_old_backups(7)
    assert isinstance(cleaned_count, int)


