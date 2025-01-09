import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.messages import get_messages
from project.models import ProjectUser
from pytest_django import asserts


@pytest.mark.django_db
class TestUserLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.user = ProjectUser.objects.create_user(username="testuser", password="testpass123")

    def test_login_page_get(self, setup):
        response = self.client.get(self.login_url)
        assert response.status_code == 200
        asserts.assertTemplateUsed(response, "project/login.html")

    def test_login_success(self):
        response = self.client.post(self.login_url, {"username": "testuser", "password": "testpass123"})
        asserts.assertRedirects(response, reverse("site-admin"))
        assert response.wsgi_request.user.is_authenticated == True

    def test_login_success_with_next(self):
        next_url = "/site-admin/"
        response = self.client.post(
            f"{self.login_url}?next={next_url}", {"username": "testuser", "password": "testpass123"}
        )
        asserts.assertRedirects(response, next_url)

    def test_login_wrong_password(self):
        response = self.client.post(self.login_url, {"username": "testuser", "password": "wrongpass"})
        messages = list(get_messages(response.wsgi_request))
        assert str(messages[0]) == "Username OR password is incorrect"
        asserts.assertTemplateUsed(response, "project/login.html")

    def test_login_nonexistent_user(self):
        response = self.client.post(self.login_url, {"username": "nonexistent", "password": "testpass123"})
        messages = list(get_messages(response.wsgi_request))
        assert str(messages[0]) == "Username does not exist"
        asserts.assertTemplateUsed(response, "project/login.html")

    def test_login_uppercase_username(self):
        response = self.client.post(self.login_url, {"username": "TESTUSER", "password": "testpass123"})
        asserts.assertRedirects(response, reverse("site-admin"))
        assert response.wsgi_request.user.is_authenticated == True
