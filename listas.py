from nodos import Nodo


class ListaSimple:
    def __init__(self):
        self.cabeza = None

    # Recorre los nodos
    def recorrer(self):
        actual = self.cabeza
        while actual:
            yield actual
            actual = actual.siguiente

    # Inserta al final
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print("Elemento insertado.")

    # Elimina el primer valor encontrado
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            print("Elemento no encontrado.")
            return
        print(f"Elemento a eliminar: {actual.valor}")
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        print("Elemento eliminado.")

    # Busca usando un for
    def buscar(self, valor):
        for posicion, actual in enumerate(self.recorrer()):
            if actual.valor == valor:
                print(f"Encontrado en posicion {posicion}.")
                return
        print("No encontrado.")

    # Muestra usando un for
    def mostrar(self):
        datos = []
        for actual in self.recorrer():
            datos.append(actual.valor)
        print(f"Lista: {datos}")


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # Recorre hacia adelante
    def recorrer_adelante(self):
        actual = self.cabeza
        while actual:
            yield actual
            actual = actual.siguiente

    # Recorre hacia atras
    def recorrer_atras(self):
        actual = self.cola
        while actual:
            yield actual
            actual = actual.anterior

    # Inserta al final
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        print("Elemento insertado.")

    # Elimina el primer valor encontrado
    def eliminar(self, valor):
        actual = None
        for nodo in self.recorrer_adelante():
            if nodo.valor == valor:
                actual = nodo
                break
        if actual is None:
            print("Elemento no encontrado.")
            return
        print(f"Elemento a eliminar: {actual.valor}")
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        else:
            self.cabeza = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        else:
            self.cola = actual.anterior
        print("Elemento eliminado.")

    # Muestra hacia adelante con for
    def mostrar_adelante(self):
        datos = []
        for actual in self.recorrer_adelante():
            datos.append(actual.valor)
        print(f"Adelante: {datos}")

    # Muestra hacia atras con for
    def mostrar_atras(self):
        datos = []
        for actual in self.recorrer_atras():
            datos.append(actual.valor)
        print(f"Atras: {datos}")
