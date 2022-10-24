def frecuencias(word):
    resultado = {}
    for letra in word:
        if letra in resultado:
            resultado[letra] += 1
        else:
            resultado[letra] = 1
    return resultado

def es_anagrama(p1,p2):
    return frecuencias(p1) == frecuencias(p2)