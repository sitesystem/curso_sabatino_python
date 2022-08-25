# EJEMPLO 2. OPERACIONES MATEMÁTICAS

# IMPORTAR LIBRERÍAS O BIBLIOTECAS QUE CONTIENEN FUNCIONES MATEMÁTICAS
import math

# ENTRADAS DE DATOS
# Declarar o crear las variables
número_1 = float(input("Escribe el 1er número: "))
número_2 = float(input("Escribe el 2do número: "))
# Declarar una Constante
PI = 3.1416

# PROCESOS (Cálculos u Operaciones Matemáticas y/o Lógicas)
suma = número_1 + número_2
resta = número_1 - número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = número_1 % número_2

# SALIDA DE DATOS
print("La suma es =", round(suma, 2))
print('La suma es = ' + str(suma)) # CONCATENACIÓN (Unión o juntar dos o más Textos)
# CASTEO: Conversión de un tipo de dato a otro tipo de dato
print(f"La suma es = {suma}") # f (Formatear el Texto)

print(f"La potencia 1 es = {potencia_1}")
print(f"La potencia 2 es = {potencia_2}")

print(f"El módulo o residuo es = {módulo_residuo}")
