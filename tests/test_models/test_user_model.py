from builtins import repr
from datetime import datetime, timezone
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_model import User, UserRole

@pytest.mark.asyncio
async def test_user_role(db_session: AsyncSession, user: User, admin_user: User, manager_user: User):
    """
    Tests that the default role is assigned correctly and can be updated.
    """
    assert user.role == UserRole.AUTHENTICATED, "Default role should be USER"
    assert admin_user.role == UserRole.ADMIN, "Admin role should be correctly assigned"
    assert manager_user.role == UserRole.MANAGER, "Pro role should be correctly assigned"
@pytest.mark.asyncio
async def test_user_nickname(db_session: AsyncSession, admin_user: User, manager_user: User):
    """
    Tests that nickname is assigned correctly.
    """
    assert admin_user.nickname == "admin_user", "Admin user's nickname should be correctly assigned"
    assert manager_user.nickname == "manager_john", "Manager user's nickname should be correctly assigned"

@pytest.mark.asyncio
async def test_user_email(db_session: AsyncSession, admin_user: User, manager_user: User):
    """
    Tests that email is assigned correctly.
    """
    assert admin_user.email == "admin@example.com", "Admin user's email should be correctly assigned"
    assert manager_user.email == "manager_user@example.com", "Manager user's email should be correctly assigned"

@pytest.mark.asyncio
async def test_user_first_name(db_session: AsyncSession, admin_user: User, manager_user: User):
    """
    Tests that first name is assigned correctly.
    """
    assert admin_user.first_name == "John", "Admin user's first name should be correctly assigned"
    assert manager_user.first_name == "John", "Manager user's first name should be correctly assigned"

@pytest.mark.asyncio
async def test_user_last_name(db_session: AsyncSession, admin_user: User, manager_user: User):
    """
    Tests that last name is assigned correctly.
    """
    assert admin_user.last_name == "Doe", "Admin user's last name should be correctly assigned"
    assert manager_user.last_name == "Doe", "Manager user's last name should be correctly assigned"

@pytest.mark.asyncio
async def test_user_password(db_session: AsyncSession, admin_user: User, manager_user: User):
    """
    Tests that password is assigned correctly.
    """
    assert admin_user.hashed_password == "securepassword", "Admin user's hashed password should be correctly assigned"
    assert manager_user.hashed_password == "securepassword", "Manager user's hashed password should be correctly assigned"

@pytest.mark.asyncio
async def test_has_role(user: User, admin_user: User, manager_user: User):
    """
    Tests the has_role method to ensure it accurately checks the user's role.
    """
    assert user.has_role(UserRole.AUTHENTICATED), "User should have USER role"
    assert not user.has_role(UserRole.ADMIN), "User should not have ADMIN role"
    assert admin_user.has_role(UserRole.ADMIN), "Admin user should have ADMIN role"
    assert manager_user.has_role(UserRole.MANAGER), "Pro user should have PRO role"

@pytest.mark.asyncio
async def test_user_repr(user: User):
    """
    Tests the __repr__ method for accurate representation of the User object.
    """
    assert repr(user) == f"<User {user.nickname}, Role: {user.role.name}>", "__repr__ should include nickname and role"

@pytest.mark.asyncio
async def test_failed_login_attempts_increment(db_session: AsyncSession, user: User):
    """
    Tests that failed login attempts can be incremented and persisted correctly.
    """
    initial_attempts = user.failed_login_attempts
    user.failed_login_attempts += 1
    await db_session.commit()
    await db_session.refresh(user)
    assert user.failed_login_attempts == initial_attempts + 1, "Failed login attempts should increment"

@pytest.mark.asyncio
async def test_last_login_update(db_session: AsyncSession, user: User):
    """
    Tests updating the last login timestamp.
    """
    new_last_login = datetime.now(timezone.utc)
    user.last_login_at = new_last_login
    await db_session.commit()
    await db_session.refresh(user)
    assert user.last_login_at == new_last_login, "Last login timestamp should update correctly"

@pytest.mark.asyncio
async def test_account_lock_and_unlock(db_session: AsyncSession, user: User):
    """
    Tests locking and unlocking the user account.
    """
    # Initially, the account should not be locked.
    assert not user.is_locked, "Account should initially be unlocked"

    # Lock the account and verify.
    user.lock_account()
    await db_session.commit()
    await db_session.refresh(user)
    assert user.is_locked, "Account should be locked after calling lock_account()"

    # Unlock the account and verify.
    user.unlock_account()
    await db_session.commit()
    await db_session.refresh(user)
    assert not user.is_locked, "Account should be unlocked after calling unlock_account()"

@pytest.mark.asyncio
async def test_email_verification(db_session: AsyncSession, user: User):
    """
    Tests the email verification functionality.
    """
    # Initially, the email should not be verified.
    assert not user.email_verified, "Email should initially be unverified"

    # Verify the email and check.
    user.verify_email()
    await db_session.commit()
    await db_session.refresh(user)
    assert user.email_verified, "Email should be verified after calling verify_email()"

@pytest.mark.asyncio
async def test_user_profile_pic_url_update(db_session: AsyncSession, user: User):
    """
    Tests the profile pic update functionality.
    """
    # Initially, the profile pic should be updated.

    # Verify the email and check.
    profile_pic_url = "http://myprofile/picture.png"
    user.profile_picture_url = profile_pic_url
    await db_session.commit()
    await db_session.refresh(user)
    assert user.profile_picture_url == profile_pic_url, "The profile pic did not update"

@pytest.mark.asyncio
async def test_user_linkedin_url_update(db_session: AsyncSession, user: User):
    """
    Tests the profile pic update functionality.
    """
    # Initially, the linkedin should  be updated.

    # Verify the linkedin profile url.
    profile_linkedin_url = "http://www.linkedin.com/profile"
    user.linkedin_profile_url = profile_linkedin_url
    await db_session.commit()
    await db_session.refresh(user)
    assert user.linkedin_profile_url == profile_linkedin_url, "The profile pic did not update"


@pytest.mark.asyncio
async def test_user_github_url_update(db_session: AsyncSession, user: User):
    """
    Tests the profile pic update functionality.
    """
    # Initially, the linkedin should  be updated.

    # Verify the linkedin profile url.
    profile_github_url = "http://www.github.com/profile"
    user.github_profile_url = profile_github_url
    await db_session.commit()
    await db_session.refresh(user)
    assert user.github_profile_url == profile_github_url, "The github did not update"


@pytest.mark.asyncio
async def test_update_user_role(db_session: AsyncSession, user: User):
    """
    Tests updating the user's role and ensuring it persists correctly.
    """
    user.role = UserRole.ADMIN
    await db_session.commit()
    await db_session.refresh(user)
    assert user.role == UserRole.ADMIN, "Role update should persist correctly in the database"

@pytest.mark.asyncio
async def test_update_user_email(db_session: AsyncSession, user: User):
    """
    Tests updating the user's email and ensuring it persists correctly.
    """
    new_email = "new_email@example.com"
    user.email = new_email
    await db_session.commit()
    await db_session.refresh(user)
    assert user.email == new_email, "Email update should persist correctly in the database"

@pytest.mark.asyncio
async def test_update_user_nickname(db_session: AsyncSession, user: User):
    """
    Tests updating the user's nickname and ensuring it persists correctly.
    """
    new_nickname = "kong_fu_panda"
    user.nickname = new_nickname
    await db_session.commit()
    await db_session.refresh(user)
    assert user.nickname == new_nickname, "Nickname update should persist correctly in the database"
