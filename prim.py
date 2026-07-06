# busca el arbol de expansion minima desde un nodo
def prim_mst(grafo, inicio):
    visitados = {inicio}
    aristas = []
    total = 0

    while len(visitados) < len(grafo):
        candidata = None
        for origen in visitados:
            for destino, peso in grafo[origen]:
                if destino not in visitados:
                    if candidata is None or peso < candidata[2]:
                        candidata = (origen, destino, peso)
        if candidata is None:
            break
        origen, destino, peso = candidata
        visitados.add(destino)
        aristas.append(candidata)
        total += peso

    return aristas, total


# busca la ruta mas corta entre dos nodos usando dijkstra
def dijkstra(grafo, inicio, destino):
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[inicio] = 0
    anteriores = {nodo: None for nodo in grafo}
    pendientes = list(grafo.keys())

    while pendientes:
        # toma el nodo con menor distancia
        actual = min(pendientes, key=lambda n: distancias[n])
        if distancias[actual] == float("inf"):
            break
        pendientes.remove(actual)

        for vecino, peso in grafo[actual]:
            nueva = distancias[actual] + peso
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                anteriores[vecino] = actual

    # reconstruye el camino
    camino = []
    nodo = destino
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = anteriores[nodo]

    if distancias[destino] == float("inf"):
        return None, float("inf")

    return camino, distancias[destino]
