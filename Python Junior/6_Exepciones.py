#######################################
'''
EXEPCIONES COMUNES

ZeroDivisionError: Se produce cuando se intenta dividir un número entre cero.
TypeError: Se produce cuando se realiza una operación con tipos de datos incompatibles.
ValueError: Se produce cuando se pasa un valor no válido a una función.
IndexError: Se produce cuando se intenta acceder a un índice fuera de rango en una lista o tupla.
FileNotFoundError: Se produce cuando se intenta abrir un archivo que no existe.
NameError: Se produce cuando se intenta utilizar una variable que no ha sido definida.
KeyError: Se produce cuando se intenta acceder a una clave que no existe en un diccionario.

'''
#######################################
'''
EJEMPLO
'''
#######################################
try:
    resultado = 10 / 'hola'  # Esto generará una excepción ZeroDivisionError
except TypeError:
    print("No se puede dividir numeros con letras")
finally:
    print("Este bloque siempre se ejecuta.")
######################################
'''
EXEPCIONES PRIPIAS CON RISE
'''
######################################
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as triger:
    print(triger)