from tasks import DatabaseFixture, MockService, TestDataBuilder


def test_database_fixture():
    fixture = DatabaseFixture("sqlite:///:memory:")
    fixture.setup()
    
    fixture.add_test_data({"id": 1, "name": "Alice"})
    fixture.add_test_data({"id": 2, "name": "Bob"})
    
    data = fixture.get_test_data()
    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    
    fixture.teardown()


def test_mock_service():
    service = MockService("user_service")
    service.mock_method("get_user", {"id": 1, "name": "Alice"})
    service.mock_method("create_user", {"id": 2, "name": "Bob"})
    
    # Simulate method calls
    service.mocks["get_user"].return_value = {"id": 1, "name": "Alice"}
    service.mocks["create_user"].return_value = {"id": 2, "name": "Bob"}
    
    service.mocks["get_user"](user_id=1)
    service.mocks["create_user"](name="Bob")
    
    history = service.get_call_history("get_user")
    assert len(history) == 1
    
    service.reset()


def test_test_data_builder():
    builder = TestDataBuilder({"type": "user"})
    data = builder.with_field("name", "Alice").with_field("age", 30).with_id(1).build()
    
    assert data["name"] == "Alice"
    assert data["age"] == 30
    assert data["id"] == 1
    assert data["type"] == "user"


