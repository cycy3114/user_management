import uuid
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest
from app.models.user_model import UserRole

# Fixtures for common test data
@pytest.fixture
def user_base_data():
    return {
        "nickname": "john_doe_123",
        "email": "john.doe@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "role": "AUTHENTICATED",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe",
        "github_profile_url": "https://github.com/johndoe"
    }

@pytest.fixture
def user_create_data(user_base_data):
    return {**user_base_data, "password": "SecurePassword123!"}

@pytest.fixture
def user_update_data():
    return {
        "email": "john.doe.new@example.com",
        "nickname": "j_doe",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "I specialize in backend development with Python and Node.js.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe_updated.jpg"
    }

@pytest.fixture
def user_response_data(user_base_data):
    return {
        "id": uuid.uuid4(),
        "nickname": user_base_data["nickname"],
        "first_name": user_base_data["first_name"],
        "last_name": user_base_data["last_name"],
        "role": user_base_data["role"],
        "email": user_base_data["email"],
        # "last_login_at": datetime.now(),
        # "created_at": datetime.now(),
        # "updated_at": datetime.now(),
        "links": []
    }

@pytest.fixture
def login_request_data():
    return {"email": "john_doe_123@emai.com", "password": "SecurePassword123!"}

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserBase all fields
def test_user_base_valid_all_fields(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]
    assert user.first_name == user_base_data["first_name"]
    assert user.last_name == user_base_data["last_name"]
    assert user.role == UserRole.AUTHENTICATED
    assert user.bio == user_base_data["bio"]
    assert user.profile_picture_url == user_base_data["profile_picture_url"]
    assert user.linkedin_profile_url == user_base_data["linkedin_profile_url"]
    assert user.github_profile_url == user_base_data["github_profile_url"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Tests for UserCreate all fields
def test_user_create_valid_all_fields(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.email == user_create_data["email"]
    assert user.first_name == user_create_data["first_name"]
    assert user.last_name == user_create_data["last_name"]
    assert user.role == UserRole.AUTHENTICATED
    assert user.bio == user_create_data["bio"]
    assert user.profile_picture_url == user_create_data["profile_picture_url"]
    assert user.linkedin_profile_url == user_create_data["linkedin_profile_url"]
    assert user.github_profile_url == user_create_data["github_profile_url"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Tests for UserUpdate all fields
def test_user_update_valid_all_fields(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.nickname == user_update_data["nickname"]
    assert user_update.first_name == user_update_data["first_name"]
    assert user_update.last_name == user_update_data["last_name"]
    assert user_update.bio == user_update_data["bio"]
    assert user_update.profile_picture_url == user_update_data["profile_picture_url"]

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == user_response_data["id"]
    # assert user.last_login_at == user_response_data["last_login_at"]

# Tests for UserResponse all fields
def test_user_response_valid_all_fields(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == user_response_data["id"]
    assert user.nickname == user_response_data["nickname"]
    assert user.first_name == user_response_data["first_name"]
    assert user.last_name == user_response_data["last_name"]
    assert user.role == UserRole.AUTHENTICATED
    assert user.email == user_response_data["email"]

    # Uncomment and adjust these if you include these fields in the UserResponse schema and the user_response_data fixture
    # assert user.links == user_response_data["links"]
    # assert user.last_login_at == user_response_data["last_login_at"]
    # assert user.created_at == user_response_data["created_at"]
    # assert user.updated_at == user_response_data["updated_at"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parameterized tests for email validation
@pytest.mark.parametrize("email", [
    "valid.email@example.com",
    "user123@example.co",
    "user.name+tag@sub.domain.com",
    "user_name@domain.org"
])
def test_user_base_email_valid(email, user_base_data):
    user_base_data["email"] = email
    user = UserBase(**user_base_data)
    assert user.email == email

@pytest.mark.parametrize("email", [
    "invalid-email",
    "user@.com",
    "user@domain",
    "@domain.com",
    "",
    "user@domain..com"
])
def test_user_base_email_invalid(email, user_base_data):
    user_base_data["email"] = email
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)
