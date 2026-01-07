###Pin de clave de banco con bucle WHILE
"""
x=0
clave=int(input('INGRESE SU CLAVE: '))
while clave != 1234 and x<3:
   clave= int(input('Clave incorrecta ingrese nuevamente: '))
   x = x + 1
   print('intento: ', x)  
if clave == 1234:
   print('Clave correcta prosiga con su transaccion.')
"""
##Contador con bucle WHILE 
"""
x=0
while x<5:
   print(f'el numero contador es {x}')
   x+=1
"""
##For(Itera sobre cada elemento)
"""
frutas=['manzana', 'pera', 'sandia', 'uvas']
for fruta in frutas:
   print(f'Me gusta la {fruta}')
"""
##Ejercicio :Crea un programa que pida al usuario un número entero positivo 
#            y luego imprima todos los números pares desde 0 hasta ese número.

##EJERCIOS CON WHILE Y FOOR
'''
num=int(input('Ingrese un número positivo: '))
i=0
while i < num:
   if i%3==0:
      print(f'el numero par es: {i} ')
   i+=1
'''
'''
##Metodo con for
numero = int(input("Ingrese un número entero positivo: "))
for i in range(0, numero +1 ,2):
    print(i)
'''
##USAR BANDERAS BOOLEANAS PARA CERRAR BUCLE
'''
flag_bandera = True
a=0
b=0
while flag_bandera:
    # ... (código dentro del bucle) ...
      total=a+b
      a+=1
      b+=1
      
      print(total)
    # En algún momento, decides que el bucle debe terminar
      if total==10:
        break
'''
##USUARIO PUEDE CERRAR EL BUCLE
'''
respuesta = input("¿Deseas un consejo de salud? (s/n): ")
while respuesta.lower() == "s":
    print('sabias que tomar agua es saludable')
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == "n":
        break
    print('hacer ejercicio mejora tu animo y salud')
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == "n":
        break
'''
###EJERCICIO APLICANDO LAS TÉCNICAS:
##Crea un programa que le pida al usuario que adivine un número secreto entre 1 y 100. Utiliza un bucle while 
# y una de las técnicas mencionadas anteriormente para controlar cuándo termina el juego
'''
print('                          GAME: ADIVINA EL NUMERO                     ')


flag_bool= False
intentos=3

re= input("¿Desea jugar? (s/n): ")
if re.lower()=='s':
   if re.lower()=='s':
      print('Genial, bienvenido a adivina un numero del 1 al 100')
      print('Recuerda que solo tienes 4 intentos, :) suerte ')
      num_adivin=int(input('Que numero piensas que es?: '))
      if num_adivin != 25:
        while True:
           print('Intento: ', intentos)
           num_adivin = int(input('Fallaste, intentalo de nuevo: '))
           if num_adivin == 25:
              flag_bool
           elif intentos == 1:
              print('No tienes mas intentos:( ')
              break
           intentos -= 1      
      elif num_adivin ==25:
        print('Vaya eres muy intuitivo :)')
elif re.lower()=='n':
   print('Esta bien, vuelve pronto')
   flag_bool
else: 
   print('Ingresa una opción valida')

print('Espero que te haya gustado el juego :)')

'''

      





