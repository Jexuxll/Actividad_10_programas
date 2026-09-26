# Pedir los datos del cliente y de los articulos que aparecen en el ticket.
nombre_cliente = input("Nombre del cliente: ")
nombre_producto = input("Nombre del producto: ")
precio_unitario = float(input("Precio del producto: "))
cantidad = int(input("Cantidad del producto: "))
# Los porcentajes se introducen como numeros (por ejemplo, 21 para un 21 %).
porcentaje_descuento = float(input("Porcentaje de descuento: "))
porcentaje_iva = float(input("Porcentaje de IVA: "))

# Calcular primero el coste de todas las unidades, antes de descuentos e IVA.
subtotal = precio_unitario * cantidad
# Aplicar el descuento porcentual al subtotal.
descuento = subtotal * (porcentaje_descuento / 100)
# Restar el descuento para obtener la base sobre la que se calcula el IVA.
total_con_descuento = subtotal - descuento
# Calcular el IVA sobre el total que ya tiene aplicado el descuento.
iva = total_con_descuento * (porcentaje_iva / 100)
# Sumar el IVA al total con descuento para obtener el importe a pagar.
total_a_pagar = total_con_descuento + iva

# Imprimir el desglose; .2f muestra los importes monetarios con dos decimales.
print("----- TICKET DE COMPRA -----")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {nombre_producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: {precio_unitario:.2f} €")
print(f"Subtotal: {subtotal:.2f} €")
print(f"Descuento: {descuento:.2f} €")
print(f"Total con descuento: {total_con_descuento:.2f} €")
print(f"IVA: {iva:.2f} €")
print(f"Total a pagar: {total_a_pagar:.2f} €\n")
