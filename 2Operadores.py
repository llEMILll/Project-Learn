##OPERADORES ARITMETICOS
x = 10
y = 3

suma = x + y       # Suma: 13
resta = x - y      # Resta: 7
multiplicacion = x * y  # Multiplicación: 30
division = x / y     # División: 3.333...
modulo = x % y       # Módulo (resto de la división): 1
potencia = x ** y     # Potencia: 1000
division_entera = x // y  # División entera: 3

##OPERADORES DE COMPARACIÓN
x = 5
y = 10

igual = x == y       # Igualdad: False
diferente = x != y    # Desigualdad: True
mayor_que = x > y     # Mayor que: False
menor_que = x < y     # Menor que: True
mayor_o_igual = x >= y  # Mayor o igual que: False
menor_o_igual = x <= y  # Menor o igual que: True

##OPERADORES LÓGICOS
a = True
b = False

and_logico = a and b   # AND lógico: False
or_logico = a or b    # OR lógico: True
not_logico = not a    # NOT lógico: False

##OPERADORES DE ASIGNACIÓN
x = 10          # Asignación simple
x += 5          # Suma y asignación: x = x + 5
x -= 2          # Resta y asignación: x = x - 2
x *= 3          # Multiplicación y asignación: x = x * 3
x /= 2          # División y asignación: x = x / 2
x %= 4          # Módulo y asignación: x = x % 4
x **= 2         # Potencia y asignación: x = x ** 2
x //= 3         # División entera y asignación: x = x // 3

##OPERADORES DE IDENTIDAD
x = [1, 2, 3]
y = x
z = [1, 2, 3]

es_identico = x is y     # True (x e y apuntan al mismo objeto)
no_es_identico = x is z  # False (x y z son objetos diferentes)

##OPERADORES DE PERTENENCIA
frutas = ["manzana", "banana", "naranja"]

esta_presente = "manzana" in frutas   # True
no_esta_presente = "uva" not in frutas  # True

##OPERACIONES DE BITS
a = 5  # 0101 en binario
b = 3  # 0011 en binario

and_bits = a & b   # AND bit a bit: 0001 (1 en decimal)
or_bits = a | b    # OR bit a bit: 0111 (7 en decimal)
xor_bits = a ^ b   # XOR bit a bit: 0110 (6 en decimal)
desplazamiento_izquierda = a << 1  # Desplazamiento a la izquierda: 1010 (10 en decimal)
desplazamiento_derecha = a >> 1   # Desplazamiento a la derecha: 0010 (2 en decimal)
complemento = ~a      # Complemento bit a bit: 1010 ( -6 en decimal)

