from django.core.management.base import BaseCommand
from books_and_authors.models import Client

# Se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Probamos que se pueda agregar un nuevo Cliente
        c = Client(first_name='Maria', last_name='Rojas', email='mmm@ccc.com', height=1.54)
        c.save()
        print('Cliente Creado')