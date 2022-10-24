def producto_total(indice): 

    #Bucle para pedir datos hasta que se introduzca una cantidad correcta
    while True: 
        try: 
            print (f'PRODUCTO {indice+1}')
            precio = float(input(f'Precio: '))
            cantidad = float(input(f'Cantidad: '))
            return precio*cantidad  
        except:
            print('Ups, inserta un dato numerico')
            pass


def productos(): 
    while True:
        try: 
            #Pedimos el numero de productos que el usuario quiere introducir
            index = int(input('¿Cuántos productos quieres añadir?'))
            if index > 0: 
                break
            else: 
                print('Ups, introduce un número positivo')
        except:
            print('Ups, inserta un dato numerico')
    subtotal = 0
    #Bucle para pedir precios y cantidades
    for i in range(index):
        producto = producto_total(i)
        subtotal += producto
        print(f'Total producto {i+1}: {producto}')
        
    print (f'Has añadido {index} productos.\nSUBTOTAL: {subtotal}')
    return subtotal    


def calcular_total_con_impuestos():
    TAX = 5.5

    subtotal= productos()
    tasas = subtotal * TAX
    total = subtotal + tasas

    print(f'Tasas: {tasas}\nTOTAL: {total}')
    return total


calcular_total_con_impuestos()