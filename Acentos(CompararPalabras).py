import unicodedata

def quitarAcentos(word):
    word = word.replace(" ", "").replace(".","").replace("ñ", "#").replace("Ñ", "%")
    word = unicodedata.normalize("NFKD", word)\
     .encode("ascii","ignore").decode("ascii")\
     .replace("#", "ñ").replace("%", "Ñ")
    
    return word.lower()
    
a = input("Palabra: ")
print(quitarAcentos(a))