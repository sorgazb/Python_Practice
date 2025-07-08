# Inmutabilidad en cadenas

cadena1 = "Hola mundo"
# cadena1[0] = "h" , no podemos modificar los caracteres
cadena2 = cadena1
cadena1 = "Adios"
print(cadena2)
print(cadena1)
