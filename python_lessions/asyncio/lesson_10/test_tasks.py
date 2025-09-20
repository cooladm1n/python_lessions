import asyncio
from tasks import AsyncMetrics, AsyncLogger, AsyncHealthCheck, HealthStatus


async def test_async_metrics():
    metrics = AsyncMetrics()
    
    metrics.increment_counter("requests", 5)
    metrics.record_timer("response_time", 0.1)
    
    result = await metrics.get_metrics()
    assert result["counters"]["requests"] == 5
    assert "response_time" in result["timers"]


async def test_async_logger():
    logger = AsyncLogger("test_app")
    
    await logger.info("Test message", user_id=123)
    await logger.error("Error message", error_code=500)
    
    logs = await logger.get_logs()
    assert len(logs) == 2
    assert any("Test message" in log["message"] for log in logs)
    assert any("Error message" in log["message"] for log in logs)


async def test_async_health_check():
    health_check = AsyncHealthCheck()
    
    async def healthy_check():
        return True
    
    async def unhealthy_check():
        return False
    
    health_check.add_check(healthy_check)
    health_check.add_check(unhealthy_check)
    
    status = await health_check.run_checks()
    assert status == HealthStatus.UNHEALTHY
    
    result = await health_check.get_status()
    assert result["status"] == HealthStatus.UNHEALTHY


