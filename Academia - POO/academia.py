class Asignatura():
    #Construtor con __init__ y los atributos van dentro despues de self. (o att. despues del class)
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel 
        self.hora = 7.5 


    #Metodos de la clase
    def __str__(self):
        return 'Asignatura: {} - {} - {:.2f} €/h'.format(self.nombre, self.nivel, self.hora)

    def __repr__(self):
        return self.__str__()
        
class Alumno():
    #Construtor con __init__ y los atributos van dentro despues de self. (o att. despues del class)
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos 
        self.mail = ''

        self.asignaturas = []
    
    #Metodos de la clase
    def alta_asignaturas(self, asignatura):
        if not isinstance(asignatura, Asignatura): #Si no es de la instancia Asignatura
            raise Exception('{} debe ser del tipo Asignatura'.format(asignatura)) # Si entra, para el programa

        self.asignaturas.append(asignatura)
    
    def __str__(self):
        return 'Alumno: {} {} - {}'.format(self.nombre, self.apellidos, self.mail)

    def __repr__(self):
        return self.__str__()


class Profesor():
    def __init__(self, nif, nom, ap, mail, sueldoBase=200):
        self.nombre = nom
        self.apellidos = ap
        self.nif = nif
        self.tlf = ''
        self.sueldoBase = sueldoBase
        self.mail = mail

        self.asignaturas = []


    def alta_asignaturas(self, asignatura):
        if not isinstance(asignatura, Asignatura): #Si no es de la instancia Asignatura
            raise Exception('{} debe ser del tipo Asignatura'.format(asignatura)) # Si entra, para el programa

        self.asignaturas.append(asignatura)

    def __str__(self):
        return 'Profesor: {} -  {} {}- {}'.format(self.nif, self.nombre, self.apellidos, self.mail,)

    def __repr__(self):
        return self.__str__()

    def sueldo(self): #Creamos la funcion sueldo 
        return self.sueldoBase + len(self.asignaturas) * 300