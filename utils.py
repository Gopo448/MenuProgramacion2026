SALIR = "SALIR"


# Pausa la pantalla
def pausa():
    input("\nEnter para continuar...")


# Muestra un titulo simple
def encabezado(titulo):
    print(f"\n===== {titulo} =====")


# Pide un numero entero
def pedir_entero(mensaje="Ingrese un numero: "):
    texto = input(mensaje)
    if texto.strip() == "":
        return 0
    return int(texto)


# Pide varios numeros
def pedir_lista():
    texto = input("Valores separados por coma: ")
    if texto.strip() == "":
        return []
    return [int(valor.strip()) for valor in texto.split(",")]


# Muestra opciones numeradas
def mostrar_menu(titulo, opciones, volver=True):
    encabezado(titulo)
    for numero, texto in opciones:
        print(f"{numero}. {texto}")
    if volver:
        print("0. Volver")
        print("99. Salir")
    else:
        print("0. Salir")
    return input("\nSeleccione una opcion: ")
