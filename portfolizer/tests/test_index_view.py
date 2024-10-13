from django.urls import reverse_lazy, reverse

from apps.common.tests import FlashMessagesMixin
from apps.common.utils import get_model_admin_change_list_url
from apps.portfolio.models import Portfolio
from apps.portfolio.tests.factories import PortfolioFactory
from apps.user.tests.factories import UserFactory


class TestIndexView(FlashMessagesMixin):
    url_path = reverse_lazy("index")

    def assertResponse(self, response, portfolio_url: str = None) -> None:
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertEqual(response.context.get("portfolio_url"), portfolio_url)

    def test_page_for_anonymous_user(self):
        response = self.client.get(self.url_path)
        self.assertResponse(response)

    def test_page_for_authenticated_user_without_portfolio(self):
        # When authenticated user doesn't have a portfolio:
        user = UserFactory.create_staff_user()
        self.client.force_login(user)

        response = self.client.get(self.url_path)

        portfolio_admin_list_url = get_model_admin_change_list_url(
            model_class=Portfolio
        )
        self.assertResponse(response, portfolio_url=portfolio_admin_list_url)

        # When authenticated user has unpublished portfolio:
        portfolio = PortfolioFactory(user=user, is_published=False)

        response = self.client.get(self.url_path)

        self.assertResponse(response, portfolio_url=portfolio_admin_list_url)

        # When authenticated user has published portfolio:
        portfolio.update(is_published=True)

        response = self.client.get(self.url_path)

        portfolio_url = reverse(
            viewname="portfolio:index", kwargs={"slug": portfolio.slug}
        )
        self.assertResponse(response, portfolio_url=portfolio_url)
