# Conversion de tipos de datos

# Convertir de cadena a numero
numero_cadena = "10"
numero_entero = int(numero_cadena)

# Convertir de cadena a numero decimal
numero_cadena2 = "3.14"
numero_decimal = float(numero_cadena2)

# Convertir de numero a cadena
numero_entero2 = 25
numero_cadena2 = str(numero_entero2)

# Convertir a booleano
# Tipo bool es False en los siguientes casos:
# Si el valor es 0, cadena vacia o None, entonces regresa False
# Regresa True, si el valor es distinto de 0, si es distinto de cadena vacia y tambien si es distinto de None
numero_entero3 = 0
booleano = bool(numero_entero3)
print(f"Valor booleano de 0: {booleano}") # False

numero_entero4 = 5
booleano2 = bool(numero_entero4)
print(f"Valor booleano de 0: {booleano2}") # True

cadena = ""
booleano3 = bool(cadena)
print(f"Valor booleano de \"\": {booleano3}") # False

cadena2 = " "
booleano4 = bool(cadena2)
print(f"Valor booleano de \" \": {booleano4}") # True

variable = None
booleano5 = bool(variable)
print(f"Valor booleano de None: {booleano5}") # False