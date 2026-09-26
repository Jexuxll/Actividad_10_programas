# Leer la duracion total en segundos como un numero entero.
segundos = int(input("Introduce el tiempo en segundos: "))
# // obtiene los minutos completos y % obtiene los segundos que sobran.
minutos = segundos // 60
segundos_restantes = segundos % 60
# Repetir la division para separar las horas de los minutos sobrantes.
horas = minutos // 60
minutos_restantes = minutos % 60

# Mostrar el tiempo como HH:MM:SS; 02 reserva dos posiciones con ceros.
print("\n--------- Conversor de tiempo ---------")
print(f"Tiempo: {horas:02}:{minutos_restantes:02}:{segundos_restantes:02} \n")