from django.test import TestCase
from django.urls import reverse_lazy
from unittest.mock import patch

from apps.user.models import Subscriber


class TestSubscribeView(TestCase):
    url_path = reverse_lazy('user:subscribe')

    def test_valid_email_creates_subscriber_and_returns_200(self):
        email = 'valid@example.com'
        self.assertFalse(Subscriber.objects.filter(email=email).exists())

        response = self.client.post(
            path=self.url_path,
            data={'email': email}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Subscriber.objects.filter(email=email).exists())
        self.assertJSONEqual(
            response.content,
            {'message': 'Successfully subscribed'}
        )

    def test_invalid_email_returns_400_and_no_subscriber_created(self):
        response = self.client.post(self.url_path, {'email': 'invalid-email'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Subscriber.objects.count(), 0)
        self.assertIn('errors', response.json())

    def test_existing_email_does_not_create_subscriber_and_returns_200(self):
        email = 'existing@example.com'
        Subscriber.objects.create(email=email)

        response = self.client.post(
            path=self.url_path,
            data={'email': email}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Subscriber.objects.count(), 1)
        self.assertJSONEqual(
            response.content,
            {'message': 'Successfully subscribed'}
        )

    @patch('apps.user.views.SubscriberForm.create_subscriber')
    def test_server_error_returns_500(self, mock_save):
        mock_save.side_effect = Exception("Test server error")

        response = self.client.post(
            path=self.url_path,
            data={'email': 'error@example.com'}
        )

        self.assertEqual(response.status_code, 500)
        self.assertEqual(Subscriber.objects.count(), 0)
        self.assertJSONEqual(
            response.content,
            {'message': 'Internal server error'}
        )
