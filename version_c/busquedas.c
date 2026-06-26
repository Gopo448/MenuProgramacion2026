#include "busquedas.h"

// Busca uno por uno
int busqueda_lineal(int datos[], int n, int objetivo) {
    int i;
    for (i = 0; i < n; i++) {
        if (datos[i] == objetivo) {
            return i;
        }
    }
    return -1;
}

// Busca partiendo la lista
int busqueda_binaria(int datos[], int n, int objetivo) {
    int inicio = 0;
    int fin = n - 1;

    while (inicio <= fin) {
        int medio = (inicio + fin) / 2;
        if (datos[medio] == objetivo) {
            return medio;
        }
        if (datos[medio] < objetivo) {
            inicio = medio + 1;
        } else {
            fin = medio - 1;
        }
    }
    return -1;
}
