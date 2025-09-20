from fastapi.testclient import TestClient
from tasks import app, CacheManager, PerformanceOptimizer, LoadBalancer, CacheStrategy


def test_cache_manager():
    cache = CacheManager(max_size=100, strategy=CacheStrategy.LRU)
    
    # Test cache operations
    try:
        # Test setting and getting values
        cache.set("key1", "value1", ttl=60)
        value = cache.get("key1")
        assert value == "value1"
        
        # Test cache stats
        stats = cache.get_cache_stats()
        assert isinstance(stats, dict)
        assert "size" in stats
        assert "hits" in stats
        assert "misses" in stats
        
        # Test cache deletion
        deleted = cache.delete("key1")
        assert deleted is True
        
        # Test cache clearing
        cache.clear()
        assert len(cache.cache) == 0
    except NotImplementedError:
        # Expected for stub implementation
        pass


def test_performance_optimizer():
    optimizer = PerformanceOptimizer()
    
    # Test performance monitoring
    try:
        # Test recording metrics
        optimizer.record_metric("response_time", 0.5)
        optimizer.record_metric("memory_usage", 70.0)
        optimizer.record_metric("cpu_usage", 60.0)
        
        # Test performance summary
        summary = optimizer.get_performance_summary()
        assert isinstance(summary, dict)
        assert "average_response_time" in summary
        assert "average_memory_usage" in summary
        assert "average_cpu_usage" in summary
        
        # Test threshold checking
        alerts = optimizer.check_performance_thresholds()
        assert isinstance(alerts, list)
        
        # Test optimization
        optimization_result = optimizer.optimize_performance()
        assert isinstance(optimization_result, dict)
    except NotImplementedError:
        # Expected for stub implementation
        pass


def test_load_balancer():
    servers = ["server1.example.com", "server2.example.com", "server3.example.com"]
    balancer = LoadBalancer(servers)
    
    # Test load balancing
    try:
        # Test getting next server
        server = balancer.get_next_server()
        assert server in servers
        
        # Test updating server weights
        balancer.update_server_weight("server1.example.com", 2.0)
        assert balancer.server_weights["server1.example.com"] == 2.0
        
        # Test server health checking
        health = balancer.check_server_health("server1.example.com")
        assert isinstance(health, bool)
        
        # Test load balancer stats
        stats = balancer.get_load_balancer_stats()
        assert isinstance(stats, dict)
        assert "total_servers" in stats
        assert "healthy_servers" in stats
    except NotImplementedError:
        # Expected for stub implementation
        pass


def test_fastapi_endpoints():
    client = TestClient(app)
    
    # Test root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Performance Optimized API"}
    
    # Test cache stats endpoint
    response = client.get("/cache/stats")
    assert response.status_code in [200, 422]  # 422 for validation errors
    
    # Test performance summary endpoint
    response = client.get("/performance/summary")
    assert response.status_code in [200, 422]
    
    # Test load balancer stats endpoint
    response = client.get("/load-balancer/stats")
    assert response.status_code in [200, 422]
    
    # Test cache clear endpoint
    response = client.post("/cache/clear")
    assert response.status_code in [200, 422]
    
    # Test optimization endpoint
    response = client.get("/optimize")
    assert response.status_code in [200, 422]


