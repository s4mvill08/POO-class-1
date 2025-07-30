# POO-class-1

poo

# POO-class-2
class perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza 
    def ladrar(self):
        print("El perro que esta ladrando: ", self.nombre)

print("Hola mundo")

class persona:
    def __init__(self, edad, sexo):
        self.edad = edad
        self.sexo = sexo 

print("Hola")

#Vamos a instanciar un objeto desde la clase perro
mi_perro = perro("Juancho", "Golden")
print(mi_perro.nombre)
print(mi_perro.raza)


print("Mi segudo perrito")
mi_otro_perro = perro ("Paco", "Chihuahua")
print(mi_otro_perro.nombre)
print(mi_otro_perro.raza)

print("Ingrese el nombre del tercer perrito")
nombre = input("Ingrese el nombre")
raza = input("Ingrese la raza")

mi_tercer_perro = perro(nombre, raza)
print("Los datos del tercer perro")
print(mi_tercer_perro.nombre)
print(mi_tercer_perro.raza)

print("Los perros van a ladrar")
mi_perro.ladrar()
mi_otro_perro.ladrar()
mi_tercer_perro.ladrar()
