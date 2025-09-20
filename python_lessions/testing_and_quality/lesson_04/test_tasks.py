from pathlib import Path
from tasks import CoverageAnalyzer, QualityMetrics, TestReportGenerator


def test_coverage_analyzer(tmp_path: Path):
    analyzer = CoverageAnalyzer(tmp_path)
    
    # Create a simple Python file for testing
    test_file = tmp_path / "test_module.py"
    test_file.write_text("def add(a, b):\n    return a + b\n")
    
    coverage = analyzer.analyze_coverage()
    assert isinstance(coverage, dict)
    
    percentage = analyzer.get_coverage_percentage()
    assert 0 <= percentage <= 100
    
    uncovered = analyzer.get_uncovered_lines()
    assert isinstance(uncovered, list)


def test_quality_metrics():
    metrics = QualityMetrics()
    
    code = "def add(a, b):\n    return a + b\n"
    complexity = metrics.calculate_complexity(code)
    assert complexity > 0
    
    maintainability = metrics.calculate_maintainability(code)
    assert 0 <= maintainability <= 1
    
    score = metrics.get_quality_score()
    assert 0 <= score <= 100


def test_test_report_generator():
    generator = TestReportGenerator()
    
    generator.add_test_result("test_add", True, 0.1)
    generator.add_test_result("test_subtract", False, 0.2)
    
    generator.set_coverage_data({"total": 100, "covered": 80})
    
    report = generator.generate_report()
    assert "test_add" in report
    assert "test_subtract" in report
    assert "coverage" in report.lower()


