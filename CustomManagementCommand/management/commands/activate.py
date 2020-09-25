from django.core.management.base import BaseCommand
from CustomManagementCommand.models import SampleCommand


class Command(BaseCommand):
    help = 'activate all unactivate commands'

    def handle(self, *args, **kwargs):
        size = SampleCommand.objects.filter(activated=False).count()

        if size != 0:
            qs = SampleCommand.objects.filter(activated=False)
            count = 0
            for obj in qs:
                count += 1
                obj.activated = True
                obj.save()
            print(f"activated {count} commands")
        else:
            print("no commands to activate")

# run 'python manage.py activate' check you SampleCommand objects are now activated
