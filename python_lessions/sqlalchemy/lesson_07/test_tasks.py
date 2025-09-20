from tasks import UserValidator, AuditLogger, DataEncryptor


def test_user_validator():
    validator = UserValidator()
    
    # Mock user object
    class MockUser:
        def __init__(self, username, email):
            self.username = username
            self.email = email
    
    user = MockUser("alice", "alice@example.com")
    
    # Test validation
    is_valid = validator.validate_user(user)
    assert isinstance(is_valid, bool)
    
    # Test validation errors
    errors = validator.get_validation_errors()
    assert isinstance(errors, list)


def test_audit_logger():
    logger = AuditLogger()
    
    # Mock entity
    class MockEntity:
        def __init__(self, id, name):
            self.id = id
            self.name = name
    
    entity = MockEntity(1, "test")
    changes = {"name": "old_name", "new_name": "new_name"}
    
    # Test logging
    logger.log_change(entity, "update", changes)
    
    logs = logger.get_audit_logs()
    assert len(logs) == 1
    assert logs[0]["action"] == "update"
    assert logs[0]["changes"] == changes


def test_data_encryptor():
    encryptor = DataEncryptor("test_key")
    
    # Test encryption
    original_value = "sensitive_data"
    encrypted = encryptor.encrypt_field(original_value)
    assert encrypted != original_value
    
    # Test decryption
    decrypted = encryptor.decrypt_field(encrypted)
    assert decrypted == original_value


