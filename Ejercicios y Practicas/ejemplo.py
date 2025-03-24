saldo = 1000

while True:
    print("\nMenú de opciones:")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion.isdigit():
        opcion = int(opcion)
        if 1 <= opcion <= 4:
            if opcion == 1:
                print(f"Saldo actual: ${saldo}")
            elif opcion == 2:
                cantidad = float(input("Ingrese la cantidad a retirar: $"))
                if cantidad <= saldo:
                    saldo -= cantidad
                    print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
                else:
                    print("Saldo insuficiente.")
            elif opcion == 3:
                cantidad = float(input("Ingrese la cantidad a depositar: $"))
                saldo += cantidad
                print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
            elif opcion == 4:
                print("Gracias por usar el cajero automático.")
                break
        else:
            print("Opción inválida. Ingrese un número entre 1 y 4.")
    else:
        print("Entrada inválida. Ingrese un número.")

##Ejercicio herencia 
import math

class figura:
    def calcular_area(self):
        pass

class cuadrado(figura):
    def calcular_area(self,lado1,lado2):
        return lado1 * lado2
        
class rectangulo(figura):
    def calcular_area(self,base,altura):
        return base*altura
        
class circulo(figura):
    def calcular_area(self, radio):
        return math.pi *radio 
    
area_cuadrado= cuadrado()
area_rectangulo= rectangulo()
area_circulo= circulo()

print(area_circulo.calcular_area(2))