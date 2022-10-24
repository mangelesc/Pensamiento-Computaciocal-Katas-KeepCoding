def voz_alta(texto):
    return texto.upper() + '!!'

def voz_baja(texto):
    return chr(129323) + ' ' + texto.lower()

gritando = voz_alta
susurrando = voz_baja

def saludar(saludo, modo):
    saludo_format = modo(saludo)
    print('*'*len(saludo_format))
    print(saludo_format)
    print('.'*len(saludo_format))