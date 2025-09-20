import time
from tasks import PerformanceProfiler, LoadTester, BenchmarkRunner


def test_performance_profiler():
    profiler = PerformanceProfiler()
    
    with profiler.profile("test_function"):
        time.sleep(0.01)
    
    stats = profiler.get_profile_stats("test_function")
    assert "mean" in stats
    assert "min" in stats
    assert "max" in stats
    
    all_profiles = profiler.get_all_profiles()
    assert "test_function" in all_profiles


def test_load_tester():
    tester = LoadTester("http://example.com")
    
    # Mock the load test results
    tester.results = [
        {"response_time": 0.1, "status_code": 200},
        {"response_time": 0.2, "status_code": 200},
        {"response_time": 0.15, "status_code": 500}
    ]
    
    response_times = tester.get_response_times()
    assert len(response_times) == 3
    assert all(rt > 0 for rt in response_times)
    
    error_rate = tester.get_error_rate()
    assert 0 <= error_rate <= 1


def test_benchmark_runner():
    runner = BenchmarkRunner()
    
    def fast_function():
        return sum(range(100))
    
    def slow_function():
        return sum(range(1000))
    
    runner.add_benchmark("fast", fast_function)
    runner.add_benchmark("slow", slow_function)
    
    results = runner.run_benchmarks()
    assert "fast" in results
    assert "slow" in results
    
    comparison = runner.compare_benchmarks()
    assert "fast" in comparison
    assert "slow" in comparison


