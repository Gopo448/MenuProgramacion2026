from nodos import Nodo


class ColaEstatica:
    def __init__(self, capacidad=5):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.frente = 0
        self.final = 0
        self.tamano = 0

    # Agrega al final
    def enqueue(self, valor):
        if self.tamano == self.capacidad:
            print("Cola llena.")
            return
        self.datos[self.final] = valor
        self.final = (self.final + 1) % self.capacidad
        self.tamano += 1
        print("Elemento agregado.")

    # Elimina del frente
    def dequeue(self):
        if self.tamano == 0:
            print("Cola vacia.")
            return
        valor = self.datos[self.frente]
        print(f"Elemento a eliminar: {valor}")
        self.datos[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.tamano -= 1
        print(f"Eliminado: {valor}")

    # Muestra la cola
    def mostrar(self):
        resultado = []
        indice = self.frente
        for _ in range(self.tamano):
            resultado.append(self.datos[indice])
            indice = (indice + 1) % self.capacidad
        print(f"Cola: {resultado}")


class ColaDinamica:
    def __init__(self):
        self.frente = None
        self.final = None

    # Recorre los nodos
    def recorrer(self):
        actual = self.frente
        while actual:
            yield actual
            actual = actual.siguiente

    # Agrega al final
    def enqueue(self, valor):
        nuevo = Nodo(valor)
        if self.final is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        print("Elemento agregado.")

    # Elimina del frente
    def dequeue(self):
        if self.frente is None:
            print("Cola vacia.")
            return
        print(f"Elemento a eliminar: {self.frente.valor}")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f"Eliminado: {valor}")

    # Muestra la cola
    def mostrar(self):
        datos = []
        for actual in self.recorrer():
            datos.append(actual.valor)
        print(f"Cola: {datos}")
