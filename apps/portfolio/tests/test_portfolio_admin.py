from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib.admin.sites import AdminSite

from apps.portfolio.admin import PortfolioAdmin
from apps.portfolio.models import Portfolio


class PortfolioAdminTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.site = AdminSite()
        self.admin = PortfolioAdmin(Portfolio, self.site)
        self.request = self.client.get("/").wsgi_request

    def test_portfolio_link_without_pk(self):
        portfolio = Portfolio(slug="test-portfolio")
        result = self.admin.portfolio_link(portfolio)
        expected = _("Save the Portfolio first to generate the link.")
        self.assertEqual(result, expected)

    def test_portfolio_link_with_pk(self):
        portfolio = Portfolio.objects.create(slug="test-portfolio")
        result = self.admin.portfolio_link(portfolio)
        expected_href = reverse(
            viewname="portfolio:index", kwargs={"slug": portfolio.slug}
        )
        expected_label = _("Display {portfolio}").format(
            portfolio=str(portfolio)
        )
        expected_html = mark_safe(
            f'<a href="{expected_href}">{expected_label}</a>'
        )
        self.assertEqual(result, expected_html)
