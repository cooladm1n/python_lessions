from tasks import TestReporter, TestAnalytics, TestDashboard


def test_test_reporter():
    reporter = TestReporter()
    
    reporter.add_test_result("test_add", "passed", 0.1)
    reporter.add_test_result("test_subtract", "failed", 0.2, "AssertionError")
    reporter.add_test_result("test_multiply", "passed", 0.05)
    
    summary = reporter.generate_summary()
    assert summary["total"] == 3
    assert summary["passed"] == 2
    assert summary["failed"] == 1
    
    html_report = reporter.generate_html_report()
    assert "test_add" in html_report
    assert "test_subtract" in html_report
    
    json_report = reporter.generate_json_report()
    assert "test_results" in json_report


def test_test_analytics():
    analytics = TestAnalytics()
    
    analytics.add_test_run({"date": "2023-01-01", "passed": 10, "failed": 2})
    analytics.add_test_run({"date": "2023-01-02", "passed": 12, "failed": 1})
    analytics.add_test_run({"date": "2023-01-03", "passed": 8, "failed": 4})
    
    trends = analytics.calculate_trends()
    assert "pass_rate" in trends
    assert "failure_rate" in trends
    
    patterns = analytics.get_failure_patterns()
    assert isinstance(patterns, list)
    
    risk = analytics.predict_failure_risk()
    assert 0 <= risk <= 1


def test_test_dashboard():
    dashboard = TestDashboard()
    
    dashboard.add_widget("test_summary", {"title": "Test Summary"})
    dashboard.add_widget("failure_trend", {"title": "Failure Trend"})
    
    dashboard.update_metrics({"total_tests": 100, "pass_rate": 0.95})
    
    dashboard_html = dashboard.generate_dashboard()
    assert "test_summary" in dashboard_html
    assert "failure_trend" in dashboard_html
    
    widget_data = dashboard.get_widget_data("test_summary")
    assert "title" in widget_data


