import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # Django command to pause execution until database is available
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_con = None
        tried = 1
        while not db_con and tried <= 20:
            try:
                db_con = connections['default']
            except OperationalError:
                self.stdout.write(f'Database unavailable, waiting {tried} second(s)')
                time.sleep(1 * tried)
                tried += 1
        
        self.stdout.write(self.style.SUCCESS('Database is available'))
