from django.test import TestCase

from apps.user.tests.factories import UserFactory


class TestUser(TestCase):
    def test_str(self):
        user = UserFactory()
        self.assertEqual(str(user), user.email)

    def test_portfolio_count(self):
        user = UserFactory()
        self.assertEqual(user.portfolio_count, user.portfolios.count())
