# Roki's Corner

**Roki's Corner** is a web application built with Django that enables users to
create, customize, and manage their portfolio pages. Users can easily generate
and download their portfolios as CVs in PDF format, providing a convenient way
to showcase their professional experience and skills.

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Project Setup

1. Clone the repository:
    ```bash
    git clone git@github.com:roknicmilos/rokis-corner.git
    ```

2. Create file with environment variables:
    ```bash
    cp example.env .env
    ```
   There is no need to change anything in the `.env` file for the **development
   environment**. However, you can change the values of the variables if you
   want to run the project in a different environment.
   <br/><br/>

3. Start Docker containers:
    ```bash
    docker-compose up -d
    ```
   To start the project in the **production environment**, run the following
   command:
    ```bash
    docker-compose -f docker-compose.prod.yaml up -d
    ```

## Enable Sentry

To enable Sentry error tracking, set the `SENTRY_DSN` and `SENTRY_ENV` variables
in the `.env` file.

Check
[Client Keys (DSN)](https://rokis-corner.sentry.io/settings/projects/rokis-corner/keys/)
in the Sentry project settings to get the DSN.

Use one of the following values for the `SENTRY_ENV` variable: `local`, `dev` or
`prod`.

To check the issues for this project on Sentry, click
[here](https://rokis-corner.sentry.io/issues/?project=4508003751821312&referrer=sidebar&statsPeriod=14d).

## Enable Google Analytics

To enable Google Analytics, set the `GOOGLE_ANALYTICS_TRACKING_ID` variable in
the `.env` file.

To get the tracking ID, visit:
[Roki's Corner DEV data stream](https://analytics.google.com/analytics/web/#/a152537310p460818596/admin/streams/table/9749560985)
or
[Roki's Corner PROD data stream](https://analytics.google.com/analytics/web/#/a152537310p215621886/admin/streams/table/9749678510)
at [Google Analytics](https://analytics.google.com/).

## Test Data

The project includes test data in the form of Django fixtures. The fixtures are
located in the `fixtures` directories in each Django app. You can load the
fixtures using the following command:

```bash
poetry run python manage.py load_fixtures
```

You can now check out Eric's Cartman portfolio page at
http://localhost:8000/eric-cartman/

### Create Superuser

To create a superuser with credentials defined in the `.env` file, run the
following command:

```bash
poetry run python manage.py create_superuser
```

You can now access the Django Admin at http://localhost:8000/admin/ and log in
with the superuser credentials defined in the `.env` file.

## Run Tests

Run the tests with the following command:

```bash
poetry run pytest
```

Check `tox.ini` file for more information about the test configuration.

## Setup pre-commit hooks

This project uses [pre-commit](https://pre-commit.com/) to manage and run
pre-commit hooks. To install the pre-commit hooks, run the following command:

```bash
poetry run pre-commit install
```

Check `.pre-commit-config.yaml` file for more information about the pre-commit
hooks configuration.
