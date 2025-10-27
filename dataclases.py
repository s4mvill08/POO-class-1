from dataclasses import dataclass, field, asdict
import operaciones
from typing import List


@dataclass(frozen=True) #Congela los atributos de los objetos
class Persona1:
    __nombre: str #=field(default=False)
    edad: int = field(default=35)
    
    @property    
    def retornar_edad_por_2(self) -> int:
        return self.edad *2     #or -> None:
           
@dataclass 
class Puesto:
    nombre: str
    persona: Persona1
    
@dataclass
class Grupo:
    personas: List[Persona1] = field(default_factory=list)
    #or lista vacio = (Lista: []) o tambien se puede (lista: List[int])  
    
class Persona2:
    def __init__(self, nombre, edad=35):
        self.nombre = nombre
        self.edad = edad
        
persona1 = Persona1("Sam", 45)
persona2 = Persona2("Teo")

print(persona1.retornar_edad_por_2)

puesto1= Puesto("Desarrollador", persona1)

grupo1 = Grupo()
grupo1.personas.append(persona1)
grupo1.personas.append(persona2)

print(grupo1)

print(operaciones.suma(persona1.edad, persona2.edad))

print(puesto1)

print(asdict(persona1))

if persona1 ==  persona2:
    print("son iguales")
else:
    print("No son iguales")
