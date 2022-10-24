import getpass
from unittest import result

CONTROL = {1:'VeryWeak', 2:'Weak', 3:'Strong', 4:'veryStrong'}
LETTERS = list("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ ")
NUMBERS = list("0123456789")

def VeryWeak(password):
    result = False
    if len(password) < 8:
        result = True
        for w in list(password):
            result = result and w in NUMBERS
    return result

def Weak(password):
    result = False
    if len(password) < 8:
        result = True
        for w in list(password):
            result = result and (w in NUMBERS or w in LETTERS)
    return result

def Strong(password):
    pass

def veryStrong(password):
    pass

#def validaPwd(password):
#    if veryStrong(password):
#       return 4
#    elif Strong(password):
#        return 3
#    elif Weak(password):
#        return 2
    




#password = getpass.getpass('Contraseña: ')

#print(validaPwd(password))