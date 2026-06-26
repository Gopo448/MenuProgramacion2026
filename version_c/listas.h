#ifndef LISTAS_H
#define LISTAS_H

typedef struct NodoSimple {
    int valor;
    struct NodoSimple *siguiente;
} NodoSimple;

typedef struct {
    NodoSimple *cabeza;
} ListaSimple;

typedef struct NodoDoble {
    int valor;
    struct NodoDoble *siguiente;
    struct NodoDoble *anterior;
} NodoDoble;

typedef struct {
    NodoDoble *cabeza;
    NodoDoble *cola;
} ListaDoble;

void inicializar_lista_simple(ListaSimple *lista);
void insertar_simple(ListaSimple *lista, int valor);
void eliminar_simple(ListaSimple *lista, int valor);
void buscar_simple(ListaSimple *lista, int valor);
void mostrar_simple(ListaSimple *lista);
void liberar_lista_simple(ListaSimple *lista);

void inicializar_lista_doble(ListaDoble *lista);
void insertar_doble(ListaDoble *lista, int valor);
void eliminar_doble(ListaDoble *lista, int valor);
void mostrar_doble_adelante(ListaDoble *lista);
void mostrar_doble_atras(ListaDoble *lista);
void liberar_lista_doble(ListaDoble *lista);

#endif
