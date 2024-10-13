import os
from unittest.mock import patch
from django.test import TestCase

from portfolizer.utils import init_sentry_sdk


class TestInitSentrySdk(TestCase):
    def setUp(self):
        super().setUp()
        self.sentry_sdk_init_patcher = patch("sentry_sdk.init")
        self.mock_sentry_init = self.sentry_sdk_init_patcher.start()

    @patch.dict(
        os.environ,
        {
            "SENTRY_DSN": "",
            "SENTRY_ENV": "dev",
        },
    )
    def test_no_sentry_dsn(self):
        init_sentry_sdk()
        self.mock_sentry_init.assert_not_called()

    @patch.dict(
        os.environ,
        {
            "SENTRY_DSN": "http://example.com",
            "SENTRY_ENV": "",
        },
    )
    def test_no_sentry_env(self):
        init_sentry_sdk()
        self.mock_sentry_init.assert_not_called()

    @patch.dict(
        os.environ,
        {
            "SENTRY_DSN": "http://example.com",
            "SENTRY_ENV": "development",
        },
    )
    def test_invalid_sentry_env(self):
        with self.assertRaises(ValueError) as context:
            init_sentry_sdk()

        self.assertEqual(
            str(context.exception),
            "Invalid SENTRY_ENV value. Must be one of: "
            "'local', 'dev', or 'prod'",
        )
        self.mock_sentry_init.assert_not_called()

    @patch.dict(
        os.environ,
        {
            "SENTRY_DSN": "http://example.com",
            "SENTRY_ENV": "prod",
            "DEBUG": "false",
            "SENTRY_TRACES_SAMPLE_RATE": "0.5",
            "SENTRY_PROFILES_SAMPLE_RATE": "0.25",
        },
    )
    def test_sentry_initialization(self):
        init_sentry_sdk()
        self.mock_sentry_init.assert_called_once_with(
            dsn="http://example.com",
            environment="prod",
            debug=False,
            traces_sample_rate=0.5,
            profiles_sample_rate=0.25,
        )

    def tearDown(self):
        super().tearDown()
        self.sentry_sdk_init_patcher.stop()
