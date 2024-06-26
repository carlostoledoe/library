from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)


class Producto(models.Model):
    descripcion = models.CharField(max_length=50)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)



'''
Consulta los productos de clientes:
-----------------------------------

En terminal:
python manage.py makemigrations
python manage.py migrate
python manage.py shell

from cliente_producto.models import Cliente, Producto

c1 = Cliente(nombre='Juan', correo='aaa@bbb.ccc')
p1 = Producto(descripcion='Lavadora', cliente=c1)
p2 = Producto(descripcion='Televisor', cliente=c1)
p3 = Producto(descripcion='Plancha', cliente=c1)

c1.save()
p1.save()
p2.save()
p3.save()


cliente = Cliente.objects.get(id=1)
productos = cliente.producto_set.all()
for producto in productos:
	print(producto.descripcion)
'''