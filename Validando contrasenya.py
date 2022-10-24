import getpass

DATOS = {'Angela': '1234', 'Daniel': '5678'}

def ValidarPassword(datos):
    user = input('Usuario: ')
    password = getpass.getpass('Contraseña: ')
    a= datos.get(user)
    if datos.get(user) == password:
        print(f'{user}, entró en el sistema')
        return True
    else: 
        print(f'Ups, no te conozco, prueba a introducir otro usuario o contraseña')
        return False

print(ValidarPassword(DATOS))