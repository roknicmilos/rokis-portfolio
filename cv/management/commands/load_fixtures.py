from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load all fixtures'

    def handle(self, *args, **options):
        fixture_labels = [
            'user',
            'cv',
            'link',
            'skill',
            'language',
            'employment',
            'internship',
            'education',
        ]
        call_command('loaddata', *fixture_labels)
