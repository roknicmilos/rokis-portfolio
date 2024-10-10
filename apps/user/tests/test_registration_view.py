from django.test import TestCase
from django.urls import reverse, reverse_lazy
from apps.portfolio import service as portfolio_service

from apps.user.models import User
from apps.user.tests.factories import UserFactory


class TestRegistrationView(TestCase):
    url_path = reverse_lazy("user:register")

    def test_get_response(self):
        response = self.client.get(path=self.url_path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/registration.html")

    def test_post_success_response(self):
        self.assertFalse(User.objects.exists())
        data = {
            "email": "example@example.com",
            "password1": "pass4user",
            "password2": "pass4user",
        }

        response = self.client.post(path=self.url_path, data=data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("admin:index"))
        new_user = User.objects.first()
        self.assertEqual(new_user.email, data["email"])
        self.assertTrue(new_user.check_password(data["password1"]))
        self.assertTrue(new_user.is_active)
        self.assertTrue(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)
        self.assertEqual(
            set(new_user.user_permissions.all()),
            set(portfolio_service.get_default_portfolio_permission()),
        )

    def test_post_error_response(self):
        existing_user = UserFactory()
        self.assertEqual(User.objects.count(), 1)
        data = {
            "email": existing_user.email,
            "password1": "pass4user",
            "password2": "pass4user",
        }
        self.client.post(path=self.url_path, data=data)

        response = self.client.post(path=self.url_path, data=data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/registration.html")
        self.assertContains(
            response, "User with this Email address already exists."
        )
        self.assertEqual(User.objects.count(), 1)
