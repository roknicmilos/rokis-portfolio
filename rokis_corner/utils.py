import sentry_sdk
from decouple import config


def init_sentry_sdk():
    if not (sentry_dsn := config("SENTRY_DSN", default=None)):
        return

    if not (sentry_env := config("SENTRY_ENV", default=None)):
        return

    if sentry_env not in ["local", "dev", "prod"]:
        raise ValueError(
            "Invalid SENTRY_ENV value. Must be one of: "
            "'local', 'dev', or 'prod'"
        )

    sentry_sdk.init(
        dsn=sentry_dsn,
        environment=sentry_env,
        debug=config("DEBUG", default=False, cast=bool),
        traces_sample_rate=config(
            "SENTRY_TRACES_SAMPLE_RATE", default=1.0, cast=float
        ),
        profiles_sample_rate=config(
            "SENTRY_PROFILES_SAMPLE_RATE", default=1.0, cast=float
        ),
    )
