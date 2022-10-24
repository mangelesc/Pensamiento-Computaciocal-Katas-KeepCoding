import string

ALFABETO = list(string.ascii_uppercase)

def cesar(letra,clave):
    letra = letra.upper()
    posicion = ALFABETO.index(letra)
    nposicion = posicion + clave
    nposicion = nposicion % len(ALFABETO) #Cogiendo el resto de la division, no tendriamos problemas si la posicion es mas grande que la longitud
    return ALFABETO[nposicion]

def encriptar(mensaje,clave):
    resultado = ''
    for caracter in mensaje:
        ncaracter = cesar(caracter,clave)
        resultado += ncaracter
    return resultado


