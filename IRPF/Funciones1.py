# Tambien se podria hacer una lista de listas, pero con un diccionario quedaria mas legible
EXCENCIONES = {'1':[0,15947,17100],
               '2':[15546,16481,17634],
               '3':[14000,14516,15063]}

def calcular_exencion(situacion, hijos):
    if hijos > 2:
        hijos = 2
    elif hijos < 0:
        hijos = 0
    
    return EXCENCIONES[situacion][hijos]
    

# RANGOS = [0, 12450, 20200, 35200, 60000, 300000]
# PORCENTAJE = [0, 19, 24, 30, 37, 45, 47]
# 
# def cacular_retencion_while(base):
#     i=0
#     while i < len(RANGOS):
#         if base <= RANGOS[i]:
#             break
#         i += 1
#     return PORCENTAJE[i]

RETENCIONES = [[0,0],[12450,19],[20200,24],[35200,30],[60000,37],[300000,45],[float('inf'),47]]

def calcular_retencion_for(base):
#     for rango in RETENCIONES:
#         if base <= rango[0]:
#             return rango[1]
    for rango, porcentaje in RETENCIONES:
        if base <= rango:
             return porcentaje
        
    