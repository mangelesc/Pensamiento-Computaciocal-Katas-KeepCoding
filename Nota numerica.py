def nota_numerica(letra):
    diccionario_valores = {'A+':4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'D-':0}
    letra = letra.upper()
    print("Su nota es: ")
    return diccionario_valores.get(letra, -1)

clave = input("Letra: ")

print(nota_numerica(clave))