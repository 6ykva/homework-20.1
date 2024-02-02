import os

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        return os.system("python manage.py loaddata data.json")
                