#include <stdio.h>
#include <stdlib.h>
#include "arboles.h"

// Crea un nodo
static NodoArbol *crear_nodo(int valor) {
    NodoArbol *nuevo = (NodoArbol *) malloc(sizeof(NodoArbol));
    nuevo->valor = valor;
    nuevo->izquierda = NULL;
    nuevo->derecha = NULL;
    return nuevo;
}

// Prepara el arbol
void inicializar_arbol_binario(ArbolBinario *arbol) {
    arbol->raiz = NULL;
}

// Inserta por niveles
void insertar_arbol_binario(ArbolBinario *arbol, int valor) {
    NodoArbol *nuevo = crear_nodo(valor);
    NodoArbol *cola[100];
    int frente = 0;
    int final = 0;

    if (arbol->raiz == NULL) {
        arbol->raiz = nuevo;
        printf("Nodo insertado\n");
        return;
    }

    cola[final++] = arbol->raiz;
    while (frente < final) {
        NodoArbol *actual = cola[frente++];
        if (actual->izquierda == NULL) {
            actual->izquierda = nuevo;
            printf("Nodo insertado\n");
            return;
        }
        cola[final++] = actual->izquierda;

        if (actual->derecha == NULL) {
            actual->derecha = nuevo;
            printf("Nodo insertado\n");
            return;
        }
        cola[final++] = actual->derecha;
    }
}

// Busca por niveles
void buscar_arbol_binario(ArbolBinario *arbol, int valor) {
    NodoArbol *cola[100];
    int frente = 0;
    int final = 0;

    if (arbol->raiz == NULL) {
        printf("Arbol vacio\n");
        return;
    }

    cola[final++] = arbol->raiz;
    while (frente < final) {
        NodoArbol *actual = cola[frente++];
        if (actual->valor == valor) {
            printf("Encontrado\n");
            return;
        }
        if (actual->izquierda != NULL) {
            cola[final++] = actual->izquierda;
        }
        if (actual->derecha != NULL) {
            cola[final++] = actual->derecha;
        }
    }
    printf("No encontrado\n");
}

// Recorre izquierda raiz derecha
void inorder_arbol(NodoArbol *raiz) {
    if (raiz != NULL) {
        inorder_arbol(raiz->izquierda);
        printf("%d ", raiz->valor);
        inorder_arbol(raiz->derecha);
    }
}

// Recorre raiz izquierda derecha
void preorder_arbol(NodoArbol *raiz) {
    if (raiz != NULL) {
        printf("%d ", raiz->valor);
        preorder_arbol(raiz->izquierda);
        preorder_arbol(raiz->derecha);
    }
}

// Recorre izquierda derecha raiz
void postorder_arbol(NodoArbol *raiz) {
    if (raiz != NULL) {
        postorder_arbol(raiz->izquierda);
        postorder_arbol(raiz->derecha);
        printf("%d ", raiz->valor);
    }
}

// Libera memoria
void liberar_arbol(NodoArbol *raiz) {
    if (raiz != NULL) {
        liberar_arbol(raiz->izquierda);
        liberar_arbol(raiz->derecha);
        free(raiz);
    }
}

// Prepara el arbol
void inicializar_bst(ArbolBST *arbol) {
    arbol->raiz = NULL;
}

// Inserta en BST
static NodoArbol *insertar_bst_rec(NodoArbol *raiz, int valor) {
    if (raiz == NULL) {
        return crear_nodo(valor);
    }
    if (valor < raiz->valor) {
        raiz->izquierda = insertar_bst_rec(raiz->izquierda, valor);
    } else if (valor > raiz->valor) {
        raiz->derecha = insertar_bst_rec(raiz->derecha, valor);
    }
    return raiz;
}

// Inserta en BST
void insertar_bst(ArbolBST *arbol, int valor) {
    arbol->raiz = insertar_bst_rec(arbol->raiz, valor);
    printf("Nodo insertado\n");
}

// Busca en BST
void buscar_bst(ArbolBST *arbol, int valor) {
    NodoArbol *actual = arbol->raiz;
    while (actual != NULL) {
        if (valor == actual->valor) {
            printf("Encontrado\n");
            return;
        }
        if (valor < actual->valor) {
            actual = actual->izquierda;
        } else {
            actual = actual->derecha;
        }
    }
    printf("No encontrado\n");
}
