#Una función es un bloque de código que realiza una tarea específica. 
#La definimos con la palabra clave def, seguida del nombre de la función, paréntesis 
#(que pueden contener parámetros) y dos puntos. 
#El código de la función va indentado debajo.
def saludar(nombre):
  print(f"¡Hola, {nombre}!")

# Llamamos a la función
saludar('emil')

##PARÁMETROS Y ARGUMENTOS
    #Parámetro: son las variables que recibe la función en su definición. 
    #Argumentos: son los valores que pasamos a la función cuando la llamamos.

def sumar(a, b):  # a y b son parámetros
  return a + b

resultado = sumar(5, 3)  # 5 y 3 son argumentos
print(resultado)  # Imprime: 8

##VALORES DE RETORNO

def multiplicar(x, y):
  return x*y

producto = multiplicar(4, 6)
print(producto)  # Imprime: 24
##FUNCIONES LAMBDA
doblar = lambda b: b * 2
print(doblar(14))  # Imprime: 14

cuadrado= lambda a, b: a**b
print(cuadrado(2, 2))

##RECURSIÓN: 
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))  # Imprime: 120

