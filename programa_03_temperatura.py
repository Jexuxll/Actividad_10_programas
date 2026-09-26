# Leer la temperatura en Celsius como numero decimal.
temperatura = float(input("Introduce la temperatura en grados Celsius: "))
# Conversion de Celsius a Fahrenheit: (C * 9/5) + 32.
temp_fahr = (temperatura * 9/5) + 32
# Para convertir Celsius a Kelvin se suman 273.15 grados.
temp_Kelvin = temperatura + 273.15

# Mostrar ambas conversiones con dos cifras decimales.
print("\n--------- Conversor de temperatura ---------")
print(f"Temperatura en Fahrenheit: {temp_fahr:.2f}")
print(f"Temperatura en Kelvin: {temp_Kelvin:.2f} \n")