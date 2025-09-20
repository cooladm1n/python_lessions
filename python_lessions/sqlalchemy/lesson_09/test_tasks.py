from tasks import SecurityManager, DataMasker, AuditTrail, Permission


def test_security_manager():
    manager = SecurityManager()
    
    # Test permission granting
    manager.grant_permission("user1", Permission.READ)
    manager.grant_permission("user1", Permission.WRITE)
    
    # Test permission checking
    assert manager.check_permission("user1", Permission.READ) is True
    assert manager.check_permission("user1", Permission.DELETE) is False
    
    # Test access logging
    manager.log_access("user1", "read", "users")
    manager.log_access("user1", "write", "posts")
    
    logs = manager.get_access_logs()
    assert len(logs) == 2
    assert logs[0]["user_id"] == "user1"
    assert logs[0]["action"] == "read"


def test_data_masker():
    masker = DataMasker()
    
    # Test masking rules
    masker.add_masking_rule("email", "***@***.***")
    masker.add_masking_rule("phone", "***-***-****")
    
    # Test data masking
    data = {"name": "Alice", "email": "alice@example.com", "phone": "123-456-7890"}
    masked_data = masker.mask_sensitive_data(data)
    
    assert masked_data["name"] == "Alice"  # Not sensitive
    assert masked_data["email"] == "***@***.***"
    assert masked_data["phone"] == "***-***-****"
    
    # Test unmasking with permissions
    unmasked_data = masker.unmask_data(masked_data, [Permission.ADMIN])
    assert unmasked_data["email"] == "alice@example.com"
    assert unmasked_data["phone"] == "123-456-7890"


def test_audit_trail():
    trail = AuditTrail()
    
    # Test data access logging
    trail.log_data_access("user1", "users", "read", "123")
    trail.log_data_access("user1", "posts", "write", "456")
    
    # Test security event logging
    trail.log_security_event("failed_login", "user2", {"ip": "192.168.1.1", "attempts": 3})
    
    # Test audit report
    from datetime import datetime, timedelta
    start_date = datetime.now() - timedelta(days=1)
    end_date = datetime.now()
    
    report = trail.get_audit_report(start_date, end_date)
    assert len(report) >= 2
    
    # Test suspicious activity detection
    suspicious = trail.detect_suspicious_activity()
    assert isinstance(suspicious, list)


