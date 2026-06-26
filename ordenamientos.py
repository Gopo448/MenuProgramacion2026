# Ordena comparando vecinos
def bubble_sort(datos):
    datos = datos[:]
    for i in range(len(datos)):
        for j in range(0, len(datos) - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos


# Busca el menor en cada vuelta
def selection_sort(datos):
    datos = datos[:]
    for i in range(len(datos)):
        minimo = i
        for j in range(i + 1, len(datos)):
            if datos[j] < datos[minimo]:
                minimo = j
        datos[i], datos[minimo] = datos[minimo], datos[i]
    return datos


# Ordena usando un pivote
def quick_sort(datos):
    if len(datos) <= 1:
        return datos[:]
    pivote = datos[len(datos) // 2]
    menores = [x for x in datos if x < pivote]
    iguales = [x for x in datos if x == pivote]
    mayores = [x for x in datos if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


# Ordena en dos direcciones
def cocktail_sort(datos):
    datos = datos[:]
    inicio = 0
    fin = len(datos) - 1
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(inicio, fin):
            if datos[i] > datos[i + 1]:
                datos[i], datos[i + 1] = datos[i + 1], datos[i]
                intercambio = True
        if not intercambio:
            break
        intercambio = False
        fin -= 1
        for i in range(fin - 1, inicio - 1, -1):
            if datos[i] > datos[i + 1]:
                datos[i], datos[i + 1] = datos[i + 1], datos[i]
                intercambio = True
        inicio += 1
    return datos


# Divide y une ordenado
def merge_sort(datos):
    if len(datos) <= 1:
        return datos[:]
    medio = len(datos) // 2
    izquierda = merge_sort(datos[:medio])
    derecha = merge_sort(datos[medio:])
    resultado = []
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


# Ordena con pasos pequenos
def gnome_sort(datos):
    datos = datos[:]
    indice = 0
    while indice < len(datos):
        if indice == 0 or datos[indice] >= datos[indice - 1]:
            indice += 1
        else:
            datos[indice], datos[indice - 1] = datos[indice - 1], datos[indice]
            indice -= 1
    return datos


# Ordena usando saltos
def shell_sort(datos):
    datos = datos[:]
    salto = len(datos) // 2
    while salto > 0:
        for i in range(salto, len(datos)):
            temporal = datos[i]
            j = i
            while j >= salto and datos[j - salto] > temporal:
                datos[j] = datos[j - salto]
                j -= salto
            datos[j] = temporal
        salto //= 2
    return datos
