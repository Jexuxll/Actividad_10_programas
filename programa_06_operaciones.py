# Leer dos valores decimales para poder operar tambien con numeros no enteros.
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Estas operaciones no necesitan dividir por el segundo numero.
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
# La division y el resto no estan definidos si el divisor es cero.
# En ese caso se prepara un mensaje en vez de intentar calcularlos.
if num2 == 0:
    division_real = "No se puede calcular"
    division_entera = "No se puede calcular"
    resto = "No se puede calcular"
    potencia = "No se puede calcular"
else:
    # // divide y descarta la parte decimal; % devuelve el resto.
    # ** calcula num1 elevado a la potencia num2.
    division_real = num1 / num2
    division_entera = num1 // num2
    resto = num1 % num2
    potencia = num1 ** num2

# Mostrar todos los resultados calculados o los mensajes correspondientes.
# El formato .2f intenta presentar la potencia con dos decimales.
print("\n--------- Operaciones con 2 números ---------")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division_real}")
print(f"División entera: {division_entera}")
print(f"Resto: {resto}")
print(f"Potencia: {potencia:.2f} \n")