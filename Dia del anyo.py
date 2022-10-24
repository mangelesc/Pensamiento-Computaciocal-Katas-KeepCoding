#Contar los días
contadorDias = 0
diasMes = [31,28,31,30,31,30,31,31,30,31,30,31]

#FUNCION: bisiesto
def bisiesto(anio):
    if anio % 4 != 0:
        return False
    
    if anio % 100 == 0 and anio % 400 != 0:
        return False
    
    return True

#Datos
dia = int(input("Día: "))
mes = int(input("Mes: "))
anyo = int(input("Año: "))

#Es bisiesto?
# if bisiesto(anyo) == True (EQUIVALENTE)
if bisiesto(anyo):
    diasMes[1] = 29
    
i = 0
while i < mes - 1:
    contadorDias += diasMes[(i)]
    i += 1

contadorDias += dia

#Imprimir resultado
print("Es el día: ", contadorDias)
    