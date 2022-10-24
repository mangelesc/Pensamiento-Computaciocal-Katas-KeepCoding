from academia import *

angela = Alumno('Angela', 'Cordoba')
daniel = Alumno('Daniel', 'Fernandez')

print(angela)
print(daniel)

ingles = Asignatura('Ingles', 'A2')

aleman = Asignatura('Aleman', 'A1')
aleman.hora = 15

chino = Asignatura('Chino', 'A1')
chino.hora = 17


angela.alta_asignaturas(ingles)
angela.alta_asignaturas(chino)
daniel.alta_asignaturas(aleman)

print(angela.asignaturas)
print(daniel.asignaturas)

donJose = Profesor('0W', 'Jose', 'Martin', 'j@mail.com')

print(donJose)

donJose.alta_asignaturas(ingles)

print(donJose.asignaturas)

print(donJose.sueldo())
