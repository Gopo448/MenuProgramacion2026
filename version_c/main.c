#include <stdio.h>
#include "arboles.h"
#include "busquedas.h"
#include "colas.h"
#include "listas.h"
#include "ordenamientos.h"
#include "pilas.h"
#include "prim.h"
#include "utils.h"

// Menu para pila estatica
int menu_pila_estatica(PilaEstatica *pila) {
    const char *opciones[] = {"Push", "Pop", "Peek", "Mostrar"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("PILA ESTATICA", opciones, 4, 1);
        if (opcion == 1) {
            push_estatica(pila, pedir_entero("Valor: "));
            pausa();
        } else if (opcion == 2) {
            pop_estatica(pila);
            pausa();
        } else if (opcion == 3) {
            peek_estatica(pila);
            pausa();
        } else if (opcion == 4) {
            mostrar_pila_estatica(pila);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para pila dinamica
int menu_pila_dinamica(PilaDinamica *pila) {
    const char *opciones[] = {"Push", "Pop", "Peek", "Mostrar"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("PILA DINAMICA", opciones, 4, 1);
        if (opcion == 1) {
            push_dinamica(pila, pedir_entero("Valor: "));
            pausa();
        } else if (opcion == 2) {
            pop_dinamica(pila);
            pausa();
        } else if (opcion == 3) {
            peek_dinamica(pila);
            pausa();
        } else if (opcion == 4) {
            mostrar_pila_dinamica(pila);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para cola estatica
int menu_cola_estatica(ColaEstatica *cola) {
    const char *opciones[] = {"Enqueue", "Dequeue", "Mostrar"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("COLA ESTATICA", opciones, 3, 1);
        if (opcion == 1) {
            enqueue_estatica(cola, pedir_entero("Valor: "));
            pausa();
        } else if (opcion == 2) {
            dequeue_estatica(cola);
            pausa();
        } else if (opcion == 3) {
            mostrar_cola_estatica(cola);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para cola dinamica
int menu_cola_dinamica(ColaDinamica *cola) {
    const char *opciones[] = {"Enqueue", "Dequeue", "Mostrar"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("COLA DINAMICA", opciones, 3, 1);
        if (opcion == 1) {
            enqueue_dinamica(cola, pedir_entero("Valor: "));
            pausa();
        } else if (opcion == 2) {
            dequeue_dinamica(cola);
            pausa();
        } else if (opcion == 3) {
            mostrar_cola_dinamica(cola);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para lista simple
int menu_lista_simple(ListaSimple *lista) {
    const char *opciones[] = {"Insertar", "Eliminar", "Buscar", "Mostrar"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("LISTA SIMPLE DINAMICA", opciones, 4, 1);
        if (opcion == 1) {
            insertar_simple(lista, pedir_entero("Valor: "));
            pausa();
        } else if (opcion == 2) {
            eliminar_simple(lista, pedir_entero("Valor a eliminar: "));
            pausa();
        } else if (opcion == 3) {
            buscar_simple(lista, pedir_entero("Valor a buscar: "));
            pausa();
        } else if (opcion == 4) {
            mostrar_simple(lista);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para lista doble
int menu_lista_doble(ListaDoble *lista) {
    const char *opciones[] = {"Insertar", "Eliminar", "Mostrar hacia adelante", "Mostrar hacia atras"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("LISTA DOBLE DINAMICA", opciones, 4, 1);
        if (opcion == 1) {
            insertar_doble(lista, pedir_entero("Valor: "));
            pausa();
        } else if (opcion == 2) {
            eliminar_doble(lista, pedir_entero("Valor a eliminar: "));
            pausa();
        } else if (opcion == 3) {
            mostrar_doble_adelante(lista);
            pausa();
        } else if (opcion == 4) {
            mostrar_doble_atras(lista);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para busquedas
int menu_busqueda(void) {
    const char *opciones[] = {"Busqueda lineal", "Busqueda binaria"};
    int opcion;
    int datos[MAX_DATOS];
    int n;
    int objetivo;
    int posicion;
    while (1) {
        opcion = mostrar_menu("BUSQUEDA", opciones, 2, 1);
        if (opcion == 1) {
            pedir_lista(datos, &n);
            objetivo = pedir_entero("Valor a buscar: ");
            posicion = busqueda_lineal(datos, n, objetivo);
            printf("Posicion: %d\n", posicion);
            pausa();
        } else if (opcion == 2) {
            pedir_lista(datos, &n);
            bubble_sort(datos, n);
            objetivo = pedir_entero("Valor a buscar: ");
            posicion = busqueda_binaria(datos, n, objetivo);
            printf("Lista ordenada: ");
            mostrar_arreglo(datos, n);
            printf("Posicion: %d\n", posicion);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para insercion
int menu_insercion(void) {
    const char *opciones[] = {"Bubble Sort", "Selection Sort", "Quick Sort"};
    int opcion;
    int datos[MAX_DATOS];
    int n;
    while (1) {
        opcion = mostrar_menu("INSERCION", opciones, 3, 1);
        if (opcion >= 1 && opcion <= 3) {
            pedir_lista(datos, &n);
            if (opcion == 1) {
                bubble_sort(datos, n);
            } else if (opcion == 2) {
                selection_sort(datos, n);
            } else {
                quick_sort(datos, 0, n - 1);
            }
            printf("Ordenado: ");
            mostrar_arreglo(datos, n);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para seleccion
int menu_seleccion(void) {
    const char *opciones[] = {"Minimo", "Maximo", "Elemento K"};
    int opcion;
    int datos[MAX_DATOS];
    int n;
    int i;
    int k;
    while (1) {
        opcion = mostrar_menu("SELECCION", opciones, 3, 1);
        if (opcion == 1) {
            pedir_lista(datos, &n);
            int minimo = datos[0];
            for (i = 1; i < n; i++) {
                if (datos[i] < minimo) {
                    minimo = datos[i];
                }
            }
            printf("Minimo: %d\n", minimo);
            pausa();
        } else if (opcion == 2) {
            pedir_lista(datos, &n);
            int maximo = datos[0];
            for (i = 1; i < n; i++) {
                if (datos[i] > maximo) {
                    maximo = datos[i];
                }
            }
            printf("Maximo: %d\n", maximo);
            pausa();
        } else if (opcion == 3) {
            pedir_lista(datos, &n);
            k = pedir_entero("K (1 es el menor): ");
            bubble_sort(datos, n);
            printf("Ordenados: ");
            mostrar_arreglo(datos, n);
            printf("Elemento K: %d\n", datos[k - 1]);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para ordenar
int menu_sort(const char *titulo, int tipo) {
    const char *opciones[] = {"Ordenar lista"};
    int opcion;
    int datos[MAX_DATOS];
    int n;
    while (1) {
        opcion = mostrar_menu(titulo, opciones, 1, 1);
        if (opcion == 1) {
            pedir_lista(datos, &n);
            if (tipo == 1) {
                cocktail_sort(datos, n);
            } else if (tipo == 2) {
                quick_sort(datos, 0, n - 1);
            } else if (tipo == 3) {
                merge_sort(datos, 0, n - 1);
            } else if (tipo == 4) {
                gnome_sort(datos, n);
            } else if (tipo == 5) {
                shell_sort(datos, n);
            }
            printf("Ordenado: ");
            mostrar_arreglo(datos, n);
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para Prim
int menu_prim(void) {
    const char *opciones[] = {"Mostrar grafo de ejemplo", "Ejecutar Prim desde A"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("PRIM", opciones, 2, 1);
        if (opcion == 1) {
            mostrar_grafo_prim();
            pausa();
        } else if (opcion == 2) {
            ejecutar_prim();
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para arbol binario
int menu_arbol_binario(ArbolBinario *arbol) {
    const char *opciones[] = {"Insertar", "Inorder", "Preorder", "Postorder", "Buscar"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("ARBOL BINARIO", opciones, 5, 1);
        if (opcion == 1) {
            insertar_arbol_binario(arbol, pedir_entero("Valor: "));
            pausa();
        } else if (opcion == 2) {
            printf("Inorder: ");
            inorder_arbol(arbol->raiz);
            printf("\n");
            pausa();
        } else if (opcion == 3) {
            printf("Preorder: ");
            preorder_arbol(arbol->raiz);
            printf("\n");
            pausa();
        } else if (opcion == 4) {
            printf("Postorder: ");
            postorder_arbol(arbol->raiz);
            printf("\n");
            pausa();
        } else if (opcion == 5) {
            buscar_arbol_binario(arbol, pedir_entero("Valor a buscar: "));
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu para BST
int menu_bst(ArbolBST *arbol) {
    const char *opciones[] = {"Insertar", "Inorder", "Preorder", "Postorder", "Buscar"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("ARBOL BINARIO DE BUSQUEDA", opciones, 5, 1);
        if (opcion == 1) {
            insertar_bst(arbol, pedir_entero("Valor: "));
            pausa();
        } else if (opcion == 2) {
            printf("Inorder: ");
            inorder_arbol(arbol->raiz);
            printf("\n");
            pausa();
        } else if (opcion == 3) {
            printf("Preorder: ");
            preorder_arbol(arbol->raiz);
            printf("\n");
            pausa();
        } else if (opcion == 4) {
            printf("Postorder: ");
            postorder_arbol(arbol->raiz);
            printf("\n");
            pausa();
        } else if (opcion == 5) {
            buscar_bst(arbol, pedir_entero("Valor a buscar: "));
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Menu sobre el programa
int menu_acerca(void) {
    const char *opciones[] = {"Ver descripcion", "Ver flujo"};
    int opcion;
    while (1) {
        opcion = mostrar_menu("MENU DEL PROGRAMA", opciones, 2, 1);
        if (opcion == 1) {
            printf("Programa de terminal para demostrar estructuras de datos\n");
            printf("Los datos se mantienen solo durante la sesion\n");
            pausa();
        } else if (opcion == 2) {
            printf("Menu principal -> Estructura -> Operaciones -> Volver o Salir\n");
            pausa();
        } else if (opcion == 0) {
            return 0;
        } else if (opcion == SALIR) {
            return SALIR;
        } else {
            printf("Opcion no valida\n");
        }
    }
}

// Inicia el programa
int main(void) {
    PilaEstatica pila_estatica;
    PilaDinamica pila_dinamica;
    ColaEstatica cola_estatica;
    ColaDinamica cola_dinamica;
    ListaSimple lista_simple;
    ListaDoble lista_doble;
    ArbolBinario arbol_binario;
    ArbolBST arbol_bst;
    int opcion;
    int resultado;

    const char *opciones[] = {
        "Pila Estatica",
        "Pila Dinamica",
        "Cola Estatica",
        "Cola Dinamica",
        "Lista Simple Dinamica",
        "Lista Doble Dinamica",
        "Busqueda",
        "Insercion",
        "Seleccion",
        "Shaker",
        "Quick Sort",
        "Merge Sort",
        "Gnome Sort",
        "Prim",
        "Shell Sort",
        "Arbol Binario",
        "Arbol Binario de Busqueda",
        "Menu"
    };

    inicializar_pila_estatica(&pila_estatica);
    inicializar_pila_dinamica(&pila_dinamica);
    inicializar_cola_estatica(&cola_estatica);
    inicializar_cola_dinamica(&cola_dinamica);
    inicializar_lista_simple(&lista_simple);
    inicializar_lista_doble(&lista_doble);
    inicializar_arbol_binario(&arbol_binario);
    inicializar_bst(&arbol_bst);

    while (1) {
        resultado = 0;
        opcion = mostrar_menu("MENU PRINCIPAL", opciones, 18, 0);

        if (opcion == 1) {
            resultado = menu_pila_estatica(&pila_estatica);
        } else if (opcion == 2) {
            resultado = menu_pila_dinamica(&pila_dinamica);
        } else if (opcion == 3) {
            resultado = menu_cola_estatica(&cola_estatica);
        } else if (opcion == 4) {
            resultado = menu_cola_dinamica(&cola_dinamica);
        } else if (opcion == 5) {
            resultado = menu_lista_simple(&lista_simple);
        } else if (opcion == 6) {
            resultado = menu_lista_doble(&lista_doble);
        } else if (opcion == 7) {
            resultado = menu_busqueda();
        } else if (opcion == 8) {
            resultado = menu_insercion();
        } else if (opcion == 9) {
            resultado = menu_seleccion();
        } else if (opcion == 10) {
            resultado = menu_sort("SHAKER", 1);
        } else if (opcion == 11) {
            resultado = menu_sort("QUICK SORT", 2);
        } else if (opcion == 12) {
            resultado = menu_sort("MERGE SORT", 3);
        } else if (opcion == 13) {
            resultado = menu_sort("GNOME SORT", 4);
        } else if (opcion == 14) {
            resultado = menu_prim();
        } else if (opcion == 15) {
            resultado = menu_sort("SHELL SORT", 5);
        } else if (opcion == 16) {
            resultado = menu_arbol_binario(&arbol_binario);
        } else if (opcion == 17) {
            resultado = menu_bst(&arbol_bst);
        } else if (opcion == 18) {
            resultado = menu_acerca();
        } else if (opcion == 0) {
            printf("Programa finalizado\n");
            break;
        } else {
            printf("Opcion no valida\n");
        }

        if (resultado == SALIR) {
            printf("Programa finalizado\n");
            break;
        }
    }

    liberar_pila_dinamica(&pila_dinamica);
    liberar_cola_dinamica(&cola_dinamica);
    liberar_lista_simple(&lista_simple);
    liberar_lista_doble(&lista_doble);
    liberar_arbol(arbol_binario.raiz);
    liberar_arbol(arbol_bst.raiz);

    return 0;
}
