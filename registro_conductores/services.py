from registro_conductores.models import Conductor, Direccion, Vehiculo

def crear_conductor(nombre:str, apellido:str, fecha_nac):
    c = Conductor(nombre=nombre, apellido=apellido, fecha_nac=fecha_nac)
    c.save()

def agregar_direccion_a_conductor():
    pass

def agregar_un_vehiculo():
    pass

def eliminar_vehiculo():
    pass

def eliminar_conductor():
    pass

