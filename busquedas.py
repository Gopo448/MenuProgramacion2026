# Busca uno por uno
def busqueda_lineal(datos, objetivo):
    for indice, valor in enumerate(datos):
        if valor == objetivo:
            return indice
    return -1


# Busca partiendo la lista
def busqueda_binaria(datos, objetivo):
    # Ordena antes de buscar
    datos = sorted(datos)
    inicio = 0
    fin = len(datos) - 1
    while inicio <= fin:
        # Revisa el centro
        medio = (inicio + fin) // 2
        if datos[medio] == objetivo:
            return medio, datos
        if datos[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1, datos
