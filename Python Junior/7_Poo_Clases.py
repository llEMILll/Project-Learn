class Persona:
    # Constructor de la clase (se ejecuta al crear un objeto)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método para saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    # metodo para cumplir años.
    def cumpleanos(self):
        self.edad += 1
        print(f"Feliz cumpleaños numero {self.edad}, {self.nombre}!")

# Crear objetos (instancias) de la clase Persona
persona1 = Persona("Ana", 30)
persona2 = Persona("Carlos", 15)
persona3= Persona('Emil', 24)
persona4= Persona('Luna', 2)

# Acceder a los atributos y llamar a los métodos
#persona1.saludar()  # Imprime: Hola, mi nombre es Ana y tengo 30 años.
#persona2.saludar()  # Imprime: Hola, mi nombre es Carlos y tengo 25 años.
#persona3.cumpleanos() 
class Persona:
    def __init__(self, nombre, edad=None):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def desde_nacimiento(cls, nombre, año_nacimiento):
        edad = 2024 - año_nacimiento
        return cls(nombre, edad)

persona1 = Persona("Ana", 30)
persona2 = Persona.desde_nacimiento("Carlos", 1995)

print(persona1.nombre, persona1.edad)
print(persona2.nombre, persona2.edad)

#HERENCIA

class Animal:  # Clase padre
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Sonidos de animal")

class Perro(Animal):  # Clase hijo
    def hablar(self):  # Sobrescritura de método
        print("Guau!")

class Gato(Animal):  # Clase hijo
    def hablar(self):  # Sobrescritura de método
        print("Miau!")

animal = Animal("Animal genérico")
perro = Perro("Buddy")
gato = Gato("Whiskers")

animal.hablar()  # Imprime: Sonidos de animal
perro.hablar()  # Imprime: Guau!
gato.hablar()  # Imprime: Miau!

#HERENCIA MULTIPLE:

class Mamifero:
    def caminar(self):
        print("Este mamífero camina.")

class Ave:
    def volar(self):
        print("Esta ave vuela.")

class Ornitorrinco(Mamifero, Ave):
    pass

ornitorrinco = Ornitorrinco()
ornitorrinco.caminar()
ornitorrinco.volar()
#POLIMORFISMO
class Perro:
    def hablar(self):
        print("Guau!")

class Gato:
    def hablar(self):
        print("Miau!")

def hacer_hablar(animal):
    animal.hablar()

perro = Perro()
gato = Gato()

hacer_hablar(perro)  # Imprime: Guau!
hacer_hablar(gato)  # Imprime: Miau!

#DUCK TYPE

class Pato:
    def volar(self):
        print("El pato vuela.")

class Avion:
    def volar(self):
        print("El avión vuela.")

def hacer_volar(objeto_volador):
    objeto_volador.volar()

pato = Pato()
avion = Avion()

hacer_volar(pato)  # Imprime: El pato vuela.
hacer_volar(avion)  # Imprime: El avión vuela.

##ENCAPSULAMIENTO

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def obtener_nombre(self): ##GETTER 
        return self.__nombre

    def establecer_nombre(self, nombre): ##SETTER
        self.__nombre = nombre

    def obtener_edad(self):##GETTER
        return self.__edad

    def establecer_edad(self, edad): ##SETTER
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa.")

persona = Persona("Juan", 30)

print(persona.obtener_nombre())  # Obtener nombre
persona.establecer_nombre("María")  # Establecer nombre

print(persona.obtener_edad())  # Obtener edad
persona.establecer_edad(-5)  # Establecer edad (inválida)

#ABSTRACCION

from abc import ABC, abstractmethod

class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def calcular_area(self):  # Método abstracto
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):  # Implementación del método abstracto
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):  # Implementación del método abstracto
        return 3.14 * self.radio * self.radio

#figura = Figura()  # Error: no se puede instanciar una clase abstracta
cuadrado = Cuadrado(5)
circulo = Circulo(3)

print(cuadrado.calcular_area())  # Imprime: 25
print(circulo.calcular_area())  # Imprime: 28.26

#INTERFACES

from typing import Protocol

class ObjetoVolador(Protocol):
    def volar(self):
        ...

class Pato:
    def volar(self):
        print("El pato vuela.")

class Avion:
    def volar(self):
        print("El avión vuela.")

def hacer_volar(objeto_volador: ObjetoVolador):
    objeto_volador.volar()

pato = Pato()
avion = Avion()

hacer_volar(pato)  # Imprime: El pato vuela.
hacer_volar(avion)  # Imprime: El avión vuela.

