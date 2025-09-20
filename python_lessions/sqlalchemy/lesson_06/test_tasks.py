from tasks import ConnectionPool, DatabaseManager, ConnectionHealthCheck


def test_connection_pool():
    pool = ConnectionPool("sqlite:///:memory:", max_connections=5)
    pool.initialize()
    
    assert pool.engine is not None
    assert pool.session_factory is not None
    
    # Test getting session
    session = pool.get_session()
    assert session is not None
    
    # Test pool status
    status = pool.get_pool_status()
    assert "max_connections" in status
    assert "active_connections" in status
    
    pool.close_all_connections()


def test_database_manager():
    pool = ConnectionPool("sqlite:///:memory:")
    pool.initialize()
    
    manager = DatabaseManager(pool)
    
    # Test query execution
    result = manager.execute_query("SELECT 1 as test")
    assert result is not None
    
    # Test database info
    info = manager.get_database_info()
    assert "database_url" in info
    
    pool.close_all_connections()


def test_connection_health_check():
    pool = ConnectionPool("sqlite:///:memory:")
    pool.initialize()
    
    manager = DatabaseManager(pool)
    health_check = ConnectionHealthCheck(manager)
    
    # Test health check
    is_healthy = health_check.check_health()
    assert isinstance(is_healthy, bool)
    
    # Test health status
    status = health_check.get_health_status()
    assert "status" in status
    assert "last_check" in status
    
    pool.close_all_connections()


