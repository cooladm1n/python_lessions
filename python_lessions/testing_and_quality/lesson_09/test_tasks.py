from pathlib import Path
from tasks import TestDataManager, TestEnvironment, DataGenerator


def test_test_data_manager(tmp_path: Path):
    manager = TestDataManager(tmp_path)
    
    test_data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    manager.create_data_set("users", test_data)
    
    data_set = manager.get_data_set("users")
    assert len(data_set) == 2
    assert data_set[0]["name"] == "Alice"
    
    manager.cleanup_data()
    assert len(manager.data_sets) == 0


def test_test_environment():
    env = TestEnvironment("test_env")
    
    env.set_config("database_url", "sqlite:///:memory:")
    env.set_config("debug", True)
    
    env.add_service("database")
    env.add_service("redis")
    
    assert env.config["database_url"] == "sqlite:///:memory:"
    assert env.config["debug"] is True
    assert "database" in env.services
    assert "redis" in env.services


def test_data_generator():
    generator = DataGenerator()
    
    def user_generator():
        return {"name": "Test User", "email": "test@example.com"}
    
    generator.add_generator("user", user_generator)
    
    data = generator.generate_data("user", 3)
    assert len(data) == 3
    assert all("name" in item for item in data)
    
    user_data = generator.generate_user_data(2)
    assert len(user_data) == 2


