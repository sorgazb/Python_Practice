# Ejercicio para generar id unicios
from random import randint

print("*** Sistema Generador de ID Unico")
nombre = input("Cual es tu nombre? ")
apellido = input("Cual es tu apellido? ")
anio_nacimiento = input("Cual es tu año de nacimiento? ")
print()
subcadena_nombre = nombre.strip().upper()[0:2]
subcadena_apellido = apellido.strip().upper()[0:2]
subcadena_anio = anio_nacimiento[2:4]
numero_aleatorio = str(randint(1000,9999))

id_unico = "".join([subcadena_nombre,subcadena_apellido, subcadena_anio, numero_aleatorio])

print(f"Hola {nombre}")
print(f'''\tTu nuevo numero de identificiacion (ID) generado por el sistema es:
\t{id_unico}
\tFelicidades!''')