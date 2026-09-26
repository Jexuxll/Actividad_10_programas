# Pedir los datos necesarios para calcular el coste de la compra.
nombre = input("Nombre del producto: ")
# float permite introducir precios y porcentajes con decimales.
precio_uni = float(input("Precio unitario: "))
# La cantidad de unidades se representa con un numero entero.
cantidad = int(input("Cantidad: "))
porcentaje_iva = float(input("Introduce el porcentaje de IVA: "))

# Calcular el importe antes de impuestos multiplicando precio por cantidad.
total_no_iva = precio_uni * cantidad
# Pasar el porcentaje a fraccion decimal y aplicarlo al importe.
iva = total_no_iva * (porcentaje_iva / 100)
# Sumar el impuesto al subtotal para obtener el importe final.
total_con_iva = total_no_iva + iva

# Mostrar el resumen; .2f presenta los importes con dos decimales.
print("\n--------- Presupuesto ---------")
print(f"Nombre: {nombre}")
print(f"Total sin IVA: {total_no_iva:.2f}")
print(f"IVA: {iva:.2f}")
print(f"Total con IVA: {total_con_iva:.2f} \n")