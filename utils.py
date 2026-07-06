# valor especial para salir desde cualquier submenu
SALIR = "SALIR"


# espera a que el usuario presione enter
def pausa():
    input("\nEnter para continuar...")


# muestra un titulo con bordes
def encabezado(titulo):
    print(f"\n===== {titulo} =====")


# pide un numero entero al usuario
def pedir_entero(mensaje="Ingrese un numero: "):
    texto = input(mensaje)
    if texto.strip() == "":
        return 0
    return int(texto)


# pide varios numeros separados por coma
def pedir_lista():
    texto = input("Valores separados por coma: ")
    if texto.strip() == "":
        return []
    return [int(x.strip()) for x in texto.split(",")]


# muestra las opciones del menu y devuelve la opcion elegida
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
