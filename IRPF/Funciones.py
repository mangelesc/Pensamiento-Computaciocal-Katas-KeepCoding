def calcular_exencion(situacion, hijos):
    cantidadRestar = 0 
    if situacion == 1:
        if hijos <= 0:
            cantidadRestar = 0 
        elif hijos == 1:
            cantidadRestar = 15947 
        else:
            cantidadRestar = 17100 

    elif situacion == 2:
        if hijos <= 0:
            cantidadRestar = 15546 
        elif hijos == 1:
            cantidadRestar = 16481 
        else:
            cantidadRestar = 17634 
    elif situacion == 3:
        if hijos <= 0:
            cantidadRestar = 14000 
        elif hijos == 1:
            cantidadRestar = 14516 
        else:
            cantidadRestar = 15063
    return cantidadRestar

def calcular_retencion(base):
    if base <= 0:
        porcentaje = 0 
    elif base <= 12450:
        porcentaje = 19 
    elif base <= 20200:
        porcentaje = 24 
    elif base <= 35200:
        porcentaje = 30 
    elif base <= 60000:
        porcentaje = 37 
    elif base <= 300000:
        porcentaje = 45 
    else: porcentaje = 47
    
    return porcentaje
