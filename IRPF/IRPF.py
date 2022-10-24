from Funciones1 import *

# ¿Quien eres?
nombre = input("Hola, ¿Cómo te llamas? ");
print("Hola", nombre);

# Datos de entrada
sueldo = float(input ("Sueldo: "));
situacion = input ("Situacion (1/2/3): ");
hijos = int(input ("Número de hijos: "));

resta = calcular_exencion(situacion,hijos)
base = float(sueldo - resta)
porcentaje = calcular_retencion_for(base)

# Monto
montoAnual = base * porcentaje / 100;
montoMensual = montoAnual / 12;

# Resultados
print("\n", nombre, ", a continuación le mostramos los resultados:\n");
print("Sueldo anual:\t", sueldo);
print("Situación:\t", situacion);
print("Base a retener:\t", base);
print("Porcentaje:\t", porcentaje);
print("Total anual:\t", montoAnual);
print("\nRETENCIÓN MENSUAL:\t", montoMensual);