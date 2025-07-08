# Ejercicio de generacion de cuentas email

nombre_usuario = "Sergio Orgaz Bravo"
nombre_normalizado = nombre_usuario.lower()
nombre_normalizado = nombre_normalizado.replace(" ",".")

empresa = "NTT Data"
empresa_normalizado = empresa.lower()
empresa_normalizado = empresa_normalizado.replace(" ", "")

dominio = ".com.es"

dominio_empresa = "".join(["@", empresa_normalizado, dominio])

correo_electronico = "".join([nombre_normalizado, dominio_empresa])

print("*** Generador de Email ***")
print(f"Nombre usuario: {nombre_usuario}")
print(f"Nombre usuario normalizado: {nombre_normalizado}")
print()
print(f"Nombre empresa: {empresa}")
print(f"Extension del dominio: {dominio}")
print(f"Dominio de emeail normalizado: {dominio_empresa}")
print(f"Email final generado: {correo_electronico}")