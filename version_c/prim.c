#include <stdio.h>
#include "prim.h"

#define NODOS_PRIM 5
#define INF 9999

static int grafo[NODOS_PRIM][NODOS_PRIM] = {
    {0, 2, 3, 0, 0},
    {2, 0, 1, 4, 0},
    {3, 1, 0, 5, 6},
    {0, 4, 5, 0, 7},
    {0, 0, 6, 7, 0}
};

static char nombres[NODOS_PRIM] = {'A', 'B', 'C', 'D', 'E'};

// Muestra el grafo
void mostrar_grafo_prim(void) {
    int i;
    int j;
    for (i = 0; i < NODOS_PRIM; i++) {
        printf("%c:", nombres[i]);
        for (j = 0; j < NODOS_PRIM; j++) {
            if (grafo[i][j] != 0) {
                printf(" %c(%d)", nombres[j], grafo[i][j]);
            }
        }
        printf("\n");
    }
}

// Busca el arbol de menor costo
void ejecutar_prim(void) {
    int visitado[NODOS_PRIM] = {0};
    int total = 0;
    int aristas = 0;

    visitado[0] = 1;

    while (aristas < NODOS_PRIM - 1) {
        int minimo = INF;
        int origen = -1;
        int destino = -1;
        int i;
        int j;

        for (i = 0; i < NODOS_PRIM; i++) {
            if (visitado[i]) {
                for (j = 0; j < NODOS_PRIM; j++) {
                    if (!visitado[j] && grafo[i][j] != 0 && grafo[i][j] < minimo) {
                        minimo = grafo[i][j];
                        origen = i;
                        destino = j;
                    }
                }
            }
        }

        if (destino == -1) {
            break;
        }

        printf("%c - %c peso %d\n", nombres[origen], nombres[destino], minimo);
        visitado[destino] = 1;
        total += minimo;
        aristas++;
    }

    printf("Peso total: %d\n", total);
}
