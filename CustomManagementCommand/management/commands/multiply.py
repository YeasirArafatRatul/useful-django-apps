from django.core.management.base import BaseCommand
from CustomManagementCommand.models import SampleCommand


class Command(BaseCommand):
    help = 'multiply count'

    def add_arguments(self, parser):
        parser.add_argument('param', type=int)

    def handle(self, *args, **options):
        param = options.get('param')
        count = SampleCommand.objects.all().count()

        multiply = count * param

        print(multiply)
        # run 'python manage.py multipy intergerParameter check you SampleCommand objects are now activated
