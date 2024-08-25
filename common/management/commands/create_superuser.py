from decouple import config
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **options):
        username = config('DJANGO_SUPERUSER_USERNAME', default=None)
        email = config('DJANGO_SUPERUSER_EMAIL', default=None)
        password = config('DJANGO_SUPERUSER_PASSWORD', default=None)

        if not username or not email or not password:
            self.stdout.write(self.style.WARNING(
                "Please provide DJANGO_SUPERUSER_USERNAME, "
                "DJANGO_SUPERUSER_EMAIL, and DJANGO_SUPERUSER_PASSWORD."
            ))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(
                f"Superuser {username} created successfully."
            ))
        else:
            self.stdout.write(self.style.WARNING(
                f"Superuser {username} already exists."
            ))
