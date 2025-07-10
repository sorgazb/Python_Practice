# Sistema generador de Emails

nombre_usuario = input("Nombre usuario: ")
nombre_normalizado = nombre_usuario.strip().lower()
nombre_normalizado = nombre_normalizado.replace(" ",".")
nombre_normalizado = nombre_normalizado+'.'

apellidos_usuario = input("Apellidos usuario: ")
apellidos_normalizado = apellidos_usuario.strip().lower()
apellidos_normalizado = apellidos_normalizado.replace(" ",".")

empresa = input("Empresa usuario: ")
empresa_normalizado = empresa.strip().lower()
empresa_normalizado = empresa_normalizado.replace(" ", "")

dominio = ".com.es"

dominio_empresa = "".join(["@", empresa_normalizado, dominio])

correo_electronico = "".join([nombre_normalizado, apellidos_normalizado, dominio_empresa])

print("*** Generador de Email ***")
print(f"Email final generado: {correo_electronico}")