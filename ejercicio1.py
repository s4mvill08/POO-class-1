class estudiantes:
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        self.nombre = nombre
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        
    def mostrar_datos(self):
        print("nombre", self.nombre)
        print("edad", self.edad)
        print("nota1", self.nota1)
        print("nota2", self.nota2)
        print("nota3", self.nota3)

    def Calcular_promedio(self):
        promedio =(self.nota1 + self.nota2 + self.nota3) / 3
        return promedio 
    
print("Bienvenido a la gestión del estudiante")
print("Ingrese el nombre")
nombre = input()
print("Ingrese su edad")
edad = int(input())
print("Ingrese su nota1")
nota1 = float(input())
print("Ingrese su nota3")
nota2 = float(input())
print("Ingrese su nota3")
nota3 = float(input())
estudiante = estudiantes(nombre, edad, nota1, nota2, nota3)

promedio_estudiante = estudiante.Calcular_promedio()
print("El promedio de ", estudiante.nombre, " es de ", promedio_estudiante)