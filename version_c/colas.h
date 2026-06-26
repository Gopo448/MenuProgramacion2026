#ifndef COLAS_H
#define COLAS_H

#define CAPACIDAD_COLA 5

typedef struct {
    int datos[CAPACIDAD_COLA];
    int frente;
    int final;
    int tamano;
} ColaEstatica;

typedef struct NodoCola {
    int valor;
    struct NodoCola *siguiente;
} NodoCola;

typedef struct {
    NodoCola *frente;
    NodoCola *final;
} ColaDinamica;

void inicializar_cola_estatica(ColaEstatica *cola);
void enqueue_estatica(ColaEstatica *cola, int valor);
void dequeue_estatica(ColaEstatica *cola);
void mostrar_cola_estatica(ColaEstatica *cola);

void inicializar_cola_dinamica(ColaDinamica *cola);
void enqueue_dinamica(ColaDinamica *cola, int valor);
void dequeue_dinamica(ColaDinamica *cola);
void mostrar_cola_dinamica(ColaDinamica *cola);
void liberar_cola_dinamica(ColaDinamica *cola);

#endif
