from django.core.management.base import BaseCommand
from registro_conductores.services import *

# Se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        crear_conductor('María', 'Rojas', '2000-09-09')
