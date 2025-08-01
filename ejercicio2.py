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

print("Bienvenido al sistema de gestión de estudiantes")
lista_estudiantes = []
while True:
    print("Seleccione la opción deseada")
    print("1.   Agregar estudiante")
    print("2. Mostrar la información del estudiante")
    print("0, Salir")
    opcion = int(input())
    if opcion == 1:
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
        lista_estudiantes.append(estudiante)
        print("Estudiantes registadro correctamente")
    elif opcion == 2:
        numero_estudiantes = len(lista_estudiantes)
        print("EL numero de estudiantes es", numero_estudiantes)
        for estudiantes in lista_estudiantes:
            print("El nombre del estudiante es ", estudiante.nombre)
            print("El promedio del estudiante es ", estudiante.Calcular_promedio())
    elif opcion == 0:
        print("Hasta luego")
        break 
    else:
        print("opcion no valida")