# Solicitar los datos personales al usuario.
nombre = input("Nombre completo: ")
# Convertir la edad a un número entero.
edad = int(input("Edad: "))
# Convertir la altura a un número decimal.
altura = float(input("Altura en metros: "))
# Los datos de texto se guardan directamente como cadenas.
ciudad = input("Ciudad de residencia: ")
experiencia = input("¿Tienes experiencia programando? ")

# Mostrar los datos de forma ordenada, uno por línea.
print("\n--- Ficha personal ---")
print("Nombre completo: " + nombre)
# Convertir el número a texto para poder concatenarlo con una etiqueta.
print("Edad: " + str(edad))
print("Altura: " + str(altura) + " m")
print("Ciudad de residencia: " + ciudad)
print("Experiencia programando: " + experiencia)
# type() permite comprobar qué tipo de dato se guardó en cada variable.
print("Tipo de edad: " + str(type(edad)))
print("Tipo de altura: " + str(type(altura)) + " \n")
