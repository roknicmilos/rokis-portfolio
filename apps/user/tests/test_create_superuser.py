import os
from unittest.mock import patch
from django.core.management import call_command
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateSuperuserCommandTests(TestCase):

    def setUp(self):
        super().setUp()
        self.mock_write_patcher = patch(
            'django.core.management.base.OutputWrapper.write'
        )
        self.mock_write = self.mock_write_patcher.start()

    @patch.dict(os.environ, {
        'DJANGO_SUPERUSER_USERNAME': '',
        'DJANGO_SUPERUSER_EMAIL': '',
        'DJANGO_SUPERUSER_PASSWORD': '',
    })
    def test_handle_no_environment_variables(self):
        call_command('create_superuser')
        self.mock_write.assert_called_once_with(
            'Please provide DJANGO_SUPERUSER_USERNAME, '
            'DJANGO_SUPERUSER_EMAIL, and DJANGO_SUPERUSER_PASSWORD.'
        )

    @patch.dict(os.environ, {
        'DJANGO_SUPERUSER_USERNAME': 'testuser',
        'DJANGO_SUPERUSER_EMAIL': 'testuser@example.com',
        'DJANGO_SUPERUSER_PASSWORD': 'testpass123',
    })
    def test_handle_superuser_already_exists(self):
        User.objects.create_superuser(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        call_command('create_superuser')
        self.mock_write.assert_called_once_with(
            'Superuser testuser already exists.'
        )

    @patch.dict(os.environ, {
        'DJANGO_SUPERUSER_USERNAME': 'testuser',
        'DJANGO_SUPERUSER_EMAIL': 'testuser@example.com',
        'DJANGO_SUPERUSER_PASSWORD': 'testpass123',
    })
    def test_handle_superuser_created_successfully(self):
        call_command('create_superuser')
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.mock_write.assert_called_once_with(
            'Superuser testuser created successfully.'
        )

    def tearDown(self):
        super().tearDown()
        self.mock_write_patcher.stop()
