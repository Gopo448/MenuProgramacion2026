from nodos import Nodo


class PilaEstatica:
    def __init__(self, capacidad=5):
        self.capacidad = capacidad
        self.datos = []

    # Agrega al tope
    def push(self, valor):
        if len(self.datos) >= self.capacidad:
            print("Pila llena.")
            return
        self.datos.append(valor)
        print("Elemento agregado.")

    # Elimina del tope
    def pop(self):
        if not self.datos:
            print("Pila vacia.")
            return
        print(f"Elemento a eliminar: {self.datos[-1]}")
        print(f"Eliminado: {self.datos.pop()}")

    # Muestra el tope
    def peek(self):
        if not self.datos:
            print("Pila vacia.")
            return
        print(f"Tope: {self.datos[-1]}")

    # Muestra la pila
    def mostrar(self):
        print(f"Pila: {self.datos}")


class PilaDinamica:
    def __init__(self):
        self.tope = None

    # Recorre los nodos
    def recorrer(self):
        actual = self.tope
        while actual:
            yield actual
            actual = actual.siguiente

    # Agrega al tope
    def push(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        print("Elemento agregado.")

    # Elimina del tope
    def pop(self):
        if self.tope is None:
            print("Pila vacia.")
            return
        print(f"Elemento a eliminar: {self.tope.valor}")
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        print(f"Eliminado: {valor}")

    # Muestra el tope
    def peek(self):
        if self.tope is None:
            print("Pila vacia.")
            return
        print(f"Tope: {self.tope.valor}")

    # Muestra la pila
    def mostrar(self):
        datos = []
        for actual in self.recorrer():
            datos.append(actual.valor)
        print(f"Pila: {datos}")
