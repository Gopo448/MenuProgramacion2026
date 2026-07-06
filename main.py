from arboles import ArbolBST, ArbolBinario
from colas import ColaDinamica, ColaEstatica
from listas import ListaDoble, ListaSimple
from pilas import PilaDinamica, PilaEstatica
from ordenamientos import cocktail_sort, gnome_sort, merge_sort, quick_sort, shell_sort
from utils import SALIR, mostrar_menu
from menus import (
    menu_pila,
    menu_cola,
    menu_lista_simple,
    menu_lista_doble,
    menu_busqueda,
    menu_insercion,
    menu_seleccion,
    menu_sort,
    menu_prim,
    menu_arbol,
    menu_validaciones,
)


def main():
    # se crean las estructuras al inicio del programa
    pila_estatica = PilaEstatica()
    pila_dinamica = PilaDinamica()
    cola_estatica = ColaEstatica()
    cola_dinamica = ColaDinamica()
    lista_simple = ListaSimple()
    lista_doble = ListaDoble()
    arbol_binario = ArbolBinario()
    arbol_bst = ArbolBST()

    while True:
        opcion = mostrar_menu("MENU PRINCIPAL", [
            ("1",  "Pila Estatica"),
            ("2",  "Pila Dinamica"),
            ("3",  "Cola Estatica"),
            ("4",  "Cola Dinamica"),
            ("5",  "Lista Simple"),
            ("6",  "Lista Doble"),
            ("7",  "Busqueda"),
            ("8",  "Insercion"),
            ("9",  "Seleccion"),
            ("10", "Shaker Sort"),
            ("11", "Quick Sort"),
            ("12", "Merge Sort"),
            ("13", "Gnome Sort"),
            ("14", "Shell Sort"),
            ("15", "Grafos"),
            ("16", "Arbol Binario"),
            ("17", "Arbol BST"),
            ("18", "Validaciones"),
        ], volver=False)

        # se llama al menu correspondiente segun la opcion
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
            resultado = menu_sort("SHAKER SORT", cocktail_sort)
        elif opcion == "11":
            resultado = menu_sort("QUICK SORT", quick_sort)
        elif opcion == "12":
            resultado = menu_sort("MERGE SORT", merge_sort)
        elif opcion == "13":
            resultado = menu_sort("GNOME SORT", gnome_sort)
        elif opcion == "14":
            resultado = menu_sort("SHELL SORT", shell_sort)
        elif opcion == "15":
            resultado = menu_prim()
        elif opcion == "16":
            resultado = menu_arbol(arbol_binario, "ARBOL BINARIO")
        elif opcion == "17":
            resultado = menu_arbol(arbol_bst, "ARBOL BST")
        elif opcion == "18":
            resultado = menu_validaciones()
        elif opcion == "0":
            print("Programa finalizado.")
            break

        # si el usuario eligio salir desde un submenu se cierra el programa
        if resultado == SALIR:
            print("Programa finalizado.")
            break


if __name__ == "__main__":
    main()
