def interes_simple(inversion, interes, anyos):
    ganancia = round(inversion * (1 + (interes/100)*anyos), 2)
    
    print(f'Tras {anyos} años de inversion al {interes}%, su cantidad dede ser {ganancia}')
    return ganancia

#pedimos los datos
while True:
    try: 
        inversion = float(input('Inversión: '))
        interes = float(input('Interés (porcentaje): '))
        anyos = float(input('Tiempo de inversión (años): '))
        if inversion>0 and interes>0 and anyos>0:
            break
        else:
            print('Ups, los numeros negativos NO son validos')
    except:
            print('Ups, datos incorrectos')

interes_simple(inversion, interes, anyos)