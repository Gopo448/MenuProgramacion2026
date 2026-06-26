#include <stdio.h>
#include <stdlib.h>
#include "listas.h"

// Prepara la lista
void inicializar_lista_simple(ListaSimple *lista) {
    lista->cabeza = NULL;
}

// Inserta al final
void insertar_simple(ListaSimple *lista, int valor) {
    NodoSimple *nuevo = (NodoSimple *) malloc(sizeof(NodoSimple));
    nuevo->valor = valor;
    nuevo->siguiente = NULL;

    if (lista->cabeza == NULL) {
        lista->cabeza = nuevo;
    } else {
        NodoSimple *actual = lista->cabeza;
        while (actual->siguiente != NULL) {
            actual = actual->siguiente;
        }
        actual->siguiente = nuevo;
    }
    printf("Elemento insertado\n");
}

// Elimina un valor
void eliminar_simple(ListaSimple *lista, int valor) {
    NodoSimple *actual = lista->cabeza;
    NodoSimple *anterior = NULL;

    while (actual != NULL && actual->valor != valor) {
        anterior = actual;
        actual = actual->siguiente;
    }

    if (actual == NULL) {
        printf("Elemento no encontrado\n");
        return;
    }

    printf("Elemento a eliminar: %d\n", actual->valor);
    if (anterior == NULL) {
        lista->cabeza = actual->siguiente;
    } else {
        anterior->siguiente = actual->siguiente;
    }
    free(actual);
    printf("Elemento eliminado\n");
}

// Busca un valor
void buscar_simple(ListaSimple *lista, int valor) {
    NodoSimple *actual = lista->cabeza;
    int posicion = 0;
    while (actual != NULL) {
        if (actual->valor == valor) {
            printf("Encontrado en posicion %d\n", posicion);
            return;
        }
        actual = actual->siguiente;
        posicion++;
    }
    printf("No encontrado\n");
}

// Muestra la lista
void mostrar_simple(ListaSimple *lista) {
    NodoSimple *actual = lista->cabeza;
    printf("Lista: [");
    while (actual != NULL) {
        printf("%d", actual->valor);
        if (actual->siguiente != NULL) {
            printf(" ");
        }
        actual = actual->siguiente;
    }
    printf("]\n");
}

// Libera memoria
void liberar_lista_simple(ListaSimple *lista) {
    while (lista->cabeza != NULL) {
        NodoSimple *temporal = lista->cabeza;
        lista->cabeza = lista->cabeza->siguiente;
        free(temporal);
    }
}

// Prepara la lista
void inicializar_lista_doble(ListaDoble *lista) {
    lista->cabeza = NULL;
    lista->cola = NULL;
}

// Inserta al final
void insertar_doble(ListaDoble *lista, int valor) {
    NodoDoble *nuevo = (NodoDoble *) malloc(sizeof(NodoDoble));
    nuevo->valor = valor;
    nuevo->siguiente = NULL;
    nuevo->anterior = NULL;

    if (lista->cabeza == NULL) {
        lista->cabeza = nuevo;
        lista->cola = nuevo;
    } else {
        lista->cola->siguiente = nuevo;
        nuevo->anterior = lista->cola;
        lista->cola = nuevo;
    }
    printf("Elemento insertado\n");
}

// Elimina un valor
void eliminar_doble(ListaDoble *lista, int valor) {
    NodoDoble *actual = lista->cabeza;

    while (actual != NULL && actual->valor != valor) {
        actual = actual->siguiente;
    }

    if (actual == NULL) {
        printf("Elemento no encontrado\n");
        return;
    }

    printf("Elemento a eliminar: %d\n", actual->valor);
    if (actual->anterior != NULL) {
        actual->anterior->siguiente = actual->siguiente;
    } else {
        lista->cabeza = actual->siguiente;
    }

    if (actual->siguiente != NULL) {
        actual->siguiente->anterior = actual->anterior;
    } else {
        lista->cola = actual->anterior;
    }

    free(actual);
    printf("Elemento eliminado\n");
}

// Muestra hacia adelante
void mostrar_doble_adelante(ListaDoble *lista) {
    NodoDoble *actual = lista->cabeza;
    printf("Adelante: [");
    while (actual != NULL) {
        printf("%d", actual->valor);
        if (actual->siguiente != NULL) {
            printf(" ");
        }
        actual = actual->siguiente;
    }
    printf("]\n");
}

// Muestra hacia atras
void mostrar_doble_atras(ListaDoble *lista) {
    NodoDoble *actual = lista->cola;
    printf("Atras: [");
    while (actual != NULL) {
        printf("%d", actual->valor);
        if (actual->anterior != NULL) {
            printf(" ");
        }
        actual = actual->anterior;
    }
    printf("]\n");
}

// Libera memoria
void liberar_lista_doble(ListaDoble *lista) {
    while (lista->cabeza != NULL) {
        NodoDoble *temporal = lista->cabeza;
        lista->cabeza = lista->cabeza->siguiente;
        free(temporal);
    }
    lista->cola = NULL;
}
