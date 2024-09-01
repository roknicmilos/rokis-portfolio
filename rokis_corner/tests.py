from unittest.mock import patch

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from apps.common.tests import FlashMessagesMixin
from apps.user.models import Subscriber


class TestIndexView(FlashMessagesMixin):
    url_path = reverse_lazy('index')

    def test_valid_email_creates_subscriber_and_returns_200(self):
        email = 'valid@example.com'
        self.assertFalse(Subscriber.objects.filter(email=email).exists())

        response = self.client.post(
            path=self.url_path,
            data={'email': email},
            follow=True
        )

        self.assertTrue(Subscriber.objects.filter(email=email).exists())
        self.assertSuccessFlashMessage(
            response=response,
            message=_('Successfully subscribed!')
        )

    def test_invalid_email_returns_400_and_no_subscriber_created(self):
        response = self.client.post(
            path=self.url_path,
            data={'email': 'invalid-email'}
        )

        self.assertEqual(Subscriber.objects.count(), 0)
        self.assertErrorFlashMessage(
            response=response,
            message=_('Invalid email address!')
        )

    def test_existing_email_does_not_create_subscriber_and_returns_200(self):
        email = 'existing@example.com'
        Subscriber.objects.create(email=email)

        response = self.client.post(
            path=self.url_path,
            data={'email': email}
        )

        self.assertEqual(Subscriber.objects.count(), 1)
        self.assertSuccessFlashMessage(
            response=response,
            message=_('Successfully subscribed!')
        )

    @patch('apps.user.views.SubscriberForm.create_subscriber')
    def test_server_error_returns_500(self, mock_save):
        mock_save.side_effect = Exception("Test server error")

        response = self.client.post(
            path=self.url_path,
            data={'email': 'error@example.com'}
        )

        self.assertEqual(Subscriber.objects.count(), 0)
        self.assertErrorFlashMessage(
            response=response,
            message=_('Internal server error!')
        )
