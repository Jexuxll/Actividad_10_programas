# Leer las medidas del rectangulo como numeros decimales.
base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))

# El area es el producto de la base por la altura.
area = base * altura
# El perimetro suma sus cuatro lados: dos bases y dos alturas.
perimetro = 2 * (base + altura)
# La diagonal se obtiene con el teorema de Pitagoras.
longitud_diagonal = (base**2 + altura**2)**0.5

# Mostrar las tres medidas calculadas con dos cifras decimales.
print("\n--------- Datos del rectángulo ---------")
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
print(f"Longitud de la diagonal: {longitud_diagonal:.2f} \n")