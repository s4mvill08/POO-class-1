import random
class estudiantes:
    def __init__(self, nombre, edad, nota1, id):
        self.nombre = nombre
        self.edad = edad
        self.nota1 = nota1
        self.id = id
                 
    def mostrar_datos(self):
        print("nombre:", self.nombre)
        print("edad:", self.edad)
        print("nota1:", self.nota1)
        print("id:", self.id)

print("Bienvenido al sistema de gestión de estudiantes")
lista_estudiantes = []

while True:
    print("Seleccione la opción deseada")
    print("1. Agregar estudiante")
    print("2. Mostrar la información del estudiante")
    print("0. Salir")
    opcion = int(input())
            
    if opcion == 1:
        print("Bienvenido a la gestión del estudiante")
        
        while True:
            id = random.randint(1000, 9999)
            id_existe = False
            for estudiante in lista_estudiantes:
                if estudiante.id == id:
                    id_existe = True
                    break
            if id_existe == False:
                break
        
        print("Su id es:", id)
        print("Ingrese el nombre")
        nombre = input()
        print("Ingrese su edad")
        edad = int(input())
        print("Ingrese su nota1")
        nota1 = float(input())
                
        estudiante = estudiantes(nombre, edad, nota1, id)
        lista_estudiantes.append(estudiante)
        print("Estudiante registrado correctamente")
    
    elif opcion == 2:
        numero_estudiantes = len(lista_estudiantes)
        print("El numero de estudiantes es", numero_estudiantes)
                
        if numero_estudiantes == 0:
            print("No hay estudiantes registrados")
        else:
            id_ingresado = int(input("Ingrese el id del estudiante: "))
                        
            encontrado = False
            for estudiante in lista_estudiantes:
                if estudiante.id == id_ingresado:
                    estudiante.mostrar_datos()
                    encontrado = True
                    break
                        
            if encontrado == False:
                print("Estudiante no encontrado")
              
    elif opcion == 0:
        print("Hasta luego")
        break
            
    else:
        print("opcion no valida, intente de nuevo")