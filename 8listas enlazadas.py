class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        ultimo_nodo = self.cabeza
        while ultimo_nodo.siguiente:
            ultimo_nodo = ultimo_nodo.siguiente
        ultimo_nodo.siguiente = nuevo_nodo

    def mostrar_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)
lista.mostrar_lista()  # Imprime: 1 -> 2 -> 3 -> None
print("Hola", end=" este es un espacio ", ' gg gg ')
print("Mundo")