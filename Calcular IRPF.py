# ¿Quien eres?
nombre = input("Hola, ¿Cómo te llamas? ");
print("Hola", nombre);

# Datos de entrada
sueldo = float(input ("Sueldo: "));
situacion = int(input ("Situacion (1/2/3): "));
hijos = int(input ("Número de hijos: "));

# Obtenemos exencion
cantidadRestar = 0;

if situacion == 1:
    if hijos <= 0:
        cantidadRestar = 0;
    elif hijos == 1:
        cantidadRestar = 15947;
    else:
        cantidadRestar = 17100;

elif situacion == 2:
    if hijos <= 0:
        cantidadRestar = 15546;
    elif hijos == 1:
        cantidadRestar = 16481;
    else:
        cantidadRestar = 17634;

elif situacion == 3:
    if hijos <= 0:
        cantidadRestar = 14000;
    elif hijos == 1:
        cantidadRestar = 14516;
    else:
        cantidadRestar = 15063;

# Retencion
sar = float(sueldo - cantidadRestar);
p = 0;

if sar <= 12450:
    p = 19;
elif sar <= 20200:
    p = 24;
elif sar <= 35200:
    p = 30;
elif sar <= 60000:
    p = 37;
elif sar <= 300000:
    p = 45;
else: p = 47;

# Monto
montoAnual = sar * p / 100;
montoMensual = montoAnual / 12;

# Resultados
print("\n", nombre, "a continuación le mostramos los resultados:\n");
print("Sueldo anual:\t", sueldo);
print("Situación:\t", situacion);
print("Base a retener:\t", sar);
print("Porcentaje:\t", p);
print("Total anual:\t", montoAnual);
print("\nRETENCIÓN MENSUAL:\t", montoMensual);