#ifndef UTILS_H
#define UTILS_H

#define SALIR 99
#define MAX_DATOS 100

void limpiar_buffer(void);
void pausa(void);
void encabezado(const char *titulo);
int pedir_entero(const char *mensaje);
void pedir_lista(int datos[], int *n);
int mostrar_menu(const char *titulo, const char *opciones[], int total, int volver);

#endif
