"""
Tasks for Lesson 06 (Security Testing)
"""
from __future__ import annotations
from typing import Dict, Any, List, Optional
from pathlib import Path


class SecurityScanner:
    def __init__(self):
        self.vulnerabilities: List[Dict[str, Any]] = []
        self.scan_rules: List[Dict[str, Any]] = []

    def add_scan_rule(self, rule_name: str, pattern: str, severity: str) -> None:
        raise NotImplementedError

    def scan_file(self, file_path: Path) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def scan_directory(self, directory: Path) -> List[Dict[str, Any]]:
        raise NotImplementedError


class VulnerabilityDetector:
    def __init__(self):
        self.detectors: List[Callable[[str], List[Dict[str, Any]]]] = []

    def add_detector(self, detector_func: Callable[[str], List[Dict[str, Any]]]) -> None:
        raise NotImplementedError

    def detect_vulnerabilities(self, code: str) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def get_vulnerability_summary(self) -> Dict[str, int]:
        raise NotImplementedError


class SecurityTestRunner:
    def __init__(self):
        self.tests: List[Callable[..., Any]] = []
        self.results: List[Dict[str, Any]] = []

    def add_security_test(self, test_func: Callable[..., Any]) -> None:
        raise NotImplementedError

    def run_security_tests(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def generate_security_report(self) -> str:
        raise NotImplementedError


