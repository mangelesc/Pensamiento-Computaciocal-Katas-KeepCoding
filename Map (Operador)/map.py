# ***** OPERADOR MAP *****

frutas = ['platano', 'fresa', 'naranja']

lfConAsterisco = list(map(lambda p: '*' + p + '*', frutas)) 
#Map devuelve un iterable propio, pero ese iterable yo puedo transformarlo en lo que quiera, es esta caso en una lista

print(lfConAsterisco)
