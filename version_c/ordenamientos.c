#include <stdio.h>
#include "ordenamientos.h"

// Intercambia dos valores
static void intercambiar(int *a, int *b) {
    int temporal = *a;
    *a = *b;
    *b = temporal;
}

// Ordena comparando vecinos
void bubble_sort(int datos[], int n) {
    int i;
    int j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (datos[j] > datos[j + 1]) {
                intercambiar(&datos[j], &datos[j + 1]);
            }
        }
    }
}

// Busca el menor en cada vuelta
void selection_sort(int datos[], int n) {
    int i;
    int j;
    int minimo;
    for (i = 0; i < n; i++) {
        minimo = i;
        for (j = i + 1; j < n; j++) {
            if (datos[j] < datos[minimo]) {
                minimo = j;
            }
        }
        intercambiar(&datos[i], &datos[minimo]);
    }
}

// Separa usando un pivote
static int particion(int datos[], int bajo, int alto) {
    int pivote = datos[alto];
    int i = bajo - 1;
    int j;
    for (j = bajo; j < alto; j++) {
        if (datos[j] <= pivote) {
            i++;
            intercambiar(&datos[i], &datos[j]);
        }
    }
    intercambiar(&datos[i + 1], &datos[alto]);
    return i + 1;
}

// Ordena usando un pivote
void quick_sort(int datos[], int bajo, int alto) {
    if (bajo < alto) {
        int pivote = particion(datos, bajo, alto);
        quick_sort(datos, bajo, pivote - 1);
        quick_sort(datos, pivote + 1, alto);
    }
}

// Ordena en dos direcciones
void cocktail_sort(int datos[], int n) {
    int inicio = 0;
    int fin = n - 1;
    int intercambio = 1;
    int i;

    while (intercambio) {
        intercambio = 0;
        for (i = inicio; i < fin; i++) {
            if (datos[i] > datos[i + 1]) {
                intercambiar(&datos[i], &datos[i + 1]);
                intercambio = 1;
            }
        }
        if (!intercambio) {
            break;
        }
        intercambio = 0;
        fin--;
        for (i = fin - 1; i >= inicio; i--) {
            if (datos[i] > datos[i + 1]) {
                intercambiar(&datos[i], &datos[i + 1]);
                intercambio = 1;
            }
        }
        inicio++;
    }
}

// Une partes ordenadas
static void mezclar(int datos[], int izquierda, int medio, int derecha) {
    int i;
    int j;
    int k;
    int n1 = medio - izquierda + 1;
    int n2 = derecha - medio;
    int izquierda_temp[100];
    int derecha_temp[100];

    for (i = 0; i < n1; i++) {
        izquierda_temp[i] = datos[izquierda + i];
    }
    for (j = 0; j < n2; j++) {
        derecha_temp[j] = datos[medio + 1 + j];
    }

    i = 0;
    j = 0;
    k = izquierda;

    while (i < n1 && j < n2) {
        if (izquierda_temp[i] <= derecha_temp[j]) {
            datos[k] = izquierda_temp[i];
            i++;
        } else {
            datos[k] = derecha_temp[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        datos[k] = izquierda_temp[i];
        i++;
        k++;
    }

    while (j < n2) {
        datos[k] = derecha_temp[j];
        j++;
        k++;
    }
}

// Divide y une ordenado
void merge_sort(int datos[], int izquierda, int derecha) {
    if (izquierda < derecha) {
        int medio = izquierda + (derecha - izquierda) / 2;
        merge_sort(datos, izquierda, medio);
        merge_sort(datos, medio + 1, derecha);
        mezclar(datos, izquierda, medio, derecha);
    }
}

// Ordena con pasos pequenos
void gnome_sort(int datos[], int n) {
    int indice = 0;
    while (indice < n) {
        if (indice == 0 || datos[indice] >= datos[indice - 1]) {
            indice++;
        } else {
            intercambiar(&datos[indice], &datos[indice - 1]);
            indice--;
        }
    }
}

// Ordena usando saltos
void shell_sort(int datos[], int n) {
    int salto;
    int i;
    int j;
    int temporal;

    for (salto = n / 2; salto > 0; salto /= 2) {
        for (i = salto; i < n; i++) {
            temporal = datos[i];
            j = i;
            while (j >= salto && datos[j - salto] > temporal) {
                datos[j] = datos[j - salto];
                j -= salto;
            }
            datos[j] = temporal;
        }
    }
}

// Muestra el arreglo
void mostrar_arreglo(int datos[], int n) {
    int i;
    printf("[");
    for (i = 0; i < n; i++) {
        printf("%d", datos[i]);
        if (i < n - 1) {
            printf(" ");
        }
    }
    printf("]\n");
}
