METROS_YARDA = 0.9144

def area_rectangulo():
    try: 
        longitud = float(input("¿Longitud de la habitación en metros? "))
        profundo = float(input("¿Profundo de la habitación en metros? "))
    except:
        print('Ups, inserta un dato numerico')

    s_metros = longitud * profundo
    s_yardas = longitud * profundo / METROS_YARDA ** 2

    return(f"Superficie de la habitación en metros cuadrados: {s_metros}\nSuperficie de la habitación en yardas cuadradas: {s_yardas}")


#Elegir entre metros o yardas
def area_rectanguloElegir():
    
    while True:
        opcion = input('Quieres calcular en metros o yardas?: (M o Y)').upper()
        
        if opcion == 'M':
            try: 
                longitud = float(input("¿Longitud de la habitación en metros? "))
                profundo = float(input("¿Profundo de la habitación en metros? "))
            except:
                print('Ups, inserta un dato numerico')

            s_metros = longitud * profundo
            return (f"Superficie de la habitación en metros cuadrados: {s_metros}")
        
        elif opcion == 'Y':
            try: 
                longitud = float(input("¿Longitud de la habitación en yardas? "))
                profundo = float(input("¿Profundo de la habitación en yardas? "))
            except:
                print('Ups, inserta un dato numerico')
            
            s_yardas = longitud * profundo / METROS_YARDA ** 2
            return(f"Superficie de la habitación en yardas cuadradas: {s_yardas}")

        else: 
            print('Ups, M para metros o Y para yardas')

print(area_rectanguloElegir())

print(area_rectangulo())