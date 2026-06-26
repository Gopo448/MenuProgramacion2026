#include <stdio.h>
#include <stdlib.h>
#include "colas.h"

// Prepara la cola
void inicializar_cola_estatica(ColaEstatica *cola) {
    cola->frente = 0;
    cola->final = 0;
    cola->tamano = 0;
}

// Agrega al final
void enqueue_estatica(ColaEstatica *cola, int valor) {
    if (cola->tamano == CAPACIDAD_COLA) {
        printf("Cola llena\n");
        return;
    }
    cola->datos[cola->final] = valor;
    cola->final = (cola->final + 1) % CAPACIDAD_COLA;
    cola->tamano++;
    printf("Elemento agregado\n");
}

// Elimina del frente
void dequeue_estatica(ColaEstatica *cola) {
    int valor;
    if (cola->tamano == 0) {
        printf("Cola vacia\n");
        return;
    }
    valor = cola->datos[cola->frente];
    printf("Elemento a eliminar: %d\n", valor);
    printf("Eliminado: %d\n", valor);
    cola->frente = (cola->frente + 1) % CAPACIDAD_COLA;
    cola->tamano--;
}

// Muestra la cola
void mostrar_cola_estatica(ColaEstatica *cola) {
    int i;
    int indice = cola->frente;
    printf("Cola: [");
    for (i = 0; i < cola->tamano; i++) {
        printf("%d", cola->datos[indice]);
        if (i < cola->tamano - 1) {
            printf(" ");
        }
        indice = (indice + 1) % CAPACIDAD_COLA;
    }
    printf("]\n");
}

// Prepara la cola
void inicializar_cola_dinamica(ColaDinamica *cola) {
    cola->frente = NULL;
    cola->final = NULL;
}

// Agrega al final
void enqueue_dinamica(ColaDinamica *cola, int valor) {
    NodoCola *nuevo = (NodoCola *) malloc(sizeof(NodoCola));
    nuevo->valor = valor;
    nuevo->siguiente = NULL;
    if (cola->final == NULL) {
        cola->frente = nuevo;
        cola->final = nuevo;
    } else {
        cola->final->siguiente = nuevo;
        cola->final = nuevo;
    }
    printf("Elemento agregado\n");
}

// Elimina del frente
void dequeue_dinamica(ColaDinamica *cola) {
    NodoCola *temporal;
    if (cola->frente == NULL) {
        printf("Cola vacia\n");
        return;
    }
    temporal = cola->frente;
    printf("Elemento a eliminar: %d\n", temporal->valor);
    printf("Eliminado: %d\n", temporal->valor);
    cola->frente = temporal->siguiente;
    if (cola->frente == NULL) {
        cola->final = NULL;
    }
    free(temporal);
}

// Muestra la cola
void mostrar_cola_dinamica(ColaDinamica *cola) {
    NodoCola *actual = cola->frente;
    printf("Cola: [");
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
void liberar_cola_dinamica(ColaDinamica *cola) {
    while (cola->frente != NULL) {
        NodoCola *temporal = cola->frente;
        cola->frente = cola->frente->siguiente;
        free(temporal);
    }
    cola->final = NULL;
}
