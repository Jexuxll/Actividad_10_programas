# Leer cuantas entradas hay y entre cuantos grupos se reparten.
entradas_disponibles = int(input("Introduce el número de entradas disponibles: "))
grupos_con_entrada = int(input("Introduce el número de grupos con entrada: "))

# // calcula cuantas entradas completas recibe cada grupo.
entradas_por_grupo = entradas_disponibles // grupos_con_entrada
# % calcula las entradas que no se pueden repartir por igual.
entradas_restantes = entradas_disponibles % grupos_con_entrada

# Presentar el reparto y el sobrante.
print("\n--------- Distribución de entradas ---------")
print(f"Entradas por grupo: {entradas_por_grupo}")
print(f"Entradas restantes: {entradas_restantes} \n")