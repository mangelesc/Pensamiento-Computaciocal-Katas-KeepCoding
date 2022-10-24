def sumaTodos(n):
    resultado = 0 
    for i in range(n + 1):
        resultado += i
    return resultado

def sumaTodosAlCuadrado(n):
    resultado = 0 
    for i in range(n + 1):
        resultado += i ** 2 # i elevado a 2
    return resultado

def sumatorio(n, funcion=None):
    resultado = 0 
    for i in range(n + 1):
        if funcion == None:
            n_i = i
        else:
            n_i = funcion(i)
        resultado += n_i
    return resultado