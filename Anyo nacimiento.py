# ¿Quien eres?
nombre = input("Hola, ¿Cómo te llamas? ");
print("Hola", nombre);

# Toma de datos
edad = input("¿Qué edad tienes? ");
edad = int(edad);
anyoActual = input("¿Qué anyo es? ");
anyoActual = int(anyoActual);

hasCumplido = input("¿Has cumplido años? (S/N)");

if hasCumplido == "S" :
     anyoNacimiento = anyoActual - edad;
else:
    anyoNacimiento = anyoActual - edad;
    anyoNacimiento = anyoNacimiento - 1;
    
# Resultados
print(nombre, ", naciste en", anyoNacimiento );

