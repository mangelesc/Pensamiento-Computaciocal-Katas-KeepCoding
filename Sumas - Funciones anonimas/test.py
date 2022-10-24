from funciones import *

print(sumaTodos(100), sumatorio(100))

print(sumaTodosAlCuadrado(3))

def cuadrado(x):
    return x ** 2

print(sumatorio(3, cuadrado))

#Para no tener que crear una nueva funcion, usamos una funcion lambda

print(sumatorio(3, lambda x: x*x))