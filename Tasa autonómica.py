def tasa_autonomica(provincia,precio):
    
    if provincia[:2] == 'VA':
        TASA_VAL = 5.5
        tasa = precio * (TASA_VAL/100)
        total = round(tasa + precio, 2)

        print(f'El subtotal es {precio}€\nLa tasa es {tasa}€\nEl total es {total}€')
        return total

    else:
        print(f'NO se aplica ninguna tasa.\nEl total es {precio}€')
        return precio


#Pedimos los datos
provincia = input('Provincia: ').upper()
while True: 
    try: 
        precio = float(input('Precio: '))
        if precio > 0:
            break
    except:
        print('Ups, introduce un dato numérico')


tasa_autonomica(provincia, precio)