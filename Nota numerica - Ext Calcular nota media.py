def nota_numerica(clave):
    diccionario_valores = {'A+':4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'D-':0}
    clave = clave.upper()
    if diccionario_valores.get(clave, -1) != -1:
        print("Su nota es: ")
        print(diccionario_valores.get(clave))
        return diccionario_valores.get(clave)
    print('Ups, has introducido un valor erroneo')
    return -1


def media():
    nota_total = 0
    n_notas = 0

    nota = input("Nota o vacio para acabar: ")

    while nota != '':
        valor = nota_numerica(nota)
        if valor != -1:
            n_notas += 1
            nota_total += valor
        nota = input("Nota o vacio para acabar: ")
    if n_notas == 0:
        print('No se han introducido datos')
    else:
        media = nota_total / n_notas
        print('La nota media es: ', media)