from tasks import extract_emails, validate_phone, extract_numbers


def test_extract_emails():
    text = "Contact alice@example.com or bob@test.org for help"
    emails = extract_emails(text)
    assert "alice@example.com" in emails
    assert "bob@test.org" in emails


def test_validate_phone():
    assert validate_phone("+1-555-123-4567") is True
    assert validate_phone("555-123-4567") is False
    assert validate_phone("invalid") is False


def test_extract_numbers():
    text = "I have 5 apples and 12 oranges, total 17 fruits"
    numbers = extract_numbers(text)
    assert 5 in numbers
    assert 12 in numbers
    assert 17 in numbers


