class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

class Profesor:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad
        self.experiencia = experiencia

class Grupo_asignatura:
    def __init__(self, nombre, horario, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.horario = horario
        self.profesor = profesor
        self.estudiantes = []


    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print("Estudiante agregado exitosamente")

    def promedio(self):
        acumulador = 0 
        for estudiante in self.estudiantes:
            acumulador = acumulador + estudiante.nota
        promedio = acumulador/len(self.estudiantes)
        return promedio 
    
    def mostrar_estudiante(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)
    
profesor = Profesor("Juancho", 35, 5)
poo = Grupo_asignatura("Programación orientada a objetos", "m-v 10-12", "62", profesor)
estudiante1 = Estudiante("Esteban dias", 17, 5)
estudiante2 = Estudiante("Jorge", 20, 2.5)
estudiante3 = Estudiante("Luis", 21, 3)

poo.agregar_estudiante(estudiante1)
poo.agregar_estudiante(estudiante2)
poo.agregar_estudiante(estudiante3)

print(poo.promedio())

poo.mostrar_estudiante()
