import sentry_sdk

from .common import *

SENTRY_DSN = config("SENTRY_DSN", default=None)
SENTRY_ENV = config("SENTRY_ENV", default=None)
if SENTRY_DSN and SENTRY_ENV:
    SENTRY_CONFIG = {
        "dsn": SENTRY_DSN,
        "environment": SENTRY_ENV,
        "debug": DEBUG,
        "traces_sample_rate": config(
            "SENTRY_TRACES_SAMPLE_RATE", default=1.0, cast=float
        ),
        "profiles_sample_rate": config(
            "SENTRY_PROFILES_SAMPLE_RATE", default=1.0, cast=float
        ),
    }

    sentry_sdk.init(**SENTRY_CONFIG)
