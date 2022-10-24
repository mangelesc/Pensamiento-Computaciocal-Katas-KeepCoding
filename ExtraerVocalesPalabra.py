#Definimos la función
def ExtraerVoc(word):
    voc = ""
    for car in word:
        if car.upper() in "AEIOUÁÉÍÓÚÄËÏÖÜ":
            voc += car
    print("Los vocales de la palabre {} son: {}".format(word,voc))

#Pedimos por pantalla la palabra
palabra = input("Palabra: ")
ExtraerVoc(palabra)