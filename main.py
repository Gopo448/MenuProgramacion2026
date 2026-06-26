from arboles import ArbolBST, ArbolBinario
from busquedas import busqueda_binaria, busqueda_lineal
from colas import ColaDinamica, ColaEstatica
from listas import ListaDoble, ListaSimple
from ordenamientos import (
    bubble_sort,
    cocktail_sort,
    gnome_sort,
    merge_sort,
    quick_sort,
    selection_sort,
    shell_sort,
)
from pilas import PilaDinamica, PilaEstatica
from prim import prim_mst
from utils import SALIR, mostrar_menu, pausa, pedir_entero, pedir_lista


# Menu para pilas
def menu_pila(pila, titulo):
    while True:
        # Muestra operaciones de pila
        opcion = mostrar_menu(titulo, [
            ("1", "Push"),
            ("2", "Pop"),
            ("3", "Peek"),
            ("4", "Mostrar"),
        ])
        if opcion == "1":
            pila.push(pedir_entero("Valor: "))
            pausa()
        elif opcion == "2":
            pila.pop()
            pausa()
        elif opcion == "3":
            pila.peek()
            pausa()
        elif opcion == "4":
            pila.mostrar()
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu para colas
def menu_cola(cola, titulo):
    while True:
        # Muestra operaciones de cola
        opcion = mostrar_menu(titulo, [
            ("1", "Enqueue"),
            ("2", "Dequeue"),
            ("3", "Mostrar"),
        ])
        if opcion == "1":
            cola.enqueue(pedir_entero("Valor: "))
            pausa()
        elif opcion == "2":
            cola.dequeue()
            pausa()
        elif opcion == "3":
            cola.mostrar()
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu para lista simple
def menu_lista_simple(lista):
    while True:
        # Muestra operaciones de lista simple
        opcion = mostrar_menu("LISTA SIMPLE DINAMICA", [
            ("1", "Insertar"),
            ("2", "Eliminar"),
            ("3", "Buscar"),
            ("4", "Mostrar"),
        ])
        if opcion == "1":
            lista.insertar(pedir_entero("Valor: "))
            pausa()
        elif opcion == "2":
            lista.eliminar(pedir_entero("Valor a eliminar: "))
            pausa()
        elif opcion == "3":
            lista.buscar(pedir_entero("Valor a buscar: "))
            pausa()
        elif opcion == "4":
            lista.mostrar()
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu para lista doble
def menu_lista_doble(lista):
    while True:
        # Muestra operaciones de lista doble
        opcion = mostrar_menu("LISTA DOBLE DINAMICA", [
            ("1", "Insertar"),
            ("2", "Eliminar"),
            ("3", "Mostrar hacia adelante"),
            ("4", "Mostrar hacia atras"),
        ])
        if opcion == "1":
            lista.insertar(pedir_entero("Valor: "))
            pausa()
        elif opcion == "2":
            lista.eliminar(pedir_entero("Valor a eliminar: "))
            pausa()
        elif opcion == "3":
            lista.mostrar_adelante()
            pausa()
        elif opcion == "4":
            lista.mostrar_atras()
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu para busquedas
def menu_busqueda():
    while True:
        # Muestra tipos de busqueda
        opcion = mostrar_menu("BUSQUEDA", [
            ("1", "Busqueda lineal"),
            ("2", "Busqueda binaria"),
        ])
        if opcion == "1":
            datos = pedir_lista()
            objetivo = pedir_entero("Valor a buscar: ")
            posicion = busqueda_lineal(datos, objetivo)
            print(f"Posicion: {posicion}")
            pausa()
        elif opcion == "2":
            datos = pedir_lista()
            objetivo = pedir_entero("Valor a buscar: ")
            posicion, ordenados = busqueda_binaria(datos, objetivo)
            print(f"Lista ordenada: {ordenados}")
            print(f"Posicion: {posicion}")
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu para ordenamientos basicos
def menu_insercion():
    while True:
        # Muestra ordenamientos basicos
        opcion = mostrar_menu("INSERCION", [
            ("1", "Bubble Sort"),
            ("2", "Selection Sort"),
            ("3", "Quick Sort"),
        ])
        if opcion in ("1", "2", "3"):
            datos = pedir_lista()
            if opcion == "1":
                print(f"Ordenado: {bubble_sort(datos)}")
            elif opcion == "2":
                print(f"Ordenado: {selection_sort(datos)}")
            else:
                print(f"Ordenado: {quick_sort(datos)}")
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu para seleccion
def menu_seleccion():
    while True:
        # Muestra opciones de seleccion
        opcion = mostrar_menu("SELECCION", [
            ("1", "Minimo"),
            ("2", "Maximo"),
            ("3", "Elemento K"),
        ])
        if opcion == "1":
            datos = pedir_lista()
            print(f"Minimo: {min(datos)}")
            pausa()
        elif opcion == "2":
            datos = pedir_lista()
            print(f"Maximo: {max(datos)}")
            pausa()
        elif opcion == "3":
            datos = pedir_lista()
            k = pedir_entero("K (1 es el menor): ")
            ordenados = sorted(datos)
            print(f"Ordenados: {ordenados}")
            print(f"Elemento K: {ordenados[k - 1]}")
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu para ordenar
def menu_sort(titulo, funcion):
    while True:
        # Pide una lista y la ordena
        opcion = mostrar_menu(titulo, [
            ("1", "Ordenar lista"),
        ])
        if opcion == "1":
            datos = pedir_lista()
            print(f"Ordenado: {funcion(datos)}")
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu para Prim
def menu_prim():
    # Grafo de ejemplo
    grafo = {
        "A": [("B", 2), ("C", 3)],
        "B": [("A", 2), ("C", 1), ("D", 4)],
        "C": [("A", 3), ("B", 1), ("D", 5), ("E", 6)],
        "D": [("B", 4), ("C", 5), ("E", 7)],
        "E": [("C", 6), ("D", 7)],
    }
    while True:
        # Muestra opciones de Prim
        opcion = mostrar_menu("PRIM", [
            ("1", "Mostrar grafo de ejemplo"),
            ("2", "Ejecutar Prim desde A"),
        ])
        if opcion == "1":
            for nodo, vecinos in grafo.items():
                print(f"{nodo}: {vecinos}")
            pausa()
        elif opcion == "2":
            aristas, total = prim_mst(grafo, "A")
            print(f"Aristas MST: {aristas}")
            print(f"Peso total: {total}")
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu para arboles
def menu_arbol(arbol, titulo):
    while True:
        # Muestra recorridos del arbol
        opcion = mostrar_menu(titulo, [
            ("1", "Insertar"),
            ("2", "Inorder"),
            ("3", "Preorder"),
            ("4", "Postorder"),
            ("5", "Buscar"),
        ])
        if opcion == "1":
            arbol.insertar(pedir_entero("Valor: "))
            pausa()
        elif opcion == "2":
            arbol.inorder()
            pausa()
        elif opcion == "3":
            arbol.preorder()
            pausa()
        elif opcion == "4":
            arbol.postorder()
            pausa()
        elif opcion == "5":
            arbol.buscar(pedir_entero("Valor a buscar: "))
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Menu sobre el programa
def menu_acerca():
    while True:
        # Muestra informacion del programa
        opcion = mostrar_menu("MENU DEL PROGRAMA", [
            ("1", "Ver descripcion"),
            ("2", "Ver flujo"),
        ])
        if opcion == "1":
            print("Programa de terminal para demostrar estructuras de datos.")
            print("Los datos se mantienen solo durante la sesion.")
            pausa()
        elif opcion == "2":
            print("Menu principal -> Estructura -> Operaciones -> Volver o Salir")
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
        else:
            print("Opcion no valida.")


# Inicia el programa
def main():
    # Crea las estructuras
    pila_estatica = PilaEstatica()
    pila_dinamica = PilaDinamica()
    cola_estatica = ColaEstatica()
    cola_dinamica = ColaDinamica()
    lista_simple = ListaSimple()
    lista_doble = ListaDoble()
    arbol_binario = ArbolBinario()
    arbol_bst = ArbolBST()

    while True:
        # Muestra el menu principal
        opcion = mostrar_menu("MENU PRINCIPAL", [
            ("1", "Pila Estatica"),
            ("2", "Pila Dinamica"),
            ("3", "Cola Estatica"),
            ("4", "Cola Dinamica"),
            ("5", "Lista Simple Dinamica"),
            ("6", "Lista Doble Dinamica"),
            ("7", "Busqueda"),
            ("8", "Insercion"),
            ("9", "Seleccion"),
            ("10", "Shaker"),
            ("11", "Quick Sort"),
            ("12", "Merge Sort"),
            ("13", "Gnome Sort"),
            ("14", "Prim"),
            ("15", "Shell Sort"),
            ("16", "Arbol Binario"),
            ("17", "Arbol Binario de Busqueda"),
            ("18", "Menu"),
        ], volver=False)

        # Ejecuta la opcion elegida
        resultado = None
        if opcion == "1":
            resultado = menu_pila(pila_estatica, "PILA ESTATICA")
        elif opcion == "2":
            resultado = menu_pila(pila_dinamica, "PILA DINAMICA")
        elif opcion == "3":
            resultado = menu_cola(cola_estatica, "COLA ESTATICA")
        elif opcion == "4":
            resultado = menu_cola(cola_dinamica, "COLA DINAMICA")
        elif opcion == "5":
            resultado = menu_lista_simple(lista_simple)
        elif opcion == "6":
            resultado = menu_lista_doble(lista_doble)
        elif opcion == "7":
            resultado = menu_busqueda()
        elif opcion == "8":
            resultado = menu_insercion()
        elif opcion == "9":
            resultado = menu_seleccion()
        elif opcion == "10":
            resultado = menu_sort("SHAKER", cocktail_sort)
        elif opcion == "11":
            resultado = menu_sort("QUICK SORT", quick_sort)
        elif opcion == "12":
            resultado = menu_sort("MERGE SORT", merge_sort)
        elif opcion == "13":
            resultado = menu_sort("GNOME SORT", gnome_sort)
        elif opcion == "14":
            resultado = menu_prim()
        elif opcion == "15":
            resultado = menu_sort("SHELL SORT", shell_sort)
        elif opcion == "16":
            resultado = menu_arbol(arbol_binario, "ARBOL BINARIO")
        elif opcion == "17":
            resultado = menu_arbol(arbol_bst, "ARBOL BINARIO DE BUSQUEDA")
        elif opcion == "18":
            resultado = menu_acerca()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida.")

        # Cierra desde cualquier menu
        if resultado == SALIR:
            print("Programa finalizado.")
            break


if __name__ == "__main__":
    main()
