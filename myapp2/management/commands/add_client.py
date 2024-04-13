from django.core.management.base import BaseCommand

from myapp2.models import Client


class Command(BaseCommand):
    help = "Add client."

    def handle(self, *args, **kwargs):
        client = Client(
            name='Yura', email='pupkin_y@yexample.com', phone=78904567874,
            address='Bobruysk')
        client.save()
        self.stdout.write(f'{client}')