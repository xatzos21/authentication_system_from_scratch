from django.test import TestCase, Client
from django.urls import reverse
from .forms import LoginForm


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")

    def test_login_view_with_valid_credentials(self):
        response = self.client.post(
            self.login_url, {"username": "aek", "password": "r21"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.client.session.get("logged_in"))
        self.assertRedirects(response, self.logout_url)

    def test_login_view_with_invalid_credentials(self):
        response = self.client.post(
            self.login_url, {"username": "invalid", "password": "password"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.client.session.get("logged_in"))
        messages = list(response.context.get("messages"))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Invalid username or password")

    def test_login_view_with_get_request(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/login.html")
        self.assertIsInstance(response.context["form"], LoginForm)

    def test_logout_view_with_post_request(self):
        self.client.session["logged_in"] = True
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.client.session.get("logged_in"))
        self.assertRedirects(response, self.login_url)

    def test_logout_view_with_get_request(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/logout.html")
