##CONDICIONALES
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres menor de edad.")

##BUCLES

############# WHILE: Se ejecuta mientras una condición sea verdadera. #############
contador = 0
while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1

############# FOR: Se ejecuta mientras una condición sea verdadera. #############
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

##CONTROL DE BUCLES

    #break : terminar el bucle inmediatamente
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es igual a 5
    print(i)

    #continue : salta a la siguiente iteracion
for i in range(10):
    if i % 2 == 0:  # Si i es par
        continue  # Salta a la siguiente iteración
    print(i)

