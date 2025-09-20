from pathlib import Path
from tasks import SecurityScanner, VulnerabilityDetector, SecurityTestRunner


def test_security_scanner(tmp_path: Path):
    scanner = SecurityScanner()
    
    scanner.add_scan_rule("sql_injection", "SELECT.*FROM", "high")
    scanner.add_scan_rule("hardcoded_password", "password.*=", "medium")
    
    test_file = tmp_path / "test.py"
    test_file.write_text("SELECT * FROM users WHERE id = 1")
    
    vulnerabilities = scanner.scan_file(test_file)
    assert len(vulnerabilities) > 0
    
    directory_vulns = scanner.scan_directory(tmp_path)
    assert len(directory_vulns) > 0


def test_vulnerability_detector():
    detector = VulnerabilityDetector()
    
    def sql_injection_detector(code: str):
        if "SELECT" in code.upper():
            return [{"type": "sql_injection", "severity": "high"}]
        return []
    
    detector.add_detector(sql_injection_detector)
    
    code = "SELECT * FROM users"
    vulnerabilities = detector.detect_vulnerabilities(code)
    assert len(vulnerabilities) > 0
    
    summary = detector.get_vulnerability_summary()
    assert "sql_injection" in summary


def test_security_test_runner():
    runner = SecurityTestRunner()
    
    def test_sql_injection():
        return {"test": "sql_injection", "passed": True}
    
    def test_xss():
        return {"test": "xss", "passed": False}
    
    runner.add_security_test(test_sql_injection)
    runner.add_security_test(test_xss)
    
    results = runner.run_security_tests()
    assert len(results) == 2
    
    report = runner.generate_security_report()
    assert "sql_injection" in report
    assert "xss" in report


