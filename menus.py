from utils import SALIR, mostrar_menu, pausa, pedir_entero, pedir_lista
from busquedas import busqueda_binaria, busqueda_lineal
from ordenamientos import bubble_sort, cocktail_sort, gnome_sort, merge_sort, quick_sort, selection_sort, shell_sort, insertion_sort, comb_sort
from prim import prim_mst, dijkstra, floyd_warshall
from validaciones import validar_entero, validar_decimal, validar_hora, validar_correo, validar_pagina_web


# menu para manejar pilas
def menu_pila(pila, titulo):
    while True:
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


# menu para manejar colas
def menu_cola(cola, titulo):
    while True:
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


# menu para lista simple
def menu_lista_simple(lista):
    while True:
        opcion = mostrar_menu("LISTA SIMPLE", [
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


# menu para lista doble
def menu_lista_doble(lista):
    while True:
        opcion = mostrar_menu("LISTA DOBLE", [
            ("1", "Insertar"),
            ("2", "Eliminar"),
            ("3", "Mostrar adelante"),
            ("4", "Mostrar atras"),
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


# menu para busquedas
def menu_busqueda():
    while True:
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


# menu para ordenamientos por insercion
def menu_insercion():
    while True:
        opcion = mostrar_menu("INSERCION", [
            ("1", "Bubble Sort"),
            ("2", "Selection Sort"),
            ("3", "Quick Sort"),
            ("4", "Insertion Sort"),
            ("5", "Comb Sort"),
        ])
        if opcion in ("1", "2", "3", "4", "5"):
            datos = pedir_lista()
            if opcion == "1":
                print(f"Ordenado: {bubble_sort(datos)}")
            elif opcion == "2":
                print(f"Ordenado: {selection_sort(datos)}")
            elif opcion == "3":
                print(f"Ordenado: {quick_sort(datos)}")
            elif opcion == "4":
                print(f"Ordenado: {insertion_sort(datos)}")
            elif opcion == "5":
                print(f"Ordenado: {comb_sort(datos)}")
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR


# menu para encontrar minimo maximo o elemento k
def menu_seleccion():
    while True:
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


# menu generico para cualquier algoritmo de ordenamiento
def menu_sort(titulo, funcion):
    while True:
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


# muestra las ciudades y pide elegir por numero
def elegir_ciudad(ciudades, mensaje):
    for i, c in enumerate(ciudades, 1):
        print(f"  {i}. {c}")
    try:
        num = int(input(mensaje))
        if 1 <= num <= len(ciudades):
            return ciudades[num - 1]
    except ValueError:
        pass
    return None


# menu de grafos con ciudades del estado de mexico
def menu_prim():
    # distancias reales aproximadas en km por carretera
    grafo = {
        "Ixtlahuaca": [("Toluca", 37), ("CDMX", 72), ("Jiquipilco", 13)],
        "Jocotitlan": [("CDMX", 80)],
        "CDMX":       [("Ixtlahuaca", 72), ("Jocotitlan", 80), ("Jiquipilco", 76), ("Metepec", 65)],
        "Toluca":     [("Ixtlahuaca", 37)],
        "Jiquipilco": [("Ixtlahuaca", 13), ("CDMX", 76), ("Metepec", 46)],
        "Metepec":    [("CDMX", 65), ("Jiquipilco", 46)],
    }
    ciudades = list(grafo.keys())

    while True:
        opcion = mostrar_menu("GRAFOS - CIUDADES EDOMEX", [
            ("1", "Mostrar conexiones del grafo"),
            ("2", "Arbol de expansion minima"),
            ("3", "Ruta mas corta entre dos ciudades"),
        ])
        if opcion == "1":
            print()
            for nodo, vecinos in grafo.items():
                conexiones = ", ".join(f"{v}({p}km)" for v, p in vecinos)
                print(f"  {nodo} -> {conexiones}")
            pausa()

        elif opcion == "2":
            print("\nCiudades disponibles:")
            inicio = elegir_ciudad(ciudades, "Elige ciudad de inicio (numero): ")
            if inicio is None:
                print("Opcion no valida.")
            else:
                aristas, total = prim_mst(grafo, inicio)
                print(f"\nArbol de expansion minima desde {inicio}:")
                for origen, destino, peso in aristas:
                    print(f"  {origen} -> {destino}  ({peso} km)")
                print(f"Distancia total: {total} km")
            pausa()

        elif opcion == "3":
            print("\nCiudades disponibles:")
            inicio = elegir_ciudad(ciudades, "Elige ciudad de inicio (numero): ")
            print("\nCiudades disponibles:")
            fin = elegir_ciudad(ciudades, "Elige ciudad de destino (numero): ")
            if inicio is None or fin is None:
                print("Opcion no valida.")
            else:
                ruta = floyd_warshall(grafo)
                camino, distancia = ruta(inicio, fin)
                if camino is None:
                    print("No hay ruta disponible.")
                else:
                    print(f"\nRuta mas corta (Floyd-Warshall) de {inicio} a {fin}:")
                    print("  " + " -> ".join(camino))
                    print(f"Distancia total: {distancia} km")
            pausa()

        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR


# menu para arboles binarios
def menu_arbol(arbol, titulo):
    while True:
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


# menu para validar distintos tipos de datos
def menu_validaciones():
    while True:
        opcion = mostrar_menu("VALIDACIONES", [
            ("1", "Entero (1 al 3999)"),
            ("2", "Decimal"),
            ("3", "Hora (hh:mm)"),
            ("4", "Correo electronico"),
            ("5", "Pagina web"),
        ])
        if opcion == "1":
            valor = input("Ingresa un numero: ")
            ok, resultado = validar_entero(valor)
            print(resultado)
            pausa()
        elif opcion == "2":
            valor = input("Ingresa un decimal: ")
            ok, resultado = validar_decimal(valor)
            print(resultado)
            pausa()
        elif opcion == "3":
            valor = input("Ingresa una hora (hh:mm): ")
            ok, resultado = validar_hora(valor)
            print(resultado)
            pausa()
        elif opcion == "4":
            valor = input("Ingresa un correo: ")
            ok, resultado = validar_correo(valor)
            print(resultado)
            pausa()
        elif opcion == "5":
            valor = input("Ingresa una pagina web: ")
            ok, resultado = validar_pagina_web(valor)
            print(resultado)
            pausa()
        elif opcion == "0":
            return
        elif opcion == "99":
            return SALIR
