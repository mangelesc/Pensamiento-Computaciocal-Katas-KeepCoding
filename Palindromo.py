import unicodedata

#Definimos la función
def Palindromo(word):
    #Quitamos los espacios y reemplazamos las tildes, ñ y diéresis usando la librería de
    #unicodedata
    word = word.replace(" ", "").replace(".","").replace("ñ", "#").replace("Ñ", "%")
    word = unicodedata.normalize("NFKD", word)\
     .encode("ascii","ignore").decode("ascii")\
     .replace("#", "ñ").replace("%", "Ñ")
    
    word = word.lower()
    return word == word[::-1]
# !!Sería igual que: 
#     if word == word[::-1]
#         print(word::-1)
#         return True
#     else:
#         return False
        

#Pedimos por pantalla la palabra o cadena
pal = input("Palabra o cadena: ")

print(Palindromo(pal))