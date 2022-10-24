from datetime import date

def tiempo_jubilacion():
    try: 
        edad = int(input('Cuántos años tienes?'))
        edad_jub = int(input('A qué edad te jubilarás?'))
    except:
        print('Ups, inserta un dato numerico')


    anyo_actual = date.today().year
    tiempo_restante_jubilacion = edad_jub - edad
    anyo_jubilacion = anyo_actual + tiempo_restante_jubilacion

    if tiempo_restante_jubilacion < 0: 
        return 'Ya puedes jubilarte!'
    else:
        return 'Te quedan {} años para jubilarte. \nEstamos en {}, te jubilarás en {}.'.format(tiempo_restante_jubilacion, anyo_actual, anyo_jubilacion)

print(tiempo_jubilacion())