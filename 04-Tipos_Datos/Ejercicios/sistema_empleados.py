# Sistema de empleados

print("*** SISTEMA DE EMPLEADOS ***")
nombre_empleado = input("Nombre del empleado: ")
edad_empleado = int(input("Edad del empleado: "))
salario_empleado = float(input("Salario del empleado: "))
es_jefe_departamento = input("Es jefe de departamento (Si/No)? ")

# Convertir a tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si' # Si son iguales el valor es True y False en el caso contrario

# Imprimir los valores del Empleado
print("\nDatos del empleado: ")
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salario: {salario_empleado:.2f}")
print(f"Es jefe de departamento?: {es_jefe_departamento}")