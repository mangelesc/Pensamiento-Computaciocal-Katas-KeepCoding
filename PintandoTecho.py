import math
from tokenize import Double

def areaRectangulo():
    while True:
        try: 
            longitud = float(input("¿Longitud de la habitación en metros? "))
            profundo = float(input("¿Profundo de la habitación en metros? "))
        except:
            print('Ups, inserta un dato numerico')

        if longitud <0 or profundo < 0:
            print('Ups, debe ser un numero positivo')
        
        else: 
            area = longitud * profundo
            return(area)

def areaCirculo():
    while True:
        try: 
            radio = float(input("¿Radio de la habitación en metros? "))
        except:
            print('Ups, inserta un dato numerico')

        if radio < 0:
            print('Ups, debe ser un numero positivo')
        
        else: 
            area = math.pi * pow(radio, 2)
            return(area)

#FALTA ESTA FUNCION!!
def areaL():
    pass


def botesPintura():
    index = int(input())
    
    if index == 1:
        area1 = areaRectangulo()

    elif index == 2:
        area1 = areaCirculo()

    elif index == 3:
        area1 = areaL()

    else:
        print('Introduce un valor correcto')

    
    tasaLitros = 0.05

    litros = area1 * tasaLitros
    botes = litros // 5

    if litros % 5 > 0:
        botes += 1

    return ('Necesitaras {} litros para pintar {} metros cuadrados de techo. \nDebes comprar {} botes de pintura.'
    .format(round(litros,2), round(area1,2),botes))


print (botesPintura())
