def conversor_euro(origen, cantidad):
    paises = {'EUR': 1, 'USD':0.99828, 'GBP':0.86476, 'CAD':11.30981, 'AUD': 1.46471}
    divisa_origen = paises.get(origen)
    divisa = cantidad * divisa_origen 
    
    print(f'Valor de cambio {origen} a EUR: {paises.get(origen)} \n{cantidad} {origen} = {divisa} EUR')
    return round(divisa,2)



moneda_convertir = input('Moneda de origen: ').upper()

while True: 
    try: 
        cantidad = float(input('Cantidad a convertir en €: '))
        if cantidad > 1:
            break
        else: 
            print('Ups, inserta un número positivo')
    except:
        print('Ups, inserta un dato numerico')


conversor_euro(moneda_convertir,cantidad)