def contarCaracteres(): 
    cadena = input('Introduce cadena: ')
    
    while cadena == '':
        print ('Ups, introduce algo')
        cadena = input('Introduce cadena: ')
    
    return'La cadena {} tiene {} caracteres'.format(cadena, len(cadena))

print(contarCaracteres())