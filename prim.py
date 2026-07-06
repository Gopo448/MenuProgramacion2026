# calcula rutas mas cortas entre todos los nodos usando floyd-warshall
def floyd_warshall(grafo):
    nodos = list(grafo.keys())
    n = len(nodos)
    idx = {nodo: i for i, nodo in enumerate(nodos)}

    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    siguiente = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for origen in grafo:
        for destino, peso in grafo[origen]:
            i, j = idx[origen], idx[destino]
            dist[i][j] = peso
            siguiente[i][j] = destino

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    siguiente[i][j] = siguiente[i][k]

    def ruta(origen, destino):
        i, j = idx[origen], idx[destino]
        if dist[i][j] == INF:
            return None, INF
        camino = [origen]
        while camino[-1] != destino:
            camino.append(siguiente[idx[camino[-1]]][j])
        return camino, dist[i][j]

    return ruta


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
