from flask import Flask, request, jsonify, send_from_directory
from pilas import PilaEstatica, PilaDinamica
from colas import ColaEstatica, ColaDinamica
from listas import ListaSimple, ListaDoble
from busquedas import busqueda_lineal, busqueda_binaria
from ordenamientos import bubble_sort, selection_sort, quick_sort, cocktail_sort, merge_sort, gnome_sort, shell_sort, insertion_sort, comb_sort
from arboles import ArbolBinario, ArbolBST
from prim import prim_mst, dijkstra, floyd_warshall
from validaciones import validar_entero, validar_decimal, validar_hora, validar_correo, validar_pagina_web

app = Flask(__name__)

# estructuras que persisten durante la sesion
pilas = {
    "estatica": PilaEstatica(),
    "dinamica": PilaDinamica(),
}
colas = {
    "estatica": ColaEstatica(),
    "dinamica": ColaDinamica(),
}
listas = {
    "simple": ListaSimple(),
    "doble":  ListaDoble(),
}
arboles = {
    "binario": ArbolBinario(),
    "bst":     ArbolBST(),
}

grafo = {
    "Ixtlahuaca": [("Toluca", 37), ("CDMX", 72), ("Jiquipilco", 13)],
    "Jocotitlan": [("CDMX", 80)],
    "CDMX":       [("Ixtlahuaca", 72), ("Jocotitlan", 80), ("Jiquipilco", 76), ("Metepec", 65)],
    "Toluca":     [("Ixtlahuaca", 37)],
    "Jiquipilco": [("Ixtlahuaca", 13), ("CDMX", 76), ("Metepec", 46)],
    "Metepec":    [("CDMX", 65), ("Jiquipilco", 46)],
}


# sirve el archivo html principal
@app.route("/")
def index():
    return send_from_directory(".", "menu_gui.html")


# --- pilas ---
@app.route("/pilas/<tipo>/<operacion>", methods=["POST"])
def op_pila(tipo, operacion):
    pila = pilas.get(tipo)
    if pila is None:
        return jsonify({"error": "tipo no valido"})
    data = request.json or {}
    try:
        if operacion == "push":
            pila.push(int(data["valor"]))
            return jsonify({"resultado": f"push {data['valor']} ok"})
        elif operacion == "pop":
            pila.pop()
            return jsonify({"resultado": "pop ok"})
        elif operacion == "peek":
            pila.peek()
            return jsonify({"resultado": "peek ok"})
        elif operacion == "mostrar":
            import io, sys
            buf = io.StringIO()
            sys.stdout = buf
            pila.mostrar()
            sys.stdout = sys.__stdout__
            return jsonify({"resultado": buf.getvalue().strip()})
    except Exception as e:
        return jsonify({"error": str(e)})


# --- colas ---
@app.route("/colas/<tipo>/<operacion>", methods=["POST"])
def op_cola(tipo, operacion):
    cola = colas.get(tipo)
    if cola is None:
        return jsonify({"error": "tipo no valido"})
    data = request.json or {}
    try:
        if operacion == "enqueue":
            cola.enqueue(int(data["valor"]))
            return jsonify({"resultado": f"enqueue {data['valor']} ok"})
        elif operacion == "dequeue":
            cola.dequeue()
            return jsonify({"resultado": "dequeue ok"})
        elif operacion == "mostrar":
            import io, sys
            buf = io.StringIO()
            sys.stdout = buf
            cola.mostrar()
            sys.stdout = sys.__stdout__
            return jsonify({"resultado": buf.getvalue().strip()})
    except Exception as e:
        return jsonify({"error": str(e)})


# --- listas ---
@app.route("/listas/<tipo>/<operacion>", methods=["POST"])
def op_lista(tipo, operacion):
    lista = listas.get(tipo)
    if lista is None:
        return jsonify({"error": "tipo no valido"})
    data = request.json or {}
    try:
        if operacion == "insertar":
            lista.insertar(int(data["valor"]))
            return jsonify({"resultado": f"insertado {data['valor']}"})
        elif operacion == "eliminar":
            lista.eliminar(int(data["valor"]))
            return jsonify({"resultado": f"eliminado {data['valor']}"})
        elif operacion == "buscar":
            import io, sys
            buf = io.StringIO()
            sys.stdout = buf
            lista.buscar(int(data["valor"]))
            sys.stdout = sys.__stdout__
            return jsonify({"resultado": buf.getvalue().strip()})
        elif operacion == "mostrar":
            import io, sys
            buf = io.StringIO()
            sys.stdout = buf
            if tipo == "simple":
                lista.mostrar()
            else:
                lista.mostrar_adelante()
            sys.stdout = sys.__stdout__
            return jsonify({"resultado": buf.getvalue().strip()})
        elif operacion == "mostrar_atras":
            import io, sys
            buf = io.StringIO()
            sys.stdout = buf
            lista.mostrar_atras()
            sys.stdout = sys.__stdout__
            return jsonify({"resultado": buf.getvalue().strip()})
    except Exception as e:
        return jsonify({"error": str(e)})


# --- ordenamientos ---
@app.route("/ordenar/<algoritmo>", methods=["POST"])
def ordenar(algoritmo):
    data = request.json or {}
    try:
        nums = [int(x) for x in data["valores"]]
        algos = {
            "bubble":    bubble_sort,
            "selection": selection_sort,
            "quick":     quick_sort,
            "shaker":    cocktail_sort,
            "merge":     merge_sort,
            "gnome":     gnome_sort,
            "shell":     shell_sort,
            "insertion": insertion_sort,
            "comb":      comb_sort,
        }
        fn = algos.get(algoritmo)
        if fn is None:
            return jsonify({"error": "algoritmo no valido"})
        resultado = fn(nums)
        return jsonify({"resultado": str(resultado)})
    except Exception as e:
        return jsonify({"error": str(e)})


# --- busquedas ---
@app.route("/buscar/<tipo>", methods=["POST"])
def buscar(tipo):
    data = request.json or {}
    try:
        nums = [int(x) for x in data["lista"]]
        objetivo = int(data["objetivo"])
        if tipo == "lineal":
            pos = busqueda_lineal(nums, objetivo)
            return jsonify({"resultado": f"posicion: {pos}"})
        elif tipo == "binaria":
            pos, ordenados = busqueda_binaria(nums, objetivo)
            return jsonify({"resultado": f"lista ordenada: {ordenados} | posicion: {pos}"})
    except Exception as e:
        return jsonify({"error": str(e)})


# --- arboles ---
@app.route("/arboles/<tipo>/<operacion>", methods=["POST"])
def op_arbol(tipo, operacion):
    arbol = arboles.get(tipo)
    if arbol is None:
        return jsonify({"error": "tipo no valido"})
    data = request.json or {}
    try:
        import io, sys
        buf = io.StringIO()
        sys.stdout = buf
        if operacion == "insertar":
            arbol.insertar(int(data["valor"]))
        elif operacion == "inorder":
            arbol.inorder()
        elif operacion == "preorder":
            arbol.preorder()
        elif operacion == "postorder":
            arbol.postorder()
        elif operacion == "buscar":
            arbol.buscar(int(data["valor"]))
        sys.stdout = sys.__stdout__
        return jsonify({"resultado": buf.getvalue().strip() or "ok"})
    except Exception as e:
        sys.stdout = sys.__stdout__
        return jsonify({"error": str(e)})


# --- grafos ---
@app.route("/grafos/ciudades", methods=["GET"])
def ciudades():
    return jsonify({"ciudades": list(grafo.keys())})


@app.route("/grafos/conexiones", methods=["GET"])
def conexiones():
    resultado = []
    for nodo, vecinos in grafo.items():
        for v, p in vecinos:
            resultado.append(f"{nodo} -> {v} ({p} km)")
    return jsonify({"resultado": "\n".join(resultado)})


@app.route("/grafos/prim", methods=["POST"])
def ruta_prim():
    data = request.json or {}
    inicio = data.get("inicio")
    if inicio not in grafo:
        return jsonify({"error": "ciudad no encontrada"})
    aristas, total = prim_mst(grafo, inicio)
    lineas = [f"{o} -> {d} ({p} km)" for o, d, p in aristas]
    return jsonify({"resultado": "\n".join(lineas) + f"\nTotal: {total} km"})


@app.route("/grafos/ruta", methods=["POST"])
def ruta_corta():
    data = request.json or {}
    inicio = data.get("inicio")
    fin = data.get("fin")
    if inicio not in grafo or fin not in grafo:
        return jsonify({"error": "ciudad no encontrada"})
    ruta = floyd_warshall(grafo)
    camino, distancia = ruta(inicio, fin)
    if camino is None:
        return jsonify({"error": "no hay ruta disponible"})
    return jsonify({"resultado": " -> ".join(camino) + f"\nDistancia: {distancia} km"})


# --- validaciones ---
@app.route("/validar/<tipo>", methods=["POST"])
def validar(tipo):
    data = request.json or {}
    valor = data.get("valor", "")
    fns = {
        "entero":  validar_entero,
        "decimal": validar_decimal,
        "hora":    validar_hora,
        "correo":  validar_correo,
        "web":     validar_pagina_web,
    }
    fn = fns.get(tipo)
    if fn is None:
        return jsonify({"error": "tipo no valido"})
    ok, resultado = fn(valor)
    return jsonify({"ok": ok, "resultado": resultado})


if __name__ == "__main__":
    print("Servidor corriendo en http://localhost:5000")
    app.run(debug=True)
