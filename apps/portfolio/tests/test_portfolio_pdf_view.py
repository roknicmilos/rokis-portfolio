from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from apps.portfolio.tests.factories import PortfolioFactory


class TestPortfolioPDFView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.portfolio = PortfolioFactory(is_published=True)

    def setUp(self):
        super().setUp()
        self.left_segments_patch = patch(
            target='apps.portfolio.service.get_left_column_segments',
            return_value=[],
        )
        self.mock_left_segments = self.left_segments_patch.start()

        self.right_segments_patch = patch(
            target='apps.portfolio.service.get_right_column_segments',
            return_value=[],
        )
        self.mock_right_segments = self.right_segments_patch.start()

    def assertResponseContext(self, response) -> None:
        self.assertEqual(response.context.get('portfolio'), self.portfolio)
        if self.portfolio.avatar:
            self.assertEqual(
                response.context.get('avatar_url'),
                self.portfolio.avatar.url
            )
        else:
            self.assertEqual(response.context.get('avatar_url'), '')

        # Assert that the left and right column segments:
        self.mock_left_segments.assert_called_once_with(
            portfolio=self.portfolio
        )
        self.mock_right_segments.assert_called_once_with(
            portfolio=self.portfolio
        )
        self.assertEqual(response.context.get('left_column'), [])
        self.assertEqual(response.context.get('right_column'), [])

        self.assertEqual(
            response.context.get('portfolio_pdf_url'),
            reverse(
                viewname='portfolio:pdf',
                kwargs={'slug': self.portfolio.slug}
            )
        )

    def test_get_html_response(self):
        url_path = reverse(
            viewname='portfolio:index',
            kwargs={'slug': self.portfolio.slug}
        )
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')
        self.assertResponseContext(response)

    def test_get_pdf_response(self):
        url_path = reverse(
            viewname='portfolio:pdf',
            kwargs={'slug': self.portfolio.slug}
        )
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'inline; filename="{self.portfolio.filename}"'
        )
        self.assertResponseContext(response)

    def test_get_download_response(self):
        url_path = reverse(
            viewname='portfolio:download',
            kwargs={'slug': self.portfolio.slug}
        )
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{self.portfolio.filename}"'
        )
        self.assertResponseContext(response)

    def test_404_response(self):
        url_path = reverse(
            viewname='portfolio:index',
            kwargs={'slug': 'non-existing-slug'}
        )
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        super().tearDown()
        self.left_segments_patch.stop()
        self.right_segments_patch.stop()
