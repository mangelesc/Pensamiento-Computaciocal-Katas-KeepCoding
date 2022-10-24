def repartir_pizzas():
    while True: 
        try: 
            personas = int(input('Personas: '))
            pizzas = int(input('Pizzas: '))
        except:
            print('Ups, inserta un dato numerico')

        if personas>0 or pizzas<0: 
            if personas % 2 == 1:
                porciones = personas + 1
            else: 
                porciones = personas

            return ('Hay {} con {} pizzas.\nCada persona toma {} porciones.\nSobran {} porciones.\n'
            .format(personas,pizzas,pizzas,(porciones*pizzas)%personas))

        else: 
            print('Ups, introduce un numero positivo')

print(repartir_pizzas())