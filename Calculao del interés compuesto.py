def interes_compuesto(inversion, interes, anyos, vecesAnyo):
    formula = inversion *(1 + (interes/100)/vecesAnyo)**(vecesAnyo*anyos)
    ganancia = round(formula, 2)
    
    print(f'{inversion}€ invertidos al {interes}% durante {anyos} años con {vecesAnyo} periodos de imposición po año se transforman un {ganancia}€')
    return ganancia

#pedimos los datos
while True:
    try: 
        inversion = float(input('Cantidad de inversión: '))
        interes = float(input('Interés anual (porcentaje): '))
        anyos = float(input('Tiempo de inversión (años): '))
        vecesAnyo = int(input('Periodos al año: '))
        if inversion>0 and interes>0 and anyos>0:
            break
        else:
            print('Ups, los numeros negativos NO son validos')
    except:
            print('Ups, datos incorrectos')

interes_compuesto(inversion, interes, anyos, vecesAnyo)