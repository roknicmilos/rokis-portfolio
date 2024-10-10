from django.test import TestCase

from apps.user.models import User
from apps.user.tests.factories import UserFactory


class TestUser(TestCase):
    def test_str(self):
        user = UserFactory()
        self.assertEqual(str(user), user.email)

    def test_portfolio_count(self):
        user = UserFactory()
        self.assertEqual(user.portfolio_count, user.portfolios.count())

    def test_create_user(self):
        user = User.objects.create_user(
            email="example@example.com",
            password="password",
        )
        self.assertEqual(user.email, "example@example.com")
        self.assertTrue(user.check_password("password"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="example@example.com",
            password="password",
        )
        self.assertEqual(user.email, "example@example.com")
        self.assertTrue(user.check_password("password"))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
