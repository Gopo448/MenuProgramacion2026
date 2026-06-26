# Busca el arbol de menor costo
def prim_mst(grafo, inicio):
    # Guarda los nodos visitados
    visitados = {inicio}
    aristas = []
    total = 0

    while len(visitados) < len(grafo):
        # Busca la arista menor
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
