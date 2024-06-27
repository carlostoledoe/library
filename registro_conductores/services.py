from registro_conductores.models import Conductor, Direccion, Vehiculo

def crear_conductor(nombre:str, apellido:str, fecha_nac):
    c = Conductor(nombre=nombre, apellido=apellido, fecha_nac=fecha_nac)
    c.save()
    imprimir_modelos()

def agregar_direccion_a_conductor(calle, numero, comuna, region, conductor_id):
    d = Direccion(calle=calle, numero=numero, comuna=comuna, region=region, conductor_id=conductor_id)
    d.save()
    imprimir_modelos()

def agregar_un_vehiculo():
    pass

def eliminar_vehiculo():
    pass

def eliminar_conductor():
    pass

def imprimir_modelos():
    conductores = Conductor.objects.all()
    direcciones = Direccion.objects.all()
    print(conductores)
    print(direcciones)