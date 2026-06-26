#include <stdio.h>
#include <stdlib.h>
#include "pilas.h"

// Prepara la pila
void inicializar_pila_estatica(PilaEstatica *pila) {
    pila->tope = -1;
}

// Agrega al tope
void push_estatica(PilaEstatica *pila, int valor) {
    if (pila->tope == CAPACIDAD_PILA - 1) {
        printf("Pila llena\n");
        return;
    }
    pila->tope++;
    pila->datos[pila->tope] = valor;
    printf("Elemento agregado\n");
}

// Elimina del tope
void pop_estatica(PilaEstatica *pila) {
    if (pila->tope == -1) {
        printf("Pila vacia\n");
        return;
    }
    printf("Elemento a eliminar: %d\n", pila->datos[pila->tope]);
    printf("Eliminado: %d\n", pila->datos[pila->tope]);
    pila->tope--;
}

// Muestra el tope
void peek_estatica(PilaEstatica *pila) {
    if (pila->tope == -1) {
        printf("Pila vacia\n");
        return;
    }
    printf("Tope: %d\n", pila->datos[pila->tope]);
}

// Muestra la pila
void mostrar_pila_estatica(PilaEstatica *pila) {
    int i;
    printf("Pila: [");
    for (i = 0; i <= pila->tope; i++) {
        printf("%d", pila->datos[i]);
        if (i < pila->tope) {
            printf(" ");
        }
    }
    printf("]\n");
}

// Prepara la pila
void inicializar_pila_dinamica(PilaDinamica *pila) {
    pila->tope = NULL;
}

// Agrega al tope
void push_dinamica(PilaDinamica *pila, int valor) {
    NodoPila *nuevo = (NodoPila *) malloc(sizeof(NodoPila));
    nuevo->valor = valor;
    nuevo->siguiente = pila->tope;
    pila->tope = nuevo;
    printf("Elemento agregado\n");
}

// Elimina del tope
void pop_dinamica(PilaDinamica *pila) {
    NodoPila *temporal;
    if (pila->tope == NULL) {
        printf("Pila vacia\n");
        return;
    }
    temporal = pila->tope;
    printf("Elemento a eliminar: %d\n", temporal->valor);
    printf("Eliminado: %d\n", temporal->valor);
    pila->tope = temporal->siguiente;
    free(temporal);
}

// Muestra el tope
void peek_dinamica(PilaDinamica *pila) {
    if (pila->tope == NULL) {
        printf("Pila vacia\n");
        return;
    }
    printf("Tope: %d\n", pila->tope->valor);
}

// Muestra la pila
void mostrar_pila_dinamica(PilaDinamica *pila) {
    NodoPila *actual = pila->tope;
    printf("Pila: [");
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
void liberar_pila_dinamica(PilaDinamica *pila) {
    while (pila->tope != NULL) {
        NodoPila *temporal = pila->tope;
        pila->tope = pila->tope->siguiente;
        free(temporal);
    }
}
