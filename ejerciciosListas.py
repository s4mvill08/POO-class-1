#Opcion larga
import random
lista = []
for i in range(10):
    lista.append(random.randint(10,99))
    
print(lista)

#Opcion corta
lista2 = [random.randint(10,99) for _ in range(10)]
print(lista2)

lista_ejemplo = [i for i in range(0,10)]
print(lista_ejemplo)

lista_ejemplo[2] = 10
lista_ejemplo[5] =5

print(lista_ejemplo)

#Eliminar un elemento
lista_ejemplo.remove(5)
print(lista_ejemplo)

#Eliminar por posicion
del lista_ejemplo[2]
print(lista_ejemplo)

lista_ejemplo = [elemento for elemento in lista_ejemplo if elemento != 1]
print(lista_ejemplo)

lista_ejemplo.sort()
print(lista_ejemplo)

lista_ejemplo.reverse()
print(lista_ejemplo)

lista_ejemplo.sort(reverse=True)
print(lista_ejemplo)

import random
class persona:
    def __init___(self, nombre):
        self.nombre = nombre
        self.numero = [random.randint(100,999) for i in range(5)]
        
persona1 = persona("Stiven")
persona2 = persona("Juan")

print("Los numeros para", persona.nombre, "son", persona1.numeros)
print("Los numeros para", persona2, "son", persona2.numeros)
