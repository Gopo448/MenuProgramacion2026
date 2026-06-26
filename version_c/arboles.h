#ifndef ARBOLES_H
#define ARBOLES_H

typedef struct NodoArbol {
    int valor;
    struct NodoArbol *izquierda;
    struct NodoArbol *derecha;
} NodoArbol;

typedef struct {
    NodoArbol *raiz;
} ArbolBinario;

typedef struct {
    NodoArbol *raiz;
} ArbolBST;

void inicializar_arbol_binario(ArbolBinario *arbol);
void insertar_arbol_binario(ArbolBinario *arbol, int valor);
void buscar_arbol_binario(ArbolBinario *arbol, int valor);
void inorder_arbol(NodoArbol *raiz);
void preorder_arbol(NodoArbol *raiz);
void postorder_arbol(NodoArbol *raiz);
void liberar_arbol(NodoArbol *raiz);

void inicializar_bst(ArbolBST *arbol);
void insertar_bst(ArbolBST *arbol, int valor);
void buscar_bst(ArbolBST *arbol, int valor);

#endif
