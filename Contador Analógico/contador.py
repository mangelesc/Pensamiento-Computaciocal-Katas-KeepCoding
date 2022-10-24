def creaContador(ini = 0): #Si no se introduce valor, empieza desde 0 por defecto
    clicks = ini

    def click():
        nonlocal clicks
        clicks = clicks + 1
        return clicks
    
    return click