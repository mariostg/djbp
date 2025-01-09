import pytest
from project.models import ProjectUser


class TestProjectUser:
    def test_user_string_representation(self):
        # Arrange
        test_username = "testuser"
        user = ProjectUser(username=test_username)

        # Act
        result = str(user)

        # Assert
        assert result == test_username
