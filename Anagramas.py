#Función para tachar o borrar un carácter de una palabra
def tacha(caracter,palabra):
    lpalabra = list(palabra)
    lpalabra.remove(caracter)
#     palabra = "".join(palabra)
#     return palabra
    return "".join(lpalabra)

def anagrama(p1,p2):
    if len(p1) != len(p2):
        return False
    
    else: 
        print("Las palabras {} y {} son anagramas: ".format(p1,p2))
        p1 = p1.lower()
        p2 = p2.lower()
        for letra in p1:
            if letra in p2:
                p2 = tacha(letra,p2)
            else:
                return False
    #     if p2 == ""
    #         return True
    #     else
    #         return False
        return p2==""

#Pedimos información por pantalla
w1 = input("Palabra 1: ")
w2 = input("Palabra 2: ")

print(anagrama(w1,w2))