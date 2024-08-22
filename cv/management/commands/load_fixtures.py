import os
import shutil

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load all fixtures'
    fixture_labels = [
        'user',
        'cv',
        'link',
        'skill',
        'language',
        'employment',
        'internship',
        'education',
        'project',
    ]

    def handle(self, *args, **options):
        call_command('loaddata', *self.fixture_labels)

        src_dir = os.path.join('cv', 'fixtures', 'img')
        dest_dir = os.path.join('media', 'cv', 'img')
        self._upload_media_files(src_dir, dest_dir)

    def _upload_media_files(self, src_dir: str, dest_dir: str):
        # Ensure the destination directory exists
        os.makedirs(dest_dir, exist_ok=True)

        # Copy all files from src_dir to dest_dir
        for filename in os.listdir(src_dir):
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dest_file)

        self.stdout.write(self.style.SUCCESS(
            f'Successfully copied files from {src_dir} to {dest_dir}'
        ))
