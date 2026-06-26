#ifndef PILAS_H
#define PILAS_H

#define CAPACIDAD_PILA 5

typedef struct {
    int datos[CAPACIDAD_PILA];
    int tope;
} PilaEstatica;

typedef struct NodoPila {
    int valor;
    struct NodoPila *siguiente;
} NodoPila;

typedef struct {
    NodoPila *tope;
} PilaDinamica;

void inicializar_pila_estatica(PilaEstatica *pila);
void push_estatica(PilaEstatica *pila, int valor);
void pop_estatica(PilaEstatica *pila);
void peek_estatica(PilaEstatica *pila);
void mostrar_pila_estatica(PilaEstatica *pila);

void inicializar_pila_dinamica(PilaDinamica *pila);
void push_dinamica(PilaDinamica *pila, int valor);
void pop_dinamica(PilaDinamica *pila);
void peek_dinamica(PilaDinamica *pila);
void mostrar_pila_dinamica(PilaDinamica *pila);
void liberar_pila_dinamica(PilaDinamica *pila);

#endif
