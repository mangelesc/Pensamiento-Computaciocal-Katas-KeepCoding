def MatSencilla():
    try: 
        n1 = float(input('Numero 1: '))
        n2 = float(input('Numero 2: '))
    
    except:
        print('Ups, inserta un dato numerico')

    if n1<0 or n2<0:
        return 'Ups has introducido un numero negativo'

    elif n1=='' or n1=='': 
        return 'Ups tienes que introducir ambos numeros'

    else: 
        n = [n1,n2]

        return "{} + {} = {}\n{} - {} = {}\n{} · {} = {}\n{} / {} = {}\n".format(n[0], n[1], n[0]+n[1], 
        n[0], n[1], n[0]-n[1], n[0], n[1], n[0]*n[1], n[0], n[1], n[0]/n[1])


def MatSencillaWhile():
    #DO WHILE con python
    while True:
        try: 
            n1 = float(input('Numero 1: '))
            n2 = float(input('Numero 2: '))
        
        except:
            print('Ups, inserta un dato numerico')
        
        if n1 >= 0 and n2 >= 0:
            n = [n1,n2]

            return "{} + {} = {}\n{} - {} = {}\n{} · {} = {}\n{} / {} = {}\n".format(n[0], n[1], n[0]+n[1], 
            n[0], n[1], n[0]-n[1], n[0], n[1], n[0]*n[1], n[0], n[1], n[0]/n[1])
        
        else:
            print ('Ups datos incorrectos')

print(MatSencillaWhile())
print(MatSencilla())