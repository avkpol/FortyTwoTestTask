from django.core.management.base import BaseCommand, CommandError
from django.apps import apps




class Command(BaseCommand):

    help = 'Displays all apps models list '

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        app_models = apps.get_app_config('avkpol4').get_models(include_auto_created=True)

        for model in app_models:
            if model:
                mod_obj_count = len(model.objects.all())
                mod_name = model.__name__
                self.stdout.write('There are %s objects in model %s' % (mod_obj_count, mod_name))
            else:
                self.stderr.write('Error:'+"Application still doesn't have any registered models")
