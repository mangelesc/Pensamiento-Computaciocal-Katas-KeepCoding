def FraseAbsurda():
    nombre = input("Nombre: ")
    verbo = input("Verbo: ")
    adverbio = input("Advervio: ")
    adjetivo = input("Adjetivo: ")

    return 'Un/a {} {} debe {} {}'.format(nombre, adjetivo, verbo, adverbio)

print(FraseAbsurda())