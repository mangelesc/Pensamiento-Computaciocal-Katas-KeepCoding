def ImpirmirComillas(): 
    cita = input('Cita: ')
    autor = input('Autor: ')

    return '"{}", {}'.format(cita, autor)

print(ImpirmirComillas())