# validaciones de distintos tipos de datos


# valida que sea un entero entre 1 y 3999
def validar_entero(texto):
    if len(texto) == 0:
        return False, "error: no ingresaste nada"

    for c in texto:
        if c < '0' or c > '9':
            return False, "error: solo se aceptan digitos"

    valor = int(texto)

    if valor >= 1 and valor <= 3999:
        return True, f"numero valido: {valor}"
    else:
        return False, "error: el numero debe estar entre 1 y 3999"


# valida que sea un numero decimal con exactamente un punto
def validar_decimal(texto):
    if len(texto) == 0:
        return False, "error: no ingresaste nada"

    pos_punto = -1

    for i, c in enumerate(texto):
        if c == '.':
            if pos_punto != -1:
                return False, "error: solo se permite un punto decimal"
            pos_punto = i
        elif c < '0' or c > '9':
            return False, "error: solo se aceptan digitos y un punto decimal"

    if pos_punto == -1:
        return False, "error: falta el punto decimal"

    parte_entera = texto[:pos_punto]
    parte_decimal = texto[pos_punto + 1:]

    if len(parte_entera) == 0 or len(parte_decimal) == 0:
        return False, "error: ambas partes deben tener digitos"

    return True, f"numero decimal valido: {float(texto):.2f}"


# valida que la hora tenga formato hh:mm
def validar_hora(texto):
    if len(texto) != 5:
        return False, "error: el formato debe ser hh:mm"

    if texto[2] != ':':
        return False, "error: falta el signo :"

    for i in [0, 1, 3, 4]:
        if texto[i] < '0' or texto[i] > '9':
            return False, "error: solo se aceptan numeros en la hora"

    hh = int(texto[0:2])
    mm = int(texto[3:5])

    if hh >= 0 and hh <= 23 and mm >= 0 and mm <= 59:
        return True, f"hora valida: {texto}"
    else:
        return False, "error: hora no valida"


# valida que el correo tenga formato correcto y dominio permitido
def validar_correo(texto):
    if len(texto) == 0:
        return False, "error: no ingresaste nada"

    arroba = -1
    punto = -1

    for i, c in enumerate(texto):
        if c == '@':
            if arroba != -1:
                return False, "error: solo se permite un @"
            arroba = i
        if c == '.':
            punto = i
        if not (c.isalpha() or c.isdigit() or c in '@._-'):
            return False, "error: el correo tiene caracteres no validos"

    if arroba <= 0 or punto < arroba + 2:
        return False, "error: correo no valido"

    dominios = ["@gmail.com", "@hotmail.com", "@yahoo.com"]
    dominio_valido = any(texto.endswith(d) for d in dominios)

    if not dominio_valido:
        return False, "error: solo se permiten gmail.com hotmail.com y yahoo.com"

    return True, f"correo valido: {texto}"


# valida que la url tenga protocolo y dominio valido
def validar_pagina_web(texto):
    if len(texto) < 10:
        return False, "error: url no valida"

    if not (texto.startswith("http://") or texto.startswith("https://") or texto.startswith("www.")):
        return False, "error: debe iniciar con http:// https:// o www."

    dominios = [".com", ".mx", ".org", ".net", ".edu"]
    dominio_valido = any(d in texto for d in dominios)

    if not dominio_valido:
        return False, "error: solo se permiten dominios .com .mx .org .net .edu"

    return True, f"url valida: {texto}"


# pide el valor al usuario y muestra el resultado
def menu_validacion(tipo, mensaje, funcion):
    from utils import pausa
    valor = input(mensaje)
    ok, resultado = funcion(valor)
    print(resultado)
    pausa()
    return ok
