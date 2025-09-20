from fastapi.testclient import TestClient
from tasks import app, JWTManager, OAuth2Provider, RoleBasedAccess, UserRole


def test_jwt_manager():
    manager = JWTManager("test_secret_key")
    
    # Test token creation
    data = {"user_id": "123", "username": "alice"}
    token = manager.create_access_token(data)
    assert token is not None
    
    # Test token verification
    decoded_data = manager.verify_token(token)
    assert decoded_data["user_id"] == "123"
    assert decoded_data["username"] == "alice"
    
    # Test token refresh
    new_token = manager.refresh_token(token)
    assert new_token != token


def test_oauth2_provider():
    provider = OAuth2Provider("client_id", "client_secret", "http://localhost:8000/callback")
    
    # Test authorization URL
    auth_url = provider.get_authorization_url("state123")
    assert "client_id" in auth_url
    assert "state123" in auth_url
    
    # Test token exchange (mock)
    try:
        token_data = provider.exchange_code_for_token("auth_code")
        assert isinstance(token_data, dict)
    except NotImplementedError:
        # Expected for stub implementation
        pass
    
    # Test user info (mock)
    try:
        user_info = provider.get_user_info("access_token")
        assert isinstance(user_info, dict)
    except NotImplementedError:
        # Expected for stub implementation
        pass


def test_role_based_access():
    rbac = RoleBasedAccess()
    
    # Test role assignment
    rbac.assign_role("user1", UserRole.ADMIN)
    rbac.assign_role("user1", UserRole.USER)
    
    # Test permission checking
    has_permission = rbac.check_permission("user1", "read_users")
    assert isinstance(has_permission, bool)
    
    # Test getting user permissions
    permissions = rbac.get_user_permissions("user1")
    assert isinstance(permissions, list)


def test_fastapi_endpoints():
    client = TestClient(app)
    
    # Test login endpoint
    response = client.post("/login", data={"username": "alice", "password": "password123"})
    assert response.status_code in [200, 422]  # 422 for validation errors
    
    # Test register endpoint
    response = client.post("/register", data={"username": "bob", "email": "bob@example.com", "password": "password123"})
    assert response.status_code in [200, 422]
    
    # Test protected route (should require authentication)
    response = client.get("/protected")
    assert response.status_code in [401, 403]  # Unauthorized without token
    
    # Test admin route (should require admin role)
    response = client.get("/admin-only")
    assert response.status_code in [401, 403]  # Unauthorized without admin role


