"""class Animal:
    def __init__ (self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

    def orinar(self):
        print(f'{self.nombre} esta orinando')

class Perro(Animal):
    def __init__(self, nombre, color_pelota):
        super().__init__(nombre)
        self.color_pelota = color_pelota

    def hacer_sonido(self):
        print(f"{self.nombre} hace guau guau")
    
    def salir_pasear(self):
        print(f"{self.nombre} sale a pasear")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace miau miau")


animal1 = Perro("Mia", "Rojo")
animal1.hacer_sonido()
animal1.salir_pasear()
animal1.orinar()

animal2 = Gato("Simba")
animal2.hacer_sonido()
animal2.orinar()

print(isinstance(animal1, Perro))
print(isinstance(animal1, Animal))
print(issubclass(Perro, Animal))
print(issubclass(Gato, Animal))
print(issubclass(Perro, Gato))"""""

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        print(f"{self.nombre} esta respirando")

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} esta estudiando {self.carrera}")

persona1 = Persona("Juan")
persona1.respirar()

persona1 = Estudiante("Camilo", "Ingenieria de sistemas")
persona1.estudiar()
