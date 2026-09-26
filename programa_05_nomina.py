# Pedir los datos del empleado y las cantidades necesarias para la nomina.
nombre = input("Nombre del empleado: ")
horas_trabajadas = float(input("Horas trabajadas: "))
salario_hora = float(input("Salario por hora: "))
retencion = float(input("Porcentaje de retención: "))

# El salario bruto es el pago antes de descontar la retencion.
salario_bruto = horas_trabajadas * salario_hora
# Calcular la retencion como porcentaje del salario bruto y restarla.
salario_neto = salario_bruto - salario_bruto * retencion / 100

# Mostrar el resumen de la nomina con importes a dos decimales.
print("\n--------- Nómina ---------")
print(f"Nombre: {nombre}")
print(f"Salario bruto: {salario_bruto:.2f}")
print(f"Retención: {retencion:.2f}%")
print(f"Salario neto: {salario_neto:.2f} \n")