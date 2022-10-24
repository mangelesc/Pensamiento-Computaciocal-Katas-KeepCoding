# Defino la función
def TablasMultiplicar(n):
    for m in range (0,11):
        print("{:>2} x {} = {:>2}".format(m, n, m*n))

#Pedimos el multiplicador
num = int(input("Número: "))
TablasMultiplicar(num)