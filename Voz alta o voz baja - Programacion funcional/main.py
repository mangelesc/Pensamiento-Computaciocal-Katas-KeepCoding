from funciones import *

dialolo = [
    ('Hola', gritando),
    ('Por favor', None),
    ('Adios', voz_baja)
]

for frase, modo in dialolo:
    if modo == None:
        print(frase)
    else:
        print(modo(frase))

saludar('Hola', gritando)


