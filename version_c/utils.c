#include <stdio.h>
#include "utils.h"

// Limpia la entrada
void limpiar_buffer(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {
    }
}

// Pausa la pantalla
void pausa(void) {
    printf("\nEnter para continuar...");
    getchar();
}

// Muestra un titulo simple
void encabezado(const char *titulo) {
    printf("\n===== %s =====\n", titulo);
}

// Pide un numero entero
int pedir_entero(const char *mensaje) {
    int valor;
    printf("%s", mensaje);
    scanf("%d", &valor);
    limpiar_buffer();
    return valor;
}

// Pide varios numeros
void pedir_lista(int datos[], int *n) {
    int i;
    printf("Cantidad de valores: ");
    scanf("%d", n);
    limpiar_buffer();

    if (*n > MAX_DATOS) {
        *n = MAX_DATOS;
    }

    for (i = 0; i < *n; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &datos[i]);
        limpiar_buffer();
    }
}

// Muestra opciones numeradas
int mostrar_menu(const char *titulo, const char *opciones[], int total, int volver) {
    int i;
    int opcion;
    encabezado(titulo);
    for (i = 0; i < total; i++) {
        printf("%d. %s\n", i + 1, opciones[i]);
    }
    if (volver) {
        printf("0. Volver\n");
        printf("99. Salir\n");
    } else {
        printf("0. Salir\n");
    }
    printf("\nSeleccione una opcion: ");
    scanf("%d", &opcion);
    limpiar_buffer();
    return opcion;
}
