# Pedir la edad y las respuestas de autorizacion e identificacion.
edad = int(input("Introduce tu edad: "))
autorizacion = input("¿Tienes autorización? (sí/no): ")
identificacion = input("¿Tienes identificación? (sí/no): ")

# strip quita espacios externos y lower convierte la respuesta a minusculas.
# Se aceptan las formas con tilde y sin tilde de una respuesta afirmativa.
tiene_autorizacion = autorizacion.strip().lower() in ("sí", "si")
tiene_identificacion = identificacion.strip().lower() in ("sí", "si")
# La comparacion produce True si la edad es al menos 18, y False en otro caso.
es_mayor_de_edad = edad >= 18
# and exige que las tres condiciones sean verdaderas a la vez.
acceso_completo = es_mayor_de_edad and tiene_autorizacion and tiene_identificacion
# or basta con que se cumpla una de las dos condiciones.
acceso_supervisado = tiene_autorizacion or es_mayor_de_edad
# not invierte el valor: queda bloqueado si no tiene identificacion.
acceso_bloqueado = not tiene_identificacion

# Mostrar cada resultado booleano (True o False).
print(es_mayor_de_edad)
print(acceso_completo)
print(acceso_supervisado)
print(acceso_bloqueado)