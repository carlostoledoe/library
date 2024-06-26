from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    height = models.DecimalField(decimal_places=2, max_digits=3)
    active = models.BooleanField(default=True)
    # Marcas temporales
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

'''
Desde el terminal, crear un Cliente:

c = Client.objects.create(
    first_name= 'Juan',
    last_name= 'Perez',
    email= 'aaa@bbb.ccc',
    height= 1.80
)
c.created
c.email = 'hola@hola.com'
c.update
'''