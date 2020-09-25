from django.core.management.base import BaseCommand

# python manage.py help
# python manage.py help commandname


class Command(BaseCommand):
    help = 'this is a custom management command'

    def handle(self, *args, **kwargs):
        print('command starts')
