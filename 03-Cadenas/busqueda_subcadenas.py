# Busqueda de Subcadenas

cadena = "Hola, mundo!"
indice_mundo = cadena.find("mundo")

print(f"Indice de la subcadena mundo: {indice_mundo}")

# Obtener el indice de la subcadena de Hola
indice_hola = cadena.find("hola")
print(f"Indice de la subcadena hola: {indice_hola}")
# Python es sensible a mayusculas y minusculas
indice_Hola = cadena.find("Hola")
print(f"Indice de la subcadena Hola: {indice_Hola}")