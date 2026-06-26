from collections import deque

from nodos import NodoArbol


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # Inserta por niveles
    def insertar(self, valor):
        nuevo = NodoArbol(valor)
        if self.raiz is None:
            self.raiz = nuevo
            print("Nodo insertado.")
            return
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            if actual.izquierda is None:
                actual.izquierda = nuevo
                print("Nodo insertado.")
                return
            cola.append(actual.izquierda)
            if actual.derecha is None:
                actual.derecha = nuevo
                print("Nodo insertado.")
                return
            cola.append(actual.derecha)

    # Busca por niveles
    def buscar(self, valor):
        if self.raiz is None:
            print("Arbol vacio.")
            return
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            if actual.valor == valor:
                print("Encontrado.")
                return
            if actual.izquierda:
                cola.append(actual.izquierda)
            if actual.derecha:
                cola.append(actual.derecha)
        print("No encontrado.")

    # Recorre izquierda raiz derecha
    def inorder(self):
        resultado = []

        def recorrer(nodo):
            if nodo:
                recorrer(nodo.izquierda)
                resultado.append(nodo.valor)
                recorrer(nodo.derecha)

        recorrer(self.raiz)
        print(f"Inorder: {resultado}")

    # Recorre raiz izquierda derecha
    def preorder(self):
        resultado = []

        def recorrer(nodo):
            if nodo:
                resultado.append(nodo.valor)
                recorrer(nodo.izquierda)
                recorrer(nodo.derecha)

        recorrer(self.raiz)
        print(f"Preorder: {resultado}")

    # Recorre izquierda derecha raiz
    def postorder(self):
        resultado = []

        def recorrer(nodo):
            if nodo:
                recorrer(nodo.izquierda)
                recorrer(nodo.derecha)
                resultado.append(nodo.valor)

        recorrer(self.raiz)
        print(f"Postorder: {resultado}")


class ArbolBST:
    def __init__(self):
        self.raiz = None

    # Inserta respetando el orden
    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)
        print("Nodo insertado.")

    # Inserta de forma recursiva
    def _insertar(self, nodo, valor):
        if nodo is None:
            return NodoArbol(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        return nodo

    # Busca usando el orden del BST
    def buscar(self, valor):
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                print("Encontrado.")
                return
            if valor < actual.valor:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        print("No encontrado.")

    # Recorre izquierda raiz derecha
    def inorder(self):
        resultado = []

        def recorrer(nodo):
            if nodo:
                recorrer(nodo.izquierda)
                resultado.append(nodo.valor)
                recorrer(nodo.derecha)

        recorrer(self.raiz)
        print(f"Inorder: {resultado}")

    # Recorre raiz izquierda derecha
    def preorder(self):
        resultado = []

        def recorrer(nodo):
            if nodo:
                resultado.append(nodo.valor)
                recorrer(nodo.izquierda)
                recorrer(nodo.derecha)

        recorrer(self.raiz)
        print(f"Preorder: {resultado}")

    # Recorre izquierda derecha raiz
    def postorder(self):
        resultado = []

        def recorrer(nodo):
            if nodo:
                recorrer(nodo.izquierda)
                recorrer(nodo.derecha)
                resultado.append(nodo.valor)

        recorrer(self.raiz)
        print(f"Postorder: {resultado}")
