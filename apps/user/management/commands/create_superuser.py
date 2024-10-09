from decouple import config
from django.core.management.base import BaseCommand

from apps.user.models import User


class Command(BaseCommand):
    help = "Create a superuser if it does not exist"

    def handle(self, *args, **options):
        email = config("DJANGO_SUPERUSER_EMAIL", default=None)
        password = config("DJANGO_SUPERUSER_PASSWORD", default=None)

        if not email or not password:
            self.stdout.write(
                self.style.WARNING(
                    "Please provide DJANGO_SUPERUSER_EMAIL "
                    "and DJANGO_SUPERUSER_PASSWORD."
                )
            )
            return

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email=email, password=password)
            self.stdout.write(
                self.style.SUCCESS(f"Superuser {email} created successfully.")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Superuser {email} already exists.")
            )
